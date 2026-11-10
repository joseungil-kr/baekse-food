/**
 * Actual public form screenshots + printable A4 PDF templates.
 * Read-only use of public pages with strictly fictitious sample information.
 */
import {chromium} from 'playwright';
import {mkdir,readFile} from 'node:fs/promises';
const base='https://order.baeksefood.com';
const assets=[
 {slug:'invoice-landscape',route:'/manual-invoice/',rows:15,form:'invoice'},
 {slug:'invoice-vertical',route:'/manual-invoice-vertical/',rows:10,form:'invoice-vertical'},
 {slug:'receipt',route:'/simple-receipt/',rows:15,form:'receipt'}
];
await mkdir('tmp-form-capture',{recursive:true});
await mkdir('static/downloads/print-forms',{recursive:true});
const browser=await chromium.launch({headless:true});
try{
 const context=await browser.newContext({viewport:{width:1440,height:1000},
  locale:'ko-KR',timezoneId:'Asia/Seoul',deviceScaleFactor:1,colorScheme:'light'});
 for(const item of assets){
  const page=await context.newPage(),badWrites=[];
  page.on('request',req=>{if(!['GET','HEAD'].includes(req.method()))badWrites.push(req.method()+' '+req.url())});
  const response=await page.goto(base+item.route,{waitUntil:'networkidle',timeout:60000});
  if(!response?.ok())throw Error('Real form did not load: '+item.slug+' HTTP '+response?.status());
  await page.locator('.print-sheet .slip').first().waitFor();
  if(await page.locator('.slip').count()!==2)throw Error('Expected two slips: '+item.slug);
  if(await page.locator('.slip[data-copy="supplier"] .item-table tbody tr').count()!==item.rows)
   throw Error('Unexpected row count: '+item.slug);
  if(await page.locator('body').getAttribute('data-form')!==item.form)throw Error('Wrong form '+item.slug);
  const fill=async(name,value)=>{
   const el=page.locator('.slip[data-copy="supplier"] [data-field="'+name+'"]');
   if(await el.count())await el.fill(value);
  };
  // Synthetic sample only; no operational or customer records.
  const values=[
   ['writtenDate','2026-11-10'],['slipNumber','예시-20261110'],
   ['supplier','백세푸드 (예시)'],['supplierNo','000-00-00000'],
   ['supplierPhone','000-0000-0000'],['supplierAddress','예시 주소 (공급자)'],
   ['buyer','거래처 예시'],['buyerNo','000-00-00001'],['buyerPhone','010-0000-0000'],
   ['buyerAddress','예시 주소 (공급받는자)'],['buyerContact','예시 담당자'],
   ['item-0-name','붕어빵 반죽'],['item-0-spec','5kg'],
   ['item-0-qty','2'],['item-0-price','12500'],
   ['item-1-name','팥앙금'],['item-1-spec','5kg'],
   ['item-1-qty','3'],['item-1-price','9000']
  ];
  for(const [key,value] of values)await fill(key,value);
  await page.locator('.print-sheet').screenshot({
   path:'tmp-form-capture/'+item.slug+'.png',animations:'disabled',type:'png'
  });
  if(badWrites.length)throw Error('Unexpected write request: '+JSON.stringify(badWrites));
  await page.close();

  const blank=await context.newPage();
  const blankResponse=await blank.goto(base+item.route+(item.form==='receipt'?'':'?blank=1'),
   {waitUntil:'networkidle',timeout:60000});
  if(!blankResponse?.ok())throw Error('Blank source unavailable: '+item.slug);
  await blank.locator('.print-sheet').waitFor();
  // The receipt does not have a blank-mode URL: clear every input and calculated cell
  // strictly in this temporary PDF-rendering browser. No server writes.
  if(item.form==='receipt'){
   await blank.evaluate(()=>{
    const root=document.querySelector('.print-sheet');
    root.querySelectorAll('input').forEach(input=>{input.value=''});
    root.querySelectorAll('[data-field]').forEach(el=>{
     if(el instanceof HTMLInputElement)el.dispatchEvent(new Event('input',{bubbles:true}));
    });
    root.querySelectorAll('[data-calc],[data-amount-korean],[data-mirror]')
     .forEach(el=>{el.textContent=''});
   });
  }
  const output='static/downloads/print-forms/'+item.slug+'.pdf';
  await blank.pdf({path:output,preferCSSPageSize:true,printBackground:true});
  await blank.close();
  const bytes=await readFile(output);
  if(bytes.subarray(0,5).toString()!=='%PDF-')throw Error('Not a PDF: '+output);
  console.log('REAL_FORM_SCREEN_AND_BLANK_PDF_CREATED',item.slug,bytes.length);
 }
 await context.close();
}finally{await browser.close()}
