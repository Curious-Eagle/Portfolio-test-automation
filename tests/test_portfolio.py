import pytest
from playwright.sync_api import Page, expect

def test_portfolio_page_structure(page: Page, base_url):
    page.goto(f"{base_url}/portfolio.html")
    expect(page).to_have_title("Siva - Personal Portfolio")
    
    # Sidebar check
    expect(page.locator(".sidebar")).to_be_visible()
    expect(page.locator(".name")).to_contain_text("Siva Amirthalingam")
    expect(page.locator(".title").first).to_contain_text("QA Engineer/Data Scientist")

def test_navbar_navigation(page: Page, base_url):
    page.goto(f"{base_url}/portfolio.html")
    
    # Check default active page is About
    expect(page.locator("article.about")).to_have_class("about  active")
    
    # Click Resume
    page.get_by_role("button", name="Resume").click()
    expect(page.locator("article.resume")).to_have_class("resume active")
    
    # Click Portfolio
    page.get_by_role("button", name="Portfolio").click()
    expect(page.locator("article.portfolio")).to_have_class("portfolio active")
    
    # Click Contact
    page.get_by_role("button", name="Contact").click()
    # Just verify button exists as we didn't see contact section in file
    expect(page.get_by_role("button", name="Contact")).to_be_visible()

def test_theme_toggle(page: Page, base_url):
    page.goto(f"{base_url}/portfolio.html")
    
    theme_btn = page.locator("#theme-toggle")
    expect(theme_btn).to_be_visible()
    theme_btn.click()
    expect(theme_btn).to_be_visible()

def test_social_links(page: Page, base_url):
    page.goto(f"{base_url}/portfolio.html")
    
    # Check LinkedIn
    linkedin = page.locator(".social-list a[href*='linkedin.com']")
    expect(linkedin).to_be_visible()
    
    # Check GitHub - target the one in the social list sidebar
    github = page.locator(".social-list a[href*='github.com']")
    expect(github).to_be_visible()

def test_download_resume_button(page: Page, base_url):
    page.goto(f"{base_url}/portfolio.html")
    
    resume_btn = page.locator(".resume-btn")
    expect(resume_btn).to_be_visible()
    expect(resume_btn).to_have_attribute("download", "Siva_Amirthalingam_Resume.docx")
