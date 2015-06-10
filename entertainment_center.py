import media
import fresh_tomatoes

#=====================================================================
#  Create move data base


#---------------------------------------------------
# Define fields of the element of movies_data array

MDATA_TITLE_IDX = 0 
MDATA_BOXART_IDX = 1
MDATA_YOUTUBEID_IDX = 2
MDATA_RATING_IDX = 3

#-------------------------------------------------
# Format of each element of the movie_data array :
#
#     [name, box_art_url, you_tube_id ]         
#
movies_data = [
    [ "Avatar", 
      "http://upload.wikimedia.org/wikipedia/en/b/b0/" 
          "Avatar-Teaser-Poster.jpg",
      "5PSNL1qE6VY",
      "7.9",
      "James Cameron",
    ],
    [ "Toy Story",   
      "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
      "KYz2wyBy3kc", 
      "8.3",
      "John Laseter",
    ],
    [ "Inception",
      "http://upload.wikimedia.org/wikipedia/en/7/7f/Inception_ver3.jpg",
      "8hP9D6kZseM",
      "8.8",
      "Christopher Nolan",
    ],
    [ "Interstellar",
      "http://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
      "zSWdZVtXT7E",
      "8.7",
      "Christopher Nolan",
    ],
    [ "Avengers",
      "http://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg",
      "eOrNdBpGMv8",
      "8.2",
      "Joss Whedon",
    ],
    [ "Iron Man",
      "http://upload.wikimedia.org/wikipedia/en/7/70/Ironmanposter.JPG",
      "XWWd6p2JHKo",
      "7.9",
      "Jon Favreau",
    ],
    [ "Shrek",
      "http://upload.wikimedia.org/wikipedia/en/3/39/Shrek.jpg",
      "W37DlG1i61s",
      "7.9",
      "Andrew Adamson, Vicky Jenson",
    ],
    [ "Guardians of the Galaxy",
      "http://upload.wikimedia.org/wikipedia/en/8/8f/GOTG-poster.jpg",
      "d96cjJhvlMA",
      "8.1",
      "James Gunn",
    ],
    [ "X-Men",
      "http://upload.wikimedia.org/wikipedia/en/8/8c/XMen1poster.jpg",
      "nbNcULQFojc",
      "7.4",
      "Bryan Singer",
    ],
]

#=====================================================================
# Create Movie object for each of the entries in movies_data
# (processed in alphabetical order based on the title) and 
# then append it to the movie_objects array.

movie_objects = []
for movie in sorted(movies_data, key=lambda movie: movie[MDATA_TITLE_IDX]):
    movie[MDATA_YOUTUBEID_IDX] = "https://www.youtube.com/watch?v=" + \
                                  movie[MDATA_YOUTUBEID_IDX] 
    movie_objects.append(media.Movie(*movie))

#=====================================================================
# Let fresh_tomatoes.open_movies_page do the rest of the magic

fresh_tomatoes.open_movies_page(movie_objects)

