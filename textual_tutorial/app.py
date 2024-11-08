from textual.app import App, ComposeResult
from textual.widgets import Header, Footer
from textual.containers import Container
from textual.screen import Screen

from textual_tutorial.components.menu import MenuWidget, MENU_OPTIONS
from textual_tutorial.screens.log_screen import LogScreen


class MainScreen(Screen):
    """Main application screen containing the menu."""

    def compose(self) -> ComposeResult:
        """Create child widgets for the screen."""
        yield Header(show_clock=True)
        yield Container(MenuWidget(MENU_OPTIONS), id="menu-container")
        yield Footer()

    def on_menu_widget_item_selected(self, message: MenuWidget.ItemSelected) -> None:
        """Handle menu item selection."""
        selected_option = MENU_OPTIONS[message.index]

        if selected_option.action == "exit":
            self.app.exit()
        elif selected_option.action == "open_logs":
            # Push the LogScreen onto the stack
            self.app.push_screen(LogScreen())
        elif selected_option.action == "show_notification":
            # Show a notification
            self.notify("This is a test notification!")


class MenuApp(App[None]):
    """A Textual app to manage several screens."""

    CSS_PATH = "styles.tcss"
    TITLE = "Menu Demo"
    SUB_TITLE = "Select an option"

    def on_mount(self) -> None:
        """Mount the main screen when the app starts."""
        self.push_screen(MainScreen())


def run():
    """Run the application."""
    app = MenuApp()
    app.run()


if __name__ == "__main__":
    run()
