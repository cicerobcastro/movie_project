import fresh_tomatoes
import media

"""
Here is the JSON with data of movies and serie
title(title of movie)
storyline(description of movie)
poster_image_url(url poster of movie)
trailer_youtube_url(url of youtube)
"""
toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "https://goo.gl/WqGqrq",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://goo.gl/L4Bmbe",
                     "https://youtu.be/5PSNL1qE6VY")

rocky = media.Movie("Rocky",
                    "A supremely rare chance to fight a heavy-weight.",
                    "https://goo.gl/kASTCy",
                    "https://youtu.be/8tab8fK2_3w")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump is a American romantic comedy-drama.",
                           "https://goo.gl/EY3Awz",
                           "https://youtu.be/bLvqoHBptjg")

breaking_bad = media.Serie("Breaking Bad",
                           "Season 5",
                           "Teacher who becomes a drug dealer",
                           "https://goo.gl/pUYWrz",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")

game_of_thrones = media.Serie("Game of Thrones",
                              "Season 7",
                              "It's the depiction of two powerful families.",
                              "https://goo.gl/1i8QL3",
                              "https://www.youtube.com/watch?v=giYeaKsXnsI")

# Here we put informations in a array and call fresh_tomatoes
movies = [toy_story, avatar, rocky,
          forrest_gump, breaking_bad, game_of_thrones]
# Open browser with movie page
fresh_tomatoes.open_movies_page(movies)
