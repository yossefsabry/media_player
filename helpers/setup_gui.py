from PyQt5.QtWidgets import  QApplication
from PyQt5.QtCore import Qt
from PyQt5.QtGui import (
    QPalette,
    QColor,
)

def setup_gui(dark_palette: QPalette, app: QApplication):
    """
    description: function for setup the colors
    """
    app.setStyle('Fusion')
    # ------- Dark theme color settings --------------- #
    dark_palette.setColor(QPalette.Window, QColor(16, 16, 16))
    dark_palette.setColor(QPalette.WindowText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.Base, QColor(25, 25, 25))
    dark_palette.setColor(QPalette.AlternateBase, QColor(53, 53, 53))
    dark_palette.setColor(QPalette.ToolTipBase, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.ToolTipText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.Text, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.Button, QColor(65, 65, 65))
    dark_palette.setColor(QPalette.ButtonText, Qt.GlobalColor.white)
    dark_palette.setColor(QPalette.BrightText, Qt.GlobalColor.red)
    dark_palette.setColor(QPalette.Link, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.Highlight, QColor(42, 130, 218))
    dark_palette.setColor(QPalette.HighlightedText, Qt.GlobalColor.black)

    app.setPalette(dark_palette)
    app.setStyleSheet(
        "QToolTip { color: #ffffff; background-color: #2a82da;\
        border: 1px solid silver; }"
    )

