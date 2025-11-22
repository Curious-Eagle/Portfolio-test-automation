import pytest
from playwright.sync_api import Page, expect

def test_home_page_title(page: Page, base_url):
    page.goto(f"{base_url}/index.html")
    expect(page).to_have_title("Siva Amirthalingam")

def test_loading_screen_disappears(page: Page, base_url):
    page.goto(f"{base_url}/index.html")
    # The loading screen has id "loadingScreen" and eventually gets "display: none"
    loading_screen = page.locator("#loadingScreen")
    expect(loading_screen).to_be_visible()
    # Wait for it to be hidden (it takes about 3-4 seconds based on the script)
    expect(loading_screen).to_be_hidden(timeout=10000)

def test_professional_panel_navigation(page: Page, base_url):
    page.goto(f"{base_url}/index.html")
    # Wait for loading screen to go away so we can click
    expect(page.locator("#loadingScreen")).to_be_hidden(timeout=10000)
    
    professional_panel = page.locator("#professional-choice")
    expect(professional_panel).to_be_visible()
    
    # Click and verify navigation
    professional_panel.click()
    expect(page).to_have_url(f"{base_url}/portfolio.html")

def test_photography_panel_navigation(page: Page, base_url):
    page.goto(f"{base_url}/index.html")
    expect(page.locator("#loadingScreen")).to_be_hidden(timeout=10000)
    
    photography_panel = page.locator("#photography-choice")
    expect(photography_panel).to_be_visible()
    
    # Click and verify navigation
    photography_panel.click()
    expect(page).to_have_url(f"{base_url}/gallery/index.html")
