# Textual Tutorial

A terminal-based user interface application built with [Textual](https://github.com/Textualize/textual), demonstrating a menu system, log data visualization, and various UI components.

Article & Video coming soon...

## Features

- Interactive menu navigation with keyboard controls
- Log data visualization with sortable columns
- Component showcase demonstrating various Textual widgets
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

The application features three main screens:

1. **Main Menu**
   - Use ↑/↓ arrows to navigate
   - Press Enter to select an option
   - Options include:
     - Component Showcase
     - Log Viewer
     - Quit

2. **Component Showcase**
   - Demonstrates various Textual widgets and interactions
   - Features:
     - Button variants (Success, Warning, Error)
     - Text input with live feedback
     - Toggle switch
     - Animated progress bar
   - Press `ESC` to return to menu

3. **Log Viewer**
   - Displays log data in a sortable table
   - Keyboard shortcuts:
     - `ESC`: Return to menu
     - `T`: Sort by timestamp
     - `L`: Sort by log level
     - `M`: Sort by message
     - `U`: Sort by user ID
   - Interactive features:
     - Click column headers to sort
     - Color-coded log levels
     - Row selection

## Project Structure

```
textual_tutorial/
├── app.py              # Main application entry point
├── components/
│   └── menu.py        # Menu widget implementation
├── screens/
│   ├── log_screen.py     # Log viewer screen
│   └── showcase_screen.py # Component showcase screen
├── styles.tcss        # Textual CSS styling
└── logs/
    └── demo_log.csv   # Sample log data
```

## Development

This project is built with:
- [Textual](https://github.com/Textualize/textual) for the TUI framework
- Poetry for dependency management
- Type hints throughout the codebase
- Reactive programming patterns for UI state management

### Key Components

- **MenuWidget**: Custom widget for navigation with keyboard controls
- **LogScreen**: Data visualization with sorting capabilities
- **ShowcaseScreen**: Interactive demonstration of Textual widgets
- **Styling**: Custom TCSS (Textual CSS) for consistent visual design

## License

[MIT License](LICENSE)

