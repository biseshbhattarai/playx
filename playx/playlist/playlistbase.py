"""File to modify the playlists."""

from playx.logger import (
    Logger
)

from playx.stringutils import remove_duplicates


# Setup logger
logger = Logger('PlaylistBase')


class SongMetadataBase:
    """
    Base class to store song metadata.
    """

    def __init__(self):
        self.title = ''
        self.search_querry = ''
        self.URL = ''
        self.better_search_kw = [
                                # ' audio',
                                # ' lyrics',
                                # ' full'
                                ]

    def _add_better_search_words(self):
        """
        Add the keywords in better_search_kw list to get a better result.
        """
        for kw in self.better_search_kw:
            self.search_querry += kw

    def _remove_duplicates(self):
        """
        Remove duplicate words from the searchquerry.
        """
        self.search_querry = remove_duplicates(self.search_querry)


class PlaylistBase():
    """Strip the playlist according to the passed index."""

    def __init__(self, pl_start, pl_end):
        self.pl_start = pl_start
        self.pl_end = pl_end
        self.default_end = 0
        self.list_content_tuple = []

    def _is_valid(self, n):
        """
        Check if passed number is valid or not.
        """
        if n is not None:
            if n in range(1, self.default_end + 1):
                return True
            else:
                return False

    def strip_to_start_end(self):
        """Strip the tuple to positions passed by the user."""
        # Update the length of the playlist
        self.default_end = len(self.list_content_tuple)

        if self._is_valid(self.pl_start):
            self.default_start = self.pl_start

        if self._is_valid(self.pl_end):
            self.default_end = self.pl_end

        self.list_content_tuple = self.list_content_tuple[self.default_start - 1: self.default_end]
