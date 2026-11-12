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

from txtscn.interfaces import IModeProvider


class CustomModeProvider(IModeProvider):
    """Represents a custom mode provider."""

    def get_mode(self) -> str:
        """Returns the custom scanning mode.

        Returns:
            str: The custom scanning mode.
        """
        return "custom_mode"
