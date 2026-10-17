/* Browser-only inquiry preparation. No submission, tracking or persistent storage. */
(function(root){
'use strict';
const offers={'TRAV-XTR':'XTR Pro 5G Wi-Fi Router','TRAV-J5':'JourneyGo 5G Hotspot','TRAV-J4':'JourneyGo 4G Hotspot','RPE-PBS':'Phoenix Business System','RPE-PNC':'Phoenix Nexus Capital','RPE-DIBANA':'DIBANA','GENERAL':'General inquiry'};
const sources=['direct','services','youtube','facebook'];
function prepare(input,ref){
 if(!Object.hasOwn(offers,input.offer))throw Error('Choose a listed offer.');
 if(input.consent!==true)throw Error('Review and accept the inquiry disclosure.');
 const message=String(input.message||'').trim();if(message.length<10||message.length>1500)throw Error('Enter a question between 10 and 1,500 characters.');
 const source=sources.includes(input.source)?input.source:'direct';
 if(!/^RPE-WEB-[a-f0-9-]{36}$/.test(ref))throw Error('Invalid inquiry reference.');
 const body=`RPE Services inquiry\nPreparation reference: ${ref}\nOffer: ${input.offer} — ${offers[input.offer]}\nSource code (customer-declared, not verified attribution): ${source}\nDisclosure: SERVICES-INQUIRY-1.0\nAcknowledgment: I reviewed the privacy notice and choose to send this inquiry to RPE. No partner sharing is authorized.\n\nQuestion:\n${message}\n\nThis reference identifies a prepared inquiry, not receipt, an application, an order or a sale. Please retain the case reference issued after actual receipt.`;
 return {ref,body,mailto:'mailto:contact@risingphoenixhq.com?subject='+encodeURIComponent(`RPE Services inquiry [${ref}] ${input.offer}`)+'&body='+encodeURIComponent(body)};
}
if(typeof module!=='undefined')module.exports={prepare,offers,sources};
if(!root.document)return;
const form=document.getElementById('commercialInquiry');if(!form)return;
const out=document.getElementById('inquiryPreview'),open=document.getElementById('openInquiry'),status=document.getElementById('inquiryStatus');
let ref=null;
const params=new URLSearchParams(root.location.search);if(Object.hasOwn(offers,params.get('offer')))form.elements.offer.value=params.get('offer');if(sources.includes(params.get('source')))form.elements.source.value=params.get('source');
function invalidate(){open.hidden=true;open.removeAttribute('href');out.hidden=true;status.textContent='Changes are not yet prepared. Review your inquiry again.';}
form.addEventListener('input',invalidate);
form.addEventListener('submit',event=>{event.preventDefault();try{
 if(!form.reportValidity())return;
 if(!root.crypto?.randomUUID)throw Error('Secure reference generation is unavailable. Please email contact@risingphoenixhq.com directly.');
 if(!ref)ref='RPE-WEB-'+root.crypto.randomUUID();
 const v=prepare({offer:form.elements.offer.value,source:form.elements.source.value,message:form.elements.message.value,consent:form.elements.consent.checked},ref);
 out.textContent=v.body;out.hidden=false;open.href=v.mailto;open.hidden=false;status.textContent='Prepared locally. Nothing has been sent. Open your email app, review and send the message.';out.focus();
}catch(e){status.textContent=e.message;open.hidden=true;open.removeAttribute('href');}});
})(typeof window==='undefined'?globalThis:window);
