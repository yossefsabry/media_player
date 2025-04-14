## import main library
import sys
from PyQt5.QtGui import QPalette 
from PyQt5.QtWidgets import  QApplication
from src.MediaPlayer import Window
from helpers.setup_gui import setup_gui

def main():
    app = QApplication(sys.argv)
    dark_palette = QPalette()

    # setup the application gui colors
    setup_gui(dark_palette, app)

    # create a window class
    mp = Window()
    mp.show()
    sys.exit(app.exec_()) # exit app

# starting run
if __name__ == '__main__':
    # for windows OS the preferred plugin to support media files
    # os.environ['QT_MULTIMEDIA_PREFERRED_PLUGINS'] = 'windowsmediafoundation'
    main()
