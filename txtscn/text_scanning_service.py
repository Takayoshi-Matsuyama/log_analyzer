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

    def scan_files(self, root_path: str) -> None:
        """Scans all files under the given root path recursively.

        Args:
            root_path (str): The root path under which files are to be scanned.
        Returns:
            None
        """
        ...  # Should be implemented by concrete subclasses.
