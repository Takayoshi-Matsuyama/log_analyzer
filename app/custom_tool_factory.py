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

from txtscn.interfaces import IToolFactory, IModeProvider, IFileScanner, ILineScanner

from app.custom_mode_provider import CustomModeProvider
from app.custom_file_scanner import CustomFileScanner
from app.custom_line_scanner import CustomLineScanner


class CustomToolFactory(IToolFactory):
    """Represents a custom tool factory implementation."""

    def create_mode_provider(self) -> IModeProvider:
        """Creates and returns a custom mode provider."""
        return CustomModeProvider()

    def create_file_scanner(self) -> IFileScanner:
        """Creates and returns a custom file scanner."""
        return CustomFileScanner()

    def create_line_scanner(self) -> ILineScanner:
        """Creates and returns a custom line scanner."""
        return CustomLineScanner()
