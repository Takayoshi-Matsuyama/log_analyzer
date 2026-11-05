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

from PySide6.QtWidgets import (
    QFileDialog,
    QHBoxLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QStatusBar,
    QVBoxLayout,
    QWidget,
)

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

        # --- Line Edit (Directory Path) ---
        self.directory_path_line_edit = QLineEdit(self)
        self.directory_path_line_edit.setPlaceholderText(
            "Select a root directory to scan"
        )
        self.directory_path_line_edit.setReadOnly(True)

        # --- Button (Select Directory) ---
        select_directory_button = QPushButton("Select Directory")
        select_directory_button.clicked.connect(self.on_select_directory_button_clicked)

        # --- Button (Start Scan) ---
        start_scan_button = QPushButton("Start Scan")
        start_scan_button.clicked.connect(self.on_start_scan_button_clicked)

        # --- Layout ---
        hbox_layout = QHBoxLayout()
        hbox_widget = QWidget()
        hbox_widget.setLayout(hbox_layout)
        hbox_layout.addWidget(self.directory_path_line_edit)
        hbox_layout.addWidget(select_directory_button)

        vbox_layout = QVBoxLayout()
        vbox_widget = QWidget()
        vbox_widget.setLayout(vbox_layout)
        vbox_layout.addWidget(hbox_widget)
        vbox_layout.addWidget(start_scan_button)

        self.setCentralWidget(vbox_widget)

    def on_select_directory_button_clicked(self):
        """Handles the select directory button click event."""
        print("Select Directory button clicked!")

        # --- Select the root directory to scan.---
        directory_name = QFileDialog.getExistingDirectory(self, "Select Directory", "")
        print(f"Selected folder: {directory_name}")
        if directory_name:
            self.directory_path_line_edit.setText(directory_name)

    def on_start_scan_button_clicked(self):
        """Handles the start scan button click event."""
        print("Start Scan button clicked!")
        directory_path = self.directory_path_line_edit.text()
        if not directory_path:
            print("No directory selected!")
            return
        self.scanning_service.scan_files(directory_path)
