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
    def scan_line(self, line: str, mode: str) -> str:
        """Scans the given line and returns the report as a string.

        Args:
            line (str): The line to be scanned.
            mode (str): The scanning mode to be used.
        Returns:
            str: The report string.
        """
        ...  # Should be implemented by concrete subclasses.


class IFileScanner(ABC):
    """Provides an interface for file scanning."""

    @abstractmethod
    def filter_file(self, file_path_name: str, mode: str) -> tuple[bool, str]:
        """Filters the given file and returns a tuple (is_scanning_target, file_type).

        Args:
            file_path_name (str): The path and name of the file to be filtered.
            mode (str): The scanning mode to be used.
        Returns:
            tuple[bool, str]: scanning target indicator and the file type.
        """
        ...  # Should be implemented by concrete subclasses.


class IToolFactory(ABC):
    """Provides an interface for the tool factory."""

    @abstractmethod
    def create_line_scanner(self) -> ILineScanner:
        """Creates and returns a line scanner."""
        ...  # Should be implemented by concrete subclasses.

    @abstractmethod
    def create_file_scanner(self) -> IFileScanner:
        """Creates and returns a file scanner."""
        ...  # Should be implemented by concrete subclasses.


class IModeProvider(ABC):
    """Provides an interface for mode providers."""

    @abstractmethod
    def get_mode_list(self) -> list[str]:
        """Returns the list of available modes."""
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
    def scan_files(self, root_path: str, mode: str) -> None:
        """Scans all files under the given root path recursively using the specified mode.

        Args:
            root_path (str): The root path under which files are to be scanned.
            mode (str): The scanning mode to be used.
        Returns:
            None
        """
        ...  # Should be implemented by concrete subclasses.
