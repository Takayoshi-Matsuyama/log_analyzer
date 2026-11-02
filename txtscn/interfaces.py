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

from __future__ import annotations
from abc import ABC, abstractmethod


class ILineScanner(ABC):
    """Provides an interface for line scanning."""

    @abstractmethod
    def scan_line(self, line: str) -> str:
        """Scans the given line and returns the report as a string.

        Args:
            line (str): The line to be scanned.
        Returns:
            str: The report string.
        """
        ...  # Should be implemented by concrete subclasses.


class IFileScanner(ABC):
    """Provides an interface for file scanning."""

    @abstractmethod
    def filter_file(self, file_path_name: str) -> tuple[bool, str]:
        """Filters the given file and returns a tuple (is_scanning_target, file_type).

        Args:
            file_path_name (str): The path and name of the file to be filtered.
        Returns:
            tuple[bool, str]: scanning target indicator and the file type.
        """
        ...  # Should be implemented by concrete subclasses.


class ITextScanningService(ABC):
    """Provides an interface for the text scanning service."""

    @abstractmethod
    def register_file_scanner(self, scanner: IFileScanner) -> None:
        """Registers a file scanner.

        Args:
            scanner (IFileScanner): The file scanner to be registered.
        Returns:
            None
        """
        ...  # Should be implemented by concrete subclasses.

    @abstractmethod
    def register_line_scanner(self, file_type: str, scanner: ILineScanner) -> None:
        """Registers a line scanner for the given file type.

        Args:
            file_type (str): The type of the file for which the line scanner is registered.
            scanner (ILineScanner): The line scanner to be registered.
        Returns:
            None
        """
        ...  # Should be implemented by concrete subclasses.

    @abstractmethod
    def scan_files(self, root_path: str) -> None:
        """Scans all files under the given root path recursively.

        Args:
            root_path (str): The root path under which files are to be scanned.
        Returns:
            None
        """
        ...  # Should be implemented by concrete subclasses.
