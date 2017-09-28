# IMPORT WEBBROWSER PKG
import webbrowser


class Movie():
    """This class provides a way to store movie related information"""

    def __init__(self, movie_title, movie_storyline, poster_image, youtube_url):
        """This Constructor builds each instance of the Movie Class"""
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_url

    def show_trailer(self):
        """This Method opens teh youtube url in the Modal window"""
        webbrowser.open(self.trailer_youtube_url)
