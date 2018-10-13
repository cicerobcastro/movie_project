import fresh_tomatoes
import media

toy_story = media.Movie("Toy Story 3",
                        "A story of a boy and his toys that come to life",
                        "http://www.gstatic.com/tv/thumb/v22vodart/3546307/p3546307_v_v8_ab.jpg",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://www.gstatic.com/tv/thumb/v22vodart/3542039/p3542039_v_v8_ac.jpg",
                     "https://youtu.be/5PSNL1qE6VY")

rocky = media.Movie("Rocky",
                    "A small-time boxer gets a supremely rare chance to fight a heavy-weight champion.",
                    "https://3.bp.blogspot.com/-3lA9VsAPdRg/WZS_C5UG10I/AAAAAAAAAwk/rPok-7py374li-N172pC4K-xFuDgcaM9ACLcBGAs/s1600/Rocky%2Bposter.jpg",
                    "https://youtu.be/8tab8fK2_3w")

forrest_gump = media.Movie("Forrest Gump",
                           "Forrest Gump is a 1994 American romantic comedy-drama film based on the 1986 novel of the same name by Winston Groom. ",
                           "http://www.gstatic.com/tv/thumb/v22vodart/15829/p15829_v_v8_ab.jpg",
                           "https://youtu.be/bLvqoHBptjg")

breaking_bad = media.Serie("Breaking Bad",
                           "Season 5",
                           "Mild-mannered high school chemistry teacher Walter White thinks his life can't get much worse.",
                           "http://www.gstatic.com/tv/thumb/tvbanners/9181462/p9181462_b_v8_aa.jpg",
                           "https://www.youtube.com/watch?v=HhesaQXLuRY")

game_of_thrones = media.Serie("Game of Thrones",
                              "Season 7",
                              " It's the depiction of two powerful families - kings and queens, knights and renegades, liars and honest men - playing a deadly game for control of the Seven Kingdoms of Westeros, and to sit atop the Iron Throne.",
                              "http://www.gstatic.com/tv/thumb/tvbanners/14160794/p14160794_b_v8_aa.jpg",
                              "https://www.youtube.com/watch?v=giYeaKsXnsI")


movies = [toy_story, avatar, rocky, forrest_gump, breaking_bad, game_of_thrones]
fresh_tomatoes.open_movies_page(movies)
