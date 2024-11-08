from textual.app import ComposeResult
from textual.screen import Screen
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import (
    Header,
    Footer,
    Button,
    Static,
    Input,
    Switch,
    Label,
    ProgressBar,
)
from textual.reactive import reactive
import asyncio


class ShowcaseScreen(Screen):
    """A screen showcasing various Textual components."""

    BINDINGS = [("escape", "app.pop_screen", "Back")]

    progress_value = reactive(0)
    progress_direction = reactive(1)

    def compose(self) -> ComposeResult:
        """Create child widgets for the screen."""
        yield Header(show_clock=True)

        with Container(id="showcase-container"):
            # Basic widgets section
            yield Static("Basic Widgets", classes="section-title")
            with Horizontal(classes="widget-row"):
                yield Button("Success!", id="success-button", variant="success")
                yield Button("Warning!", id="warning-button", variant="warning")
                yield Button("Error!", id="error-button", variant="error")

            # Input section
            yield Static("Input Components", classes="section-title")
            with Horizontal(classes="widget-row"):
                with Vertical():
                    yield Label("Text Input")
                    yield Input(placeholder="Type something...", id="demo-input")
                with Vertical():
                    yield Label("Toggle Switch")
                    yield Switch(id="demo-switch")

            # Progress section
            yield Static("Progress Bar", classes="section-title")
            with Vertical():
                yield ProgressBar(id="demo-progress", total=100)
                with Horizontal(classes="widget-row"):
                    yield Button(
                        "Start Progress", id="start-progress", variant="success"
                    )
                    yield Button(
                        "Reset Progress", id="reset-progress", variant="warning"
                    )

        yield Footer()

    def on_mount(self) -> None:
        """Start the progress animation when the screen is mounted."""
        self.progress_value = 0

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        button_id = event.button.id

        if button_id == "success-button":
            self.notify("Success notification!", severity="information")
        elif button_id == "warning-button":
            self.notify("Warning notification!", severity="warning")
        elif button_id == "error-button":
            self.notify("Error notification!", severity="error")
        elif button_id == "start-progress":
            self.run_worker(self.animate_progress())
        elif button_id == "reset-progress":
            self.progress_value = 0
            progress_bar = self.query_one("#demo-progress", ProgressBar)
            progress_bar.progress = 0

    def on_input_changed(self, event: Input.Changed) -> None:
        """Handle input changes."""
        if event.input.id == "demo-input" and event.value:
            self.notify(f"Input changed: {event.value}", severity="information")

    def on_switch_changed(self, event: Switch.Changed) -> None:
        """Handle switch toggle."""
        if event.switch.id == "demo-switch":
            state = "ON" if event.value else "OFF"
            self.notify(f"Switch turned {state}!", severity="information")

    async def animate_progress(self) -> None:
        """Animate the progress bar."""
        progress_bar = self.query_one("#demo-progress", ProgressBar)

        while self.progress_value < 100:
            await asyncio.sleep(0.05)
            self.progress_value += 1
            progress_bar.progress = self.progress_value

        self.notify("Progress complete!", severity="information")

    def watch_progress_value(self, value: int) -> None:
        """Watch for progress value changes."""
        if value == 100:
            self.notify("Progress reached 100%!", severity="success")
