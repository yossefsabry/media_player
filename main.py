## import main library
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPalette,
    QColor,
)
from PyQt5.QtWidgets import (
    QApplication,
)
from src.MediaPlayer import Window

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')

    # ------- Dark theme color settings --------------- #
    dark_palette = QPalette()
    dark_palette.setColor(QPalette.Window, QColor(16, 16, 16))
    dark_palette.setColor(QPalette.WindowText, Qt.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.white)
    dark_palette.setColor(QPalette.Text, Qt.white)
    dark_palette.setColor(QPalette.Button, QColor(65, 65, 65))
    dark_palette.setColor(QPalette.ButtonText, Qt.white)
    dark_palette.setColor(QPalette.BrightText, Qt.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.black)

    app.setPalette(dark_palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da;\
        border: 1px solid silver; }"
    )
    # ---- Create window object --------- #
    mp = Window()
    mp.show()
    sys.exit(app.exec_())

# starting run
if __name__ == '__main__':
    # ---- for Windows OS the preferred plugin to support media files -- #
    # os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    main()
