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

from interfaces import IFileScanner


class DefaultFileScanner(IFileScanner):
    """Represents the default file scanner implementation."""

    def filter_file(self, file_path_name: str, mode: str) -> tuple[bool, str]:
        """Filters a file.

        Args:
            file_path_name (str): The path and name of the file to be filtered.
            mode (str): The scanning mode to be used.
        Returns:
            tuple[bool, str]: scanning target indicator and the file type.
        """

        # Implement the default file filtering logic here
        return True, "default"
