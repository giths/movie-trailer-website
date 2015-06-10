
This application generates and displays a webpage that includes a set
of movies using their box art images.  When an image is clicked, it's
trailer is played.


Contents

  1) Quick start

  2) Files and their description


1) Quick Start

   a) Download this application.

   b) If not already installed, download and install Python 2.x (e.g. 2.7).

   c) Run the following in the directory where the application is downloaded :

         python entertainment_center.py

   d) This should open a web browser displaying the movie tiles.

   e) When mouse is hover over the movie tile, the director
      information is displayed.

   f) When an image is clicked, the trailer for the movie will be played.


2) Files and their description

2.1) entertainment.py

     The main program file is 'entertainment_center.py'. It contains
     the data for all the movies to be displayed. A new movie can be
     added by adding an entry to the movies_data array. See the
     comment at the beginning of this array definition for the format
     details.

     The movies are sorted by title before displaying.

     It uses Movie class defined in 'media.py' and html generating
     routines in 'fresh_tomatoes.py'.

2.2) media.py

     The Movie class is defined in this file.

2.3) fresh_tomatoes.py

     This file contains html generation code.


