import webbrowser

class Movie():
    """This class represents a general movie with certain attributes.

    Attributes:
        title: A string representing the movie's title
        storyline: A string representing the movie's storyline
        poster_image_url: An string of the movie's poster image url
        trailer_youtube_url: A string of the movie's youtube trailer url
        release_date: A string of the movie's release date
        rating: A string of the movie's MPAA rating
    """
        
    def __init__(self, movie_title, story,
                 poster, trailer_yt, theater_date, movie_rating):
        """Inits Movie instance with certain arguments

        Args:
            movie_title: A string of the instance's title
            story: A string of the instance's storyline
            poster: A string of the instance's poster image url
            trailer_yt: A string of the instance's youtube trailer
            theater_date: A string of the instance's release date
            movie_rating: A string of the instance's MPAA rating
                        
        """        
        self.title = movie_title
        self.storyline = story
        self.poster_image_url = poster
        self.trailer_youtube_url = trailer_yt
        self.release_date = theater_date
        self.rating = movie_rating

    def show_trailer(self):
        """Opens a movie's youtube trailer url in a webbrowser"""
        webbrowser.open(self.trailer_youtube_url)
