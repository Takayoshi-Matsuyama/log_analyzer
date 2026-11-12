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

from interfaces import IModeProvider


class DefaultModeProvider(IModeProvider):
    """Represents the default mode provider."""

    def get_mode(self) -> str:
        """Returns the default scanning mode.

        Returns:
            str: The default scanning mode.
        """
        return "default_mode"
