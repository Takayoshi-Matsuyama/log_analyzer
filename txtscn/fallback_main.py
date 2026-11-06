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

from PySide6.QtWidgets import QApplication

from main_window import MainWindow
from interfaces import ILineScanner, IFileScanner, ITextScanningService
from text_scanning_service import TextScanningService
from default_tool_factory import DefaultToolFactory


def fallback_main():
    """fallback main is used when the primary main is not available."""
    print("Hello, World!")

    tool_factory = DefaultToolFactory()
    line_scanner: ILineScanner = tool_factory.create_line_scanner()
    file_scanner: IFileScanner = tool_factory.create_file_scanner()

    text_scanning_service: ITextScanningService = TextScanningService()
    text_scanning_service.register_file_scanner(file_scanner)
    text_scanning_service.register_line_scanner("default", line_scanner)

    app = QApplication(sys.argv)
    window = MainWindow(scanning_service=text_scanning_service)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    fallback_main()
