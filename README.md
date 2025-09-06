# Python Template

A Python project template with pre-configured code formatting and development tools.

## Features

- **Python 3.13** support
- **Ruff** - Modern Python linter and formatter
- **MyPy** - Static type checking
- **Black** code formatter for consistent code style
- **isort** for import sorting
- **Pre-commit hooks** for automated code quality checks
- **VS Code** configuration for seamless development experience

## Setup

### 1. Install Dependencies

This project uses [uv](https://docs.astral.sh/uv/) for dependency management:

```bash
uv sync
```

### 2. Install Pre-commit Hooks (Optional)

To enable automatic formatting and checks before each commit:

```bash
uv run pre-commit install
```

## Code Quality Tools

### Linting and Type Checking

Run Ruff linter to check for code quality issues:

```bash
uv run ruff check .
```

Auto-fix issues with Ruff:

```bash
uv run ruff check --fix .
```

Run MyPy for static type checking:

```bash
uv run mypy .
```

### Code Formatting

Format code with Ruff (recommended):

```bash
uv run ruff format .
```

Or use Black formatter:

```bash
uv run black .
```

Sort imports with isort:

```bash
uv run isort .
```

Run all checks at once:

```bash
uv run ruff check --fix . && uv run mypy . && uv run ruff format .
```

## Configuration

### Ruff Configuration

Ruff is configured in `pyproject.toml` with:

- Line length: 88 characters (compatible with Black)
- Target Python version: 3.13
- Enabled rules: pycodestyle, pyflakes, isort, flake8-bugbear, flake8-comprehensions, pyupgrade
- Auto-formatting with double quotes and proper indentation

### MyPy Configuration

MyPy is configured for strict type checking:

- Disallow untyped function definitions
- Warn about unused imports and redundant casts
- Check for unreachable code and missing return statements

### Black Configuration

Black is configured in `pyproject.toml` with:

- Line length: 88 characters
- Target Python version: 3.13
- Excludes common build/cache directories

### isort Configuration

isort is configured to be compatible with Black:

- Uses Black profile
- Same line length (88 characters)
- Consistent trailing commas and parentheses usage

### Pre-commit Hooks

The following hooks run before each commit:

- **trailing-whitespace**: Remove trailing whitespace
- **end-of-file-fixer**: Ensure files end with newline
- **check-yaml**: Validate YAML files
- **check-added-large-files**: Prevent large files from being committed
- **ruff**: Lint and auto-fix code issues
- **ruff-format**: Format code with Ruff
- **black**: Format Python code (fallback)
- **isort**: Sort Python imports
- **mypy**: Static type checking

## Development

### Running the Application

```bash
uv run python main.py
```

### Project Structure

```
.
├── .pre-commit-config.yaml    # Pre-commit configuration
├── .vscode/settings.json      # VS Code settings
├── main.py                    # Main application file
├── pyproject.toml             # Project configuration and dependencies
├── uv.lock                    # Dependency lock file
└── README.md                  # This file
```

## Contributing

1. Make sure all pre-commit hooks pass
2. Run linting and type checking: `uv run ruff check . && uv run mypy .`
3. Follow the existing code style (Ruff/Black formatting)
4. Ensure imports are sorted (isort)
5. Add type annotations to all functions
6. Test your changes before committing

## Requirements

- Python 3.13+
- uv (for dependency management)
- VS Code with Black Formatter extension (recommended)
