
from PyQt5.QtCore import Qt, QAbstractListModel

class PlaylistModel(QAbstractListModel):
    def __init__(self, playlist, *args, **kwargs):
        super(PlaylistModel, self).__init__(*args, **kwargs)
        self.playlist = playlist

    def data(self, index, role):
        if role == Qt.DisplayRole: # return info about the song that display
            media = self.playlist.media(index.row())
            return media.canonicalUrl().fileName()

    def rowCount(self, index): # return count for song in playlist
        return self.playlist.mediaCount()
