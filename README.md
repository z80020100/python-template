# Python Template

A Python project template with pre-configured code formatting and development tools.

## Features

- **Python 3.13** support
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

## Code Formatting

### Automatic Formatting in VS Code

The project is configured to automatically format Python code on save using Black formatter. Make sure you have the [Black Formatter extension](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter) installed.

### Manual Formatting

Format all Python files with Black:

```bash
uv run black .
```

Sort imports with isort:

```bash
uv run isort .
```

Format and sort in one command:

```bash
uv run black . && uv run isort .
```

## Configuration

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
- **black**: Format Python code
- **isort**: Sort Python imports

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
2. Follow the existing code style (Black formatting)
3. Ensure imports are sorted (isort)
4. Test your changes before committing

## Requirements

- Python 3.13+
- uv (for dependency management)
- VS Code with Black Formatter extension (recommended)
