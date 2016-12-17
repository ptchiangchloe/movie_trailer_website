import media
import fresh_tomatoes

manchester_by_the_sea = media.Movie("Manchester by the Sea ",
                        "An uncle is forced to take care of his teenage nephew\
                         after the boy's father dies.",
                        "http://t3.gstatic.com/images?q=tbn:ANd9GcS5-FlTo1iYdLeCeTN09lbE6seUjxO1jksMN8y5dpz3vJdRgFig",
                        "https://www.youtube.com/watch?v=gsVoD0pTge0",
                        "http://statcdn.fandango.com/MPX/image/NBCU_Fandango/453/671/ManchesterbytheSea_Trailer.jpg")


the_danish_girl = media.Movie("The Danish Girl",
                                "A fictitious love story loosely inspired by the lives of \
                                Danish artists Lili Elbe and Gerda Wegener.\
                                Lili and Gerda's marriage and work evolve as they navigate\
                                 Lili's groundbreaking journey as a transgender pioneer.",
                                "https://images-na.ssl-images-amazon.com/images/M/MV5BMjA0NjA4NjE2Nl5BMl5BanBnXkFtZTgwNzIxNTY2NjE@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=d88APYIGkjk",
                                "https://i.ytimg.com/vi/sCPgKTvx3RI/maxresdefault.jpg")

memoirs_of_a_geisha = media.Movie("Memoirs of a Geisha",
                                  "the story of a young Japanese girl, Chiyo\
                                   Sakamoto...",
                                  "http://www.impawards.com/2005/posters/memoirs_of_a_geisha.jpg",
                                  "https://www.youtube.com/watch?v=i_TXEEgNiWE",
                                  "http://hdwallpaperexpert.com/wp-content/uploads/2015/02/Memoirs-Of-A-Geisha-Wallpaper-Hd.jpg"
                                  )

chloe = media.Movie("Chloe",
                    "A doctor hires an escort to seduce her husband, whom she\
                     suspects of cheating, \
                    though unforeseen events put the family in danger.",
                    "https://images-na.ssl-images-amazon.com/images/M/MV5BMTczMzExNTkyMV5BMl5BanBnXkFtZTcwODUyMzAyMw@@._V1_SY1000_CR0,0,690,1000_AL_.jpg",
                    "https://www.youtube.com/watch?v=a13PqQq4fv0",
                    "http://mafab.hu/static/2014t/285/10/35496_39.jpg")

a_single_man = media.Movie("A Single Man",
                           "An English professor, one year after the sudden \
                           death of his boyfriend, is unable to cope with his \
                           typical days in 1960s Los Angeles.",
                           "https://images-na.ssl-images-amazon.com/images/M/MV5BMzU5MTk4MjQ2M15BMl5BanBnXkFtZTcwNDU0MzEwMw@@._V1_SY1000_CR0,0,674,1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=sC9Zm1UJ7zs",
                           "https://fergalcasey.files.wordpress.com/2010/02/single-man-colin-firth-2.jpg")

notes_on_a_scandal = media.Movie("Notes on a Scandal",
                                 "A veteran high school teacher befriends a \
                                 younger art teacher, who is having an\
                                  affair with one of her 15-year-old students. \
                                  However, her intentions with this new\
                                   'friend' also go well beyond platonic \
                                   friendship.",
                                 "https://images-na.ssl-images-amazon.com/images/M/MV5BMTI2NTcyMjE3NF5BMl5BanBnXkFtZTcwNDAyNzkzMQ@@._V1_.jpg",
                                 "https://www.youtube.com/watch?v=AruRpjQquQQ",
                                 "http://www.vhcorner.com/wp-content/uploads/notesonascandal_gospeloak.jpg")
# Add each movie to the list
movies = [manchester_by_the_sea, the_danish_girl, memoirs_of_a_geisha, chloe, a_single_man, notes_on_a_scandal]

fresh_tomatoes.create_movie_tiles_content(movies)

# Call open movies
fresh_tomatoes.open_movies_page(movies)
