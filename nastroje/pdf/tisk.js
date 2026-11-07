// Vytiskne sestavené HTML do PDF pomocí Chromia (Playwright).
// Použití: node tisk.js <vstup.html> <vystup.pdf>
const { chromium } = require('playwright');

(async () => {
  const [vstup, vystup] = process.argv.slice(2);
  const prohlizec = await chromium.launch();
  const stranka = await prohlizec.newPage();
  // chyby ve vzorcích vypíšeme, ať se dají opravit
  stranka.on('console', z => { if (z.text().startsWith('CHYBA')) console.log(z.text()); });
  await stranka.goto('file://' + require('path').resolve(vstup), { waitUntil: 'load' });
  await stranka.waitForFunction(() => document.body.dataset.hotovo === '1');
  await stranka.evaluate(() => document.fonts.ready);
  await stranka.pdf({
    path: vystup,
    format: 'A4',
    printBackground: true,
    preferCSSPageSize: true,
    displayHeaderFooter: true,
    headerTemplate: '<span></span>',
    // číslo stránky dole uprostřed
    footerTemplate: '<div style="width:100%;text-align:center;font-size:9px;color:#888;font-family:DejaVu Sans,sans-serif"><span class="pageNumber"></span></div>',
  });
  await prohlizec.close();
})();
