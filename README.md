# Automation Exercise Test Project

Playwright Python end-to-end tests for [automationexercise.com](https://automationexercise.com/).

## Setup

```powershell
uv sync --dev
uv run playwright install
```

For account-based tests, copy `.env.example` to `.env` and fill in the optional credentials.

## Run Tests

```powershell
uv run pytest
uv run pytest -m smoke
uv run pytest --headed
```

## Quality Checks

```powershell
uv run ruff check .
uv run ruff format --check .
uv run mypy pages tests conftest.py
```

## Structure

- `pages/`: page objects and reusable UI components
- `tests/`: pytest test modules and test-level fixtures
- `conftest.py`: project-wide fixtures and environment loading
