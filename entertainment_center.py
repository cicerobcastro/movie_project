import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/WqGqrq",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/L4Bmbe",
                     "https://youtu.be/5PSNL1qE6VY")

rocky = media.Movie("Rocky",
                    "A small-time boxer gets a supremely rare chance to fight a heavy-weight champion.",
                    "https://goo.gl/kASTCy",
                    "https://youtu.be/8tab8fK2_3w")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump is a 1994 American romantic comedy-drama film based on the 1986.",
                           "https://goo.gl/EY3Awz",
                           "https://youtu.be/bLvqoHBptjg")

breaking_bad = media.Serie("Breaking Bad",
                           "Season 5",
                           "Mild-mannered high school chemistry teacher Walter White thinks his life can't get much worse.",
                           "https://goo.gl/pUYWrz",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")

game_of_thrones = media.Serie("Game of Thrones",
                              "Season 7",
                              "It's the depiction of two powerful families - kings and queens, knights and renegades, liars and honest men.",
                              "https://goo.gl/1i8QL3",
                              "https://www.youtube.com/watch?v=giYeaKsXnsI")


movies = [toy_story, avatar, rocky,
          forrest_gump, breaking_bad, game_of_thrones]
fresh_tomatoes.open_movies_page(movies)
