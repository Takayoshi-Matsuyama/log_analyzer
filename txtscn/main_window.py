# Copyright 2026 Takayoshi Matsuyama
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from PySide6.QtWidgets import QFileDialog, QMainWindow, QPushButton, QStatusBar

from interfaces import ITextScanningService


class MainWindow(QMainWindow):
    """Represents the main window of the application."""

    def __init__(self, scanning_service: ITextScanningService):
        """Initializes the main window.

        Args:
            scanning_service (ITextScanningService): The scanning service to be used by the main window.
        """
        super().__init__()
        self.scanning_service = scanning_service
        self.setWindowTitle("Log Analyzer")
        self.resize(800, 600)

        # --- Status Bar ---
        status_bar = QStatusBar(self)
        status_bar.showMessage("Ready")
        self.setStatusBar(status_bar)

        # --- Button ---
        button = QPushButton("Click Me")
        button.clicked.connect(self.on_button_clicked)
        self.setCentralWidget(button)

    def on_button_clicked(self):
        """Handles the button click event."""
        print("Button clicked!")

        # --- Select the root directory to scan.---
        directory_name = QFileDialog.getExistingDirectory(self, "Select Directory", "")
        print(f"Selected folder: {directory_name}")
