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
from PySide6.QtWidgets import QApplication  # noqa: E402

# Add the project root to sys.path to allow imports from the project
project_root = Path(__file__).resolve().parent.parent
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

from txtscn.interfaces import (  # noqa: E402, F401, F403
    IFileScanner,
    ILineScanner,
    IModeProvider,
    ITextScanningService,
    IToolFactory,
)
from txtscn.text_scanning_service import TextScanningService  # noqa: E402, F401, F403
from txtscn.main_window import MainWindow  # noqa: E402, F401, F403
from app.factory_provider import FactoryProvider  # noqa: E402, F401, F403


def setup_scanning_service() -> ITextScanningService:
    """Sets up and returns the text scanning service.

    Returns:
        ITextScanningService: Text scanning service with default scanners.
    """
    factory_provider: FactoryProvider = FactoryProvider()
    tool_factory: IToolFactory = factory_provider.create_tool_factory()
    mode_provider: IModeProvider = tool_factory.create_mode_provider()
    file_scanner: IFileScanner = tool_factory.create_file_scanner()
    line_scanner: ILineScanner = tool_factory.create_line_scanner()

    text_scanning_service: ITextScanningService = TextScanningService()
    text_scanning_service.register_mode_provider(mode_provider)
    text_scanning_service.register_file_scanner(file_scanner)
    text_scanning_service.register_line_scanner("custom", line_scanner)

    return text_scanning_service


def main():
    """Effective main entry point for the application."""

    text_scanning_service: ITextScanningService = setup_scanning_service()

    app = QApplication(sys.argv)
    window = MainWindow(scanning_service=text_scanning_service)
    window.show()

    sys.exit(app.exec())


# Entry point for main application
if __name__ == "__main__":
    main()
