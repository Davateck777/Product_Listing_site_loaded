/* Optional browser regression. npm install playwright; install Chromium first.
   Run AFTER assemble/build/validate. This checks behaviour, not supplier truth. */
const {chromium}=require('playwright'),fs=require('fs'),path=require('path');
const ROOT=path.resolve(__dirname,'..');
(async()=>{
 const b=await chromium.launch({headless:true}),page=await b.newPage({viewport:{width:1440,height:1000},acceptDownloads:true}),errors=[],checks=[];
 const assert=(ok,msg)=>{if(!ok)throw Error(msg);checks.push(msg)};page.on('pageerror',e=>errors.push(e.message));
 // Offline file mode must load without any HTTP resources.
 await page.route('http://**/*',r=>r.abort());await page.route('https://**/*',r=>r.abort());
 await page.goto('file://'+path.join(ROOT,'../kitchen-week2-product-listings.html'));await page.waitForSelector('.product');assert(await page.locator('.product').count()===40,'Initial40cards');
 for(let d=1;d<=5;d++){await page.locator('#day').selectOption('Day '+String(d).padStart(2,'0'));assert(await page.locator('.product').count()===40,'Day'+d+'40cards')}
 await page.locator('#day').selectOption('');assert(await page.locator('.product').count()===200,'All200view');
 await page.locator('#search').fill('Wood-Handle Stainless Steel Slicing Knife');assert(await page.locator('.product').count()===1,'Englishsearch');await page.locator('.description summary').click();assert(await page.locator('.details-copy h3').allTextContents().then(h=>h.join('|')==='What the Product is?|What are the clear benefits of the Product|Features of the Product'),'Exactthreeheadings');await page.locator('#search').fill('');
 await page.locator('#status').selectOption('freight');assert(await page.locator('.product').count()===13,'13conditionalfreight');await page.locator('#status').selectOption('shipping');assert(await page.locator('.product').count()===187,'187pendingfreight');await page.locator('#status').selectOption('jumia');assert(await page.locator('.product').count()===27,'27pendingJumia');await page.locator('#status').selectOption('');
 await page.locator('#group').selectOption('knives');assert(await page.locator('.product').count()===10,'10knives');await page.locator('#group').selectOption('');
 // Scenario arithmetic, minimums and immutable observations.
 const base=await page.evaluate(()=>({sale:KITCHEN_W2_QA.plan(CATALOG.products[0]).sale,source:CATALOG.products[0].source_price_cny}));await page.locator('#cnyFx').fill('400');assert(await page.evaluate(()=>KITCHEN_W2_QA.plan(CATALOG.products[0]).sale)>base.sale,'FXcalculator');assert(await page.evaluate(()=>CATALOG.products[0].source_price_cny)===base.source,'Observationimmutable');await page.locator('#sourceFloor').fill('1');await page.locator('#shipFloor').fill('1');assert(await page.evaluate(()=>KITCHEN_W2_QA.assumptions().floor>=5.2&&KITCHEN_W2_QA.assumptions().ship>=2000),'Enforcedfloors');await page.locator('#resetPlanning').click();assert(await page.evaluate(()=>KITCHEN_W2_QA.plan(CATALOG.products[0]).sale)===base.sale,'Reset');
 const mismatches=await page.evaluate(()=>CATALOG.products.filter(p=>KITCHEN_W2_QA.plan(p).sale!==p.planning.sale_ngn).map(p=>p.id));assert(!mismatches.length,'All200JSvsPythonprices');
 await page.locator('#day').selectOption('Day 01');await page.locator('#expand').click();assert(await page.locator('.description[open]').count()===40,'Expand40buyers');await page.locator('#expand').click();assert(await page.locator('.description[open]').count()===0,'Collapsecopy');
 await page.locator('[data-image="1"]').click();assert(await page.locator('#modal').isVisible(),'Imageviewer');await page.keyboard.press('Escape');assert(await page.locator('#modal').isHidden(),'Escapeclose');assert(await page.evaluate(()=>document.activeElement.dataset.image)==='1','Focusrestore');
 const dl=page.waitForEvent('download');await page.locator('#export').click();assert((await dl).suggestedFilename()==='kitchen-week2-200-current-planning.csv','CSVdownload');
 const failed=await page.evaluate(async()=>{let fails=[];await Promise.all(CATALOG.products.map(p=>new Promise(resolve=>{let i=new Image;i.onload=()=>resolve();i.onerror=()=>{fails.push(p.id);resolve()};i.src=p.images[0].local_path})));return fails});assert(!failed.length,'All200embeddedmainimages');
 // Responsive overflow and mobile accessibility.
 await page.evaluate(()=>scrollTo(0,0));const scratch=path.join(ROOT,'../research/kitchen-week2');if(process.env.KEEP_QA_SCREENSHOTS==='1'&&fs.existsSync(scratch))await page.screenshot({path:path.join(scratch,'qa-desktop.png')});
 await page.setViewportSize({width:390,height:844});assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth),'Mobile390nooverflow');await page.locator('[data-image="1"]').click();assert(await page.locator('#modal').isVisible(),'Mobileviewer');await page.locator('#closeModal').click();await page.evaluate(()=>scrollTo(0,0));if(process.env.KEEP_QA_SCREENSHOTS==='1'&&fs.existsSync(scratch))await page.screenshot({path:path.join(scratch,'qa-mobile.png')});
 // Team modular page must also work from file:// with local assets.
 await page.goto('file://'+path.join(ROOT,'index.html'));await page.waitForSelector('.product');assert(await page.locator('.product').count()===40,'Modularofflinepage');assert(errors.length===0,'NoJavaScripterrors');
 fs.writeFileSync(path.join(ROOT,'data/browser-qa.json'),JSON.stringify({result:'PASS',desktop:'1440x1000',mobile:'390x844',checks,errors,scope:'Interface/file regression only; not research completeness or safety certification'},null,2));await b.close();console.log('Browser QA PASS:',checks.length,'checks');
})().catch(e=>{console.error(e);process.exit(1)});
