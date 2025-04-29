## import main library
import sys
from PyQt5.QtGui import QPalette 
from PyQt5.QtWidgets import  QApplication
from src.MediaPlayer import Window
from helpers.setup_gui import setup_gui
import os

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
    # os.environ['QT_LOGGING_RULES'] = 'qt.multimedia.*=false'
    # os.environ["QT_MEDIA_AUDIO_BACKEND"] = "alsa"  # Bypass PulseAudio/LADSPA
    # os.environ["PIPEWIRE_RUNTIME_DIR"] = "/tmp"  # Workaround for some issues
    # os.environ["GST_PIPEWIRE"] = "1"  # Force GStreamer to use PipeWire
    # os.environ["QT_MEDIA_BACKEND"] = "gstreamer"  # Ensure Qt uses GStreamer
    main()
