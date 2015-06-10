class Movie(object):
    """ This class stores information about a movie """

    def __init__(self, title,  poster_image, trailer_youtube, 
                 rating, director):
        self.title               = title
        self.poster_image_url    = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.rating              = rating
        self.director            = director

