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

import os
from pathlib import Path

from PySide6.QtCore import Signal

from interfaces import ITextScanningService, IFileScanner, ILineScanner


class TextScanningService(ITextScanningService):
    """Implementation of the text scanning service."""

    def __init__(self):
        """Initializes the text scanning service."""
        self._file_scanner = None
        self._line_scanners = dict()

    def register_file_scanner(self, scanner: IFileScanner) -> None:
        """Registers a file scanner.

        Args:
            scanner (IFileScanner): The file scanner to be registered.
        Returns:
            None
        """
        self._file_scanner = scanner

    def register_line_scanner(self, file_type: str, scanner: ILineScanner) -> None:
        """Registers a line scanner for the given file type.

        Args:
            file_type (str): The type of the file for which the line scanner is registered.
            scanner (ILineScanner): The line scanner to be registered.
        Returns:
            None
        """
        self._line_scanners[file_type] = scanner

    def scan_files(self, root_path: str, message_signal: Signal(str)) -> None:
        """Scans all files under the given root path recursively.

        Args:
            root_path (str): The root path under which files are to be scanned.
            message_signal (Signal(str)): The signal to emit messages during scanning.
        Returns:
            None
        """
        # Check if a file scanner is registered
        if self._file_scanner is None:
            raise ValueError("No file scanner registered.")

        # Check if the directory exists
        if not Path(root_path).exists():
            raise ValueError(f"Directory does not exist: {root_path}")
        if not Path(root_path).is_dir():
            raise ValueError(f"Path is not a directory: {root_path}")
        if not os.access(root_path, os.R_OK):
            raise ValueError(f"Directory is not readable: {root_path}")

        # Enumerate and scan files using the registered file scanner
        # os.walk() is used to recursively enumerate files under the root path.
        for dirpath, _, filenames in os.walk(root_path):
            for filename in filenames:
                file_path = os.path.join(dirpath, filename)
                print(f"Scanning file: {file_path}")
                message_signal.emit(f"Scanning file: {file_path}")
                self._file_scanner.filter_file(file_path)
