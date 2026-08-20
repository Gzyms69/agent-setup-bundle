---
name: skill-stealth-scraping
description: Advanced anti-bot evasion, stealth web scraping, TLS/JA3/HTTP2 fingerprint management, browser automation (Playwright/Puppeteer), CAPTCHA handling, and reverse engineering internal private APIs. Use when collecting web data from protected platforms (Cloudflare, Akamai, DataDome, PerimeterX).
---

# Stealth Web Scraping & Anti-Detection Skill

This skill defines protocols and technical countermeasures for extracting structured intelligence and data from websites protected by modern anti-bot and Web Application Firewall (WAF) systems.

---

## 1. Hierarchy of Data Extraction Techniques

Always choose the least detectable and most efficient extraction vector:

```
┌────────────────────────────────────────────────────────────────────────┐
│ Level 0: Agentic MCP Web Scrapers (Firecrawl MCP & Puppeteer MCP)      │
│ - Firecrawl MCP for LLM-ready clean Markdown and automated bypass      │
│ - Puppeteer MCP for direct DOM exploration and interactive sessions     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ If complex auth or native API
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Level 1: Reverse Engineering Private/Internal JSON APIs (Fastest, Best)│
│ - Inspect mobile app / Web SPA network requests                        │
│ - Replay HTTP requests with exact headers, cookies & TLS tokens        │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ If blocked / Signature required
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Level 2: Headless Browser Automation with Stealth Patches              │
│ - Playwright / Puppeteer with stealth patches & CDP evasions           │
│ - Human mouse curves, scrolling, and random jitter                     │
└───────────────────────────────────┬────────────────────────────────────┘
                                    │ If Cloudflare Turnstile / DataDome
                                    ▼
┌────────────────────────────────────────────────────────────────────────┐
│ Level 3: Residential Proxy Pools + Full Profile Emulation              │
│ - Rotating residential IPs + realistic browser fingerprints            │
└────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Anti-Detection Countermeasures Checklist

When automating headless browsers or sending raw HTTP requests, verify the following:

### 1. Browser Fingerprint Hardening:
- **`navigator.webdriver`**: Must be overridden to `false` / `undefined`.
- **`chrome.runtime` & Plugins**: Emulate genuine Chrome plugin arrays.
- **WebGL / Canvas Fingerprints**: Inject consistent WebGL vendor (`Google Inc. (NVIDIA)`) and renderer strings.
- **AudioContext & Hardware Concurrency**: Emulate realistic hardware concurrency (`8` or `16` cores, `8GB` device memory).
- **Permissions API**: Return `'prompt'` or `'granted'` for notifications instead of anomalous undefined states.

### 2. Network & TLS Fingerprints (JA3 / JA4 / HTTP2):
- Standard Python `requests` or `urllib` emit a Python TLS fingerprint that is trivially blocked by Cloudflare.
- **Countermeasure:** Use HTTP clients that support TLS fingerprint spoofing (e.g. `curl_cffi`, `tls-client`, or real browser instances).

### 3. Human Behavioral Emulation:
- Never click instantly on DOM coordinates without randomized delays.
- Use Bezier curve mouse movements (`playwright-extra` or human motion generators).
- Introduce realistic keystroke jitter (50ms - 150ms per keypress) for input fields.

---

## 3. Playwright / Python Implementation Blueprint

```python
from playwright.async_api import async_playwright
import asyncio
import random

async def launch_stealth_browser(headless: bool = True):
    p = await async_playwright().start()
    browser = await p.chromium.launch(
        headless=headless,
        args=[
            "--disable-blink-features=AutomationControlled",
            "--no-sandbox",
            "--disable-infobars",
            "--disable-dev-shm-usage",
            "--disable-extensions",
        ]
    )
    
    context = await browser.new_context(
        user_agent="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        viewport={"width": 1920, "height": 1080},
        locale="en-US",
        timezone_id="America/New_York",
    )
    
    # Evaluate evasions before any script runs
    await context.add_init_script("""
        Object.defineProperty(navigator, 'webdriver', { get: () => undefined });
        window.chrome = { runtime: {} };
    """)
    
    page = await context.new_page()
    return browser, page

async def human_type(page, selector: str, text: str):
    await page.click(selector)
    for char in text:
        await page.type(selector, char, delay=random.randint(50, 180))
```

---

## 4. Ethical & Safety Mandates

1. Respect rate limits to prevent denial of service (DoS) on target servers.
2. Never store or expose unencrypted session cookies containing sensitive private user sessions.
3. Automatically delete ephemeral browser sessions and profiles upon completion.
