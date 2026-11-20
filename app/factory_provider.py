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

import json

from txtscn.default_tool_factory import DefaultToolFactory
from txtscn.interfaces import IToolFactory
from app.custom_tool_factory import CustomToolFactory


class FactoryProvider:
    """Provides factory methods for creating instances of various components."""

    @staticmethod
    def create_tool_factory() -> IToolFactory:
        """Gets the tool factory instance.

        Returns:
            IToolFactory: The tool factory instance.
        """
        ...
        # Load the tool factory setting from the configuration file
        with open("app/setting.json", "r") as f:
            settings = json.load(f)
        tool_factory_type = settings.get("ToolFactory", "default")

        # Create the appropriate tool factory instance based on the setting
        if tool_factory_type == "default":
            return DefaultToolFactory()
        elif tool_factory_type == "custom":
            return CustomToolFactory()
        else:
            raise ValueError(f"Unknown tool factory type: {tool_factory_type}")
