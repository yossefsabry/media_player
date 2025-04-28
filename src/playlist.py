
# from PyQt5.QtCore import Qt, QAbstractListModel
from PyQt6.QtCore import QModelIndex
from PyQt6.QtCore import Qt, QAbstractListModel
from PyQt5.QtCore import QAbstractListModel  # or PySide2/Qt6 equivalent



class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    # return information about current song in playlist
    def data(self, index: QModelIndex, role: int=Qt.ItemDataRole.DisplayRole):
        if role == Qt.ItemDataRole.DisplayRole: # return info about the song that display
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()
        return None

    # return count for song in playlist
    def rowCount(self, parent:QModelIndex = QModelIndex()) -> int: 
        return self.playlist.mediaCount()
