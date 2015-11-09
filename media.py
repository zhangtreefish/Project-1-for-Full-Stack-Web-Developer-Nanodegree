class Movie():
    """
    create a class for creating movie objects in entertainment.py
    """
    def __init__(self, movie_title, movie_storyline, movie_poster,
                 movie_trailer):
        """
        this is the constructor of the class
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
