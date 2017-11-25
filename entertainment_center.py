import media
import fresh_tomatoes

"""
This code takes a list of movie data, creates Movie objects, and passes them
to fresh_tomatoes, which generates an html page and launches in browser.
"""

movie_data = [
    [
        "Quadrophenia",
        "An angst-ridden London youth joins a gang.",
        ("http://t1.gstatic.com/images?q="
         "tbn:ANd9GcTHhnevWFllxVrdJmj3orkVVXXpxt5LTcpVWu0_UL3OaERJi8lk"),
        "https://www.youtube.com/watch?v=Xwp5Fu2KZsc",
    ],
    [
        "The Dressmaker",
        "A dressmaker returns to her small Australian town to seek revenge.",
        ("http://t1.gstatic.com/images?q="
         "tbn:ANd9GcQ_O0kRLm-KTUqvCwB5dO9_TCn0sqLdI8wZ8F_tAThD_n0GNmzb"),
        "https://www.youtube.com/watch?v=DMEu-1CIB_I",
    ],
    [
        "The Grand Budapest Hotel",
        "The adventures of legendary concierge Gustave H. and Zero Moustafa.",
        ("http://t0.gstatic.com/images?q="
         "tbn:ANd9GcSDDmHpt0TcHkK9DCv0QU-Xx4WNEVOJnHlj7pVfN61-1mEX2eCG"),
        "https://www.youtube.com/watch?v=1Fg5iWmQjwk",
    ],
    [
        "Minority Report",
        "An action-detective thriller set in Washington D.C. in 2054.",
        ("http://www.gstatic.com/"
         "tv/thumb/movieposters/29122/p29122_p_v8_ap.jpg"),
        "https://www.youtube.com/watch?v=lG7DGMgfOb8",
    ],
    [
        "Pan's Labyrinth",
        "While exploring an ancient maze, Ofelia encounters the faun Pan.",
        ("http://www.gstatic.com/"
         "tv/thumb/movieposters/162074/p162074_p_v8_ab.jpg"),
        "https://www.youtube.com/watch?v=E7XGNPXdlGQ",
    ],
    [
        "Hellboy 2",
        "Hellboy faces his biggest battle.",
        ("http://www.gstatic.com/"
         "tv/thumb/movieposters/172364/p172364_p_v8_af.jpg"),
        "https://www.youtube.com/watch?v=Uw19ktMTZeA",
    ]
]

# create list of Movie objects
movies = []
for i in movie_data:
    movies.append(media.Movie(*i))

# creates and launches webpage
fresh_tomatoes.open_movies_page(movies)
