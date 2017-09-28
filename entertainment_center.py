# IMPORT NECESSARY MODULES
import fresh_tomatoes
import media

# INSTANTIATE MOVIE INSTANCES
DEADPOOL = media.Movie("Deadpool",
                       "A story of a boy and his toys",
                       "http://assets1.ignimgs.com/2016/01/14/deadpoolver10xxlgjpg-0d72a2_1280w.jpg",
                       "https://www.youtube.com/watch?v=CnLGJHtdH1w")

GUARDIANS = media.Movie("Guardians of the Galaxy",
                        "A story of a boy and his space toys",
                        "http://www.fatmovieguy.com/wp-content/uploads/2014/06/Guardians-of-the-Galaxy-Rocket-and-Groot-Movie-Poster.jpg",
                        "https://www.youtube.com/watch?v=d96cjJhvlMA")

TOMBSTONE = media.Movie("Tombstone",
                        "Best Skate Movie",
                        "https://images-na.ssl-images-amazon.com/images/I/51UdG6rzHkL.jpg",
                        "https://www.youtube.com/watch?v=XTWYKf5hXIg")

BAKER = media.Movie("Baker Skate Movie",
                    "A battle the west will never forget",
                    "http://skately.com/img/library/videos/large/baker-skateboards-baker-3.jpg",
                    "https://www.youtube.com/watch?v=hZ7H8HXnhKQ")

DEADPOOL_TWO = media.Movie("Deadpool 2",
                           "Deadpool is back",
                           "https://pre00.deviantart.net/852c/th/pre/f/2017/069/4/3/deadpool_2_movie_poster_by_prkrdesigns-db1tw95.jpg",
                           "https://www.youtube.com/watch?v=Kc9zDkn3A-M")

ANCHORMAN = media.Movie("Anchor Man",
                        "Best News Casters Around",
                        "https://images-na.ssl-images-amazon.com/images/M/MV5BMTQ2MzYwMzk5Ml5BMl5BanBnXkFtZTcwOTI4NzUyMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=-T3wnP91OnI")

MOVIES = [DEADPOOL, GUARDIANS, TOMBSTONE, BAKER, DEADPOOL_TWO, ANCHORMAN]
fresh_tomatoes.open_movies_page(MOVIES)
