const puppeteer = require('puppeteer');
(async () => {
const browser = await puppeteer.launch();
const page = await browser.newPage();
await page.goto('https://y.qq.com');
await page.screenshot({path: './yqq.png'});
browser.close();
})();