"""Bounded source checks; does not substitute for browser or CATE acceptance."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit, unquote
import json, re, subprocess
root=Path(__file__).resolve().parents[1]
BASE='70e78b5d49eec5ac600e5acfa0c3d77365f9f647'
class Page(HTMLParser):
 def __init__(self,text):
  super().__init__();self.ids=set();self.links=[];self.nav=[];self.innav=False;self.feed(text)
 def handle_starttag(self,tag,attrs):
  a=dict(attrs)
  if 'id' in a: assert a['id'] not in self.ids, f'Duplicate id {a["id"]}';self.ids.add(a['id'])
  if tag=='nav' and a.get('aria-label')=='Services navigation':self.innav=True
  if tag=='a' and 'href' in a:
   self.links.append(a['href'])
   if self.innav:self.nav.append(a['href'])
 def handle_endtag(self,tag):
  if tag=='nav':self.innav=False
pages={p.name:Page(p.read_text()) for p in root.glob('*.html')}
expected=['products.html','business-services.html','business-financing.html','business-network.html','about.html','help.html']
checks=0
for name,page in pages.items():
 assert page.nav==expected, (name,page.nav)
 for link in page.links:
  u=urlsplit(link)
  if u.scheme or u.netloc:continue
  path=unquote(u.path).lstrip('/') or name
  if path=='':path='index.html'
  if u.path=='/':path='index.html'
  assert (root/path).is_file(),(name,link)
  if u.fragment and path in pages:assert unquote(u.fragment) in pages[path].ids,(name,link)
 checks+=1
catalog=json.loads((root/'offer-catalog.json').read_text())
assert len(catalog['offers'])==6
assert len({o['offer_id'] for o in catalog['offers']})==6
for o in catalog['offers']:
 assert o['commercially_active'] is False
 assert o['last_commercial_verification'] is None
 assert o['commission_terms'] is None
 assert (root/o['destination_url']).is_file()
 assert o['destination_url'] in pages['index.html'].links or o['category']=='connectivity'
checks+=6
# Existing content and interactions are unchanged outside header navigation/styles.
for name in subprocess.check_output(['git','ls-tree','--name-only',BASE],cwd=root,text=True).splitlines():
 if not name.endswith('.html'):continue
 before=subprocess.check_output(['git','show',BASE+':'+name],cwd=root,text=True)
 after=(root/name).read_text()
 def strip_changes(t):
  t=re.sub(r'<nav class="nav" aria-label="Services navigation">.*?</nav>','NAV',t,flags=re.S)
  t=re.sub(r'<style id="commercial-navigation">.*?</style>','',t,flags=re.S)
  if name=='help.html':t=t.replace('<h2>Product and business-service inquiries</h2><p><a class="btn" href="inquiry.html">PREPARE A REFERENCED INQUIRY</a></p>','')
  if name=='index.html':t=re.sub(r'<section id="commercial-destinations".*?</section>','',t,flags=re.S)
  return t
 assert strip_changes(before)==strip_changes(after),name+' existing content changed'
 checks+=1
assert 'No lender application or approved funding offer' in (root/'index.html').read_text()
assert 'Enrollment is unavailable' in (root/'index.html').read_text()
assert 'does not enroll you' in (root/'business-services.html').read_text()
print(f'PASS: {checks} page/catalog/preservation checks; all local links and fragment targets resolve. Browser/CATE acceptance not performed.')
