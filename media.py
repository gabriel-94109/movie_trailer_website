class Movie():
    """ This class provides a way to store movie related information """

    def __init__(self, title, storyline,
                 poster_image_url, trailer_youtube_url):
        """
        Args:
            title (str): movie title
            storyline (str): summary of movie plot
            poster_image_url (str): link to image to display
            trailer_youtube_url (str): link to youtube video

        """
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def __str__(self):
        return self.movie_title
