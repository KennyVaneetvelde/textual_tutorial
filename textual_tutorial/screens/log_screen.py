from pathlib import Path
import csv
from datetime import datetime

from textual.app import ComposeResult
from textual.screen import Screen
from textual.widgets import DataTable, Header, Footer
from textual.containers import Container
from rich.text import Text
from textual.widgets._data_table import DataTable as DataTableType  # for type hints


class LogScreen(Screen):
    """Screen displaying the log data in a sortable table."""

    BINDINGS = [
        ("escape", "app.pop_screen", "Back"),
        ("t", "sort_by_timestamp", "Sort by Time"),
        ("l", "sort_by_level", "Sort by Level"),
        ("m", "sort_by_message", "Sort by Message"),
        ("u", "sort_by_user", "Sort by User"),
    ]

    def __init__(self) -> None:
        super().__init__()
        # Track sort direction for each column
        self.sort_reverse = {
            "timestamp": False,
            "level": False,
            "message": False,
            "user": False,
        }

    def compose(self) -> ComposeResult:
        """Create child widgets for the screen."""
        yield Header(show_clock=True)
        yield Container(DataTable(id="log-table"), id="log-screen-container")
        yield Footer()

    def on_mount(self) -> None:
        """Load and display the log data when the screen is mounted."""
        table = self.query_one(DataTable)

        # Enable row selection
        table.cursor_type = "row"

        # Store column keys as class attributes for sorting
        self.columns = table.add_columns("Timestamp", "Level", "Message", "User ID")

        # Read and add data from CSV
        log_path = Path("logs/demo_log.csv")
        with open(log_path, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                # Parse timestamp for sorting
                timestamp = datetime.strptime(
                    row["timestamp"].strip('"'), "%Y-%m-%dT%H:%M:%SZ"
                )

                # Style the level column based on log level
                level_style = {"INFO": "green", "WARN": "yellow", "ERROR": "red"}.get(
                    row["level"].strip('"'), "white"
                )

                level = Text(row["level"].strip('"'), style=level_style)

                table.add_row(
                    timestamp.strftime("%Y-%m-%d %H:%M:%S"),
                    level,
                    row["message"].strip('"'),
                    row["user_id"].strip('"'),
                )

    def _sort_column(self, column_index: int, data_table: DataTableType) -> None:
        """Helper method to sort a column by index.

        Args:
            column_index: The index of the column to sort
            data_table: The DataTable widget to sort
        """
        column_keys = ["timestamp", "level", "message", "user"]
        key = column_keys[column_index]

        self.sort_reverse[key] = not self.sort_reverse[key]

        # Special handling for level column
        sort_key = lambda x: str(x) if column_index == 1 else str(x)

        data_table.sort(
            self.columns[column_index], key=sort_key, reverse=self.sort_reverse[key]
        )

    def on_data_table_header_selected(
        self, event: DataTableType.HeaderSelected
    ) -> None:
        """Handle column header clicks for sorting."""
        self._sort_column(event.column_index, event.data_table)

    def action_sort_by_timestamp(self) -> None:
        """Handle the 't' key press to sort by timestamp."""
        self._sort_column(0, self.query_one(DataTable))

    def action_sort_by_level(self) -> None:
        """Handle the 'l' key press to sort by level."""
        self._sort_column(1, self.query_one(DataTable))

    def action_sort_by_message(self) -> None:
        """Handle the 'm' key press to sort by message."""
        self._sort_column(2, self.query_one(DataTable))

    def action_sort_by_user(self) -> None:
        """Handle the 'u' key press to sort by user."""
        self._sort_column(3, self.query_one(DataTable))
