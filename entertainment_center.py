import fresh_tomatoes
import media

# Six Movie class instances with unique values for the common attributes
# Each line corresponds to a different attribute

titanic = media.Movie("Titanic",
          ("A love story between a pauper and a rich lady while on the biggest "
          "ship in the world."),
          "http://ia.media-imdb.com/images/M/MV5BMjExNzM0NDM0N15BMl5BanBnXkFtZTcwMzkxOTUwNw@@._V1_SX640_SY720_.jpg",
          "https://www.youtube.com/watch?v=zCy5WQ9S4c0",
          "1997",
          "PG-13")

home_alone = media.Movie("Home Alone",
          ("The youngest member of the McCallister family battles a group of "
          "robbers while home alone."),
          "http://ia.media-imdb.com/images/M/MV5BMTUzMzg4MTg2M15BMl5BanBnXkFtZTYwNDM4OTk4._V1_SX640_SY720_.jpg",
          "https://www.youtube.com/watch?v=CK2Btk6Ybm0",
          "1990",
          "PG-13")

monsters_inc = media.Movie("Monsters Inc.",
          ("A little girl enters the world of monsters where monsters scare "
          "children to fuel their world."),
          "http://ia.media-imdb.com/images/M/MV5BMTY1NTI0ODUyOF5BMl5BanBnXkFtZTgwNTEyNjQ0MDE@._V1_SX640_SY720_.jpg",
          "https://www.youtube.com/watch?v=8IBNZ6O2kMk",
          "2001",
          "G")

matilda = media.Movie("Matilda",
          ("A genius little girl battles with the crazy headmistress of her new "
          "school with her special powers."),
          "http://ia.media-imdb.com/images/M/MV5BNTYxNDEyMDQ1MF5BMl5BanBnXkFtZTcwODcxMDYyMQ@@._V1_SY317_CR6,0,214,317_AL_.jpg",
          "https://www.youtube.com/watch?v=MdC_YMvYZyI",
          "1996",
          "PG")

jurassic_park = media.Movie("Jurassic Park",
          ("A group of scientists discover Jurassic Park, an island where "
          "dinosaurs live, but all havoc wrecks loose."),
          "http://ia.media-imdb.com/images/M/MV5BMjM2MDgxMDg0Nl5BMl5BanBnXkFtZTgwNTM2OTM5NDE@._V1_SX214_AL_.jpg",
          "https://www.youtube.com/watch?v=QWBKEmWWL38",
          "1993",
          "PG-13")

fellowship_of_the_ring = media.Movie("Fellowship of the Ring",
          ("A group of hobbits, a wizard, men, an elf, and a dwarf embark "
          "upon a quest to destroy the one ring."),
          "http://ia.media-imdb.com/images/M/MV5BNTEyMjAwMDU1OV5BMl5BanBnXkFtZTcwNDQyNTkxMw@@._V1_SX640_SY720_.jpg",
          "https://www.youtube.com/watch?v=V75dMMIW2B4",
          "2001",
          "PG-13")

# Movies data structure which stores a list of Movie class instances from above
# List includes: titanic, home_alone, monsters_inc, matilda, jurassic_park, and
# fellowship_of_the_ring

movies = [titanic, home_alone, monsters_inc,
          matilda, jurassic_park, fellowship_of_the_ring]

# Passes movies list to open_movies_page method and calls it
# The open_movies_page method is defined in fresh_tomatoes.py

fresh_tomatoes.open_movies_page(movies)
