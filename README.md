# Textual Tutorial

A terminal-based user interface application built with [Textual](https://github.com/Textualize/textual), demonstrating a menu system and log data visualization.

## Features

- Interactive menu navigation with keyboard controls
- Log data visualization with sortable columns
- Color-coded log levels (INFO, WARN, ERROR)
- Responsive terminal UI with custom styling

## Requirements

- Python 3.9 or higher

## Installation

This project uses Poetry for dependency management:

```bash
# Install poetry if you haven't already
pip install poetry

# Install dependencies
poetry install
```

## Usage

Run the application:

```bash
poetry run python -m textual_tutorial.app
```

### Navigation

The application features two main screens:

1. **Main Menu**
   - Use ↑/↓ arrows to navigate
   - Press Enter to select an option
   - Options include:
     - Screen One (Log Viewer)
     - Screen Two
     - Quit

2. **Log Viewer (Screen One)**
   - Displays log data in a sortable table
   - Keyboard shortcuts:
     - `ESC`: Return to menu
     - `T`: Sort by timestamp
     - `L`: Sort by log level
     - `M`: Sort by message
     - `U`: Sort by user ID

## Project Structure

```
textual_tutorial/
├── app.py              # Main application entry point
├── components/
│   └── menu.py        # Menu widget implementation
├── screens/
│   └── screen_one.py  # Log viewer screen
├── styles.tcss        # Textual CSS styling
└── logs/
    └── demo_log.csv   # Sample log data
```

## Development

This project is built with:
- [Textual](https://github.com/Textualize/textual) for the TUI framework
- Poetry for dependency management
- Type hints throughout the codebase

## License

[MIT License](LICENSE)

