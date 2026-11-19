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

import sys
from pathlib import Path

# Add the project root to sys.path to allow imports from the project
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from txtscn.interfaces import IToolFactory, IModeProvider  # noqa: E402, F401, F403
from txtscn.interfaces import ITextScanningService  # noqa: E402, F401, F403

from app.factory_provider import FactoryProvider


def setup_scanning_service() -> ITextScanningService:
    """Sets up and returns the text scanning service.

    Returns:
        ITextScanningService: Text scanning service with default scanners.
    """
    factory_provider: FactoryProvider = FactoryProvider()
    tool_factory: IToolFactory = factory_provider.create_tool_factory()
    mode_provider: IModeProvider = tool_factory.create_mode_provider()
    ...


def main():
    print("Hello, World!")
    import os

    print(os.getcwd())

    setup_scanning_service()


if __name__ == "__main__":
    main()
