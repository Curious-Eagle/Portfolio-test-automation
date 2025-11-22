import pytest
import os
from playwright.sync_api import Page, expect


@pytest.fixture(autouse=True)
def set_timeout(page: Page):
    page.set_default_timeout(10000)
    yield

def pytest_html_report_title(report):
    report.title = "Portfolio Automation Test Report"

def pytest_configure(config):
    try:
        from pytest_metadata.plugin import metadata_key
        config.stash[metadata_key]["Project"] = "Siva Portfolio"
        config.stash[metadata_key]["Tester"] = "Automation Bot"
    except ImportError:
        # Fallback or ignore if plugin not present
        pass
