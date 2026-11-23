import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

CRIATIVOS_DIR = Path(r"c:\Users\dluzgg\Documents\antigravity\serene-newton\prospector-de-sites\dashboard\sites\safra-agro-paraiso\assets\criativos")
INPUT_HTML = CRIATIVOS_DIR / "carousel.html"

TOTAL_SLIDES = 5
VIEW_W = 420
VIEW_H = 525
SCALE = 1080 / 420  # 2.57142857... -> 1080x1350

async def export():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(
            viewport={"width": VIEW_W, "height": VIEW_H},
            device_scale_factor=SCALE,
        )

        content = INPUT_HTML.read_text(encoding="utf-8")
        await page.set_content(content, wait_until="networkidle")
        await page.wait_for_timeout(3000)  # Wait for Google Fonts

        # Strip preview wrapper so slide fills exact viewport
        await page.evaluate("""() => {
            const header = document.querySelector('.ig-header');
            if (header) header.style.display = 'none';

            const frame = document.querySelector('.ig-frame');
            if (frame) {
                frame.style.cssText = 'width:420px;height:525px;max-width:none;border-radius:0;box-shadow:none;border:none;overflow:hidden;margin:0;';
            }

            const viewport = document.querySelector('.carousel-viewport');
            if (viewport) {
                viewport.style.cssText = 'width:420px;height:525px;aspect-ratio:unset;overflow:hidden;cursor:default;';
            }

            document.body.style.cssText = 'padding:0;margin:0;display:block;overflow:hidden;background:#000;';
        }""")
        await page.wait_for_timeout(500)

        for i in range(TOTAL_SLIDES):
            await page.evaluate("""(idx) => {
                const track = document.querySelector('.carousel-track');
                track.style.transition = 'none';
                track.style.transform = 'translateX(' + (-idx * 420) + 'px)';
            }""", i)
            await page.wait_for_timeout(400)

            out_file = CRIATIVOS_DIR / f"slide_{i+1}.png"
            await page.screenshot(
                path=str(out_file),
                clip={"x": 0, "y": 0, "width": VIEW_W, "height": VIEW_H}
            )
            print(f"Exported: {out_file.name}")

        await browser.close()
        print("All slides exported successfully!")

asyncio.run(export())
