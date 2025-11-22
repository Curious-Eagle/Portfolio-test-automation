# Portfolio Automation Suite

This repository contains the automation testing suite for [www.sivaamir.com](https://www.sivaamir.com).

## Overview
- **Framework**: Playwright + Pytest
- **Schedule**: Runs daily at 09:00 UTC via GitHub Actions.
- **Target**: Tests the live production website.

## Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Install Browsers:
   ```bash
   playwright install chromium
   ```

## Running Tests

Run the tests against the live site:

```bash
pytest --base-url https://www.sivaamir.com --html=report.html
```
