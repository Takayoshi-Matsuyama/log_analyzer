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

from interfaces import IFileScanner, ILineScanner, IToolFactory
from default_file_scanner import DefaultFileScanner
from default_line_scanner import DefaultLineScanner


class DefaultToolFactory(IToolFactory):
    """Factory class for creating default tools."""

    @staticmethod
    def create_file_scanner() -> IFileScanner:
        """Creates a default file scanner.

        Returns:
            IFileScanner: An instance of the default file scanner.
        """
        return DefaultFileScanner()

    @staticmethod
    def create_line_scanner() -> ILineScanner:
        """Creates a default line scanner.

        Returns:
            ILineScanner: An instance of the default line scanner.
        """
        return DefaultLineScanner()
