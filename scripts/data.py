import customtkinter as ctk
from PIL import Image

# Constants


# Genres
GEX_1 = 0
GEX_2 = 1
GEX_3 = 2
GEX_TRILOGY = 3
CUTSCENE = 4
TRAILER = 5
GAMEPLAY = 6
REVIEW = 7
COMPILATION = 8
OTHER = 9

genres = {
    GEX_1 : "Gex 1",
    GEX_2 : "Gex: Enter the Gecko",
    GEX_3 : "Gex 3: Deep Cover Gecko",
    GEX_TRILOGY : "GEX Trilogy",
    CUTSCENE : "Cutscene",
    TRAILER : "Trailer",
    GAMEPLAY : "Gameplay",
    REVIEW : "Review",
    COMPILATION : "Compilation",
}
genre_list = []
for i, j in genres.items():
    genre_list.append(j)

# types
SHOW = 0
MOVIE = 1
# ratings assigned to their minimum age (inclusive)
G = 0
PG = 13  # PG and M can techniquely be freely accessed but
M = 15  # implementing parental guidance options is not in
MA = 15  # the scope of this project
R = 18
X = 18

LOGO = ctk.CTkImage(light_image=Image.open("data/images/logo_light.png"),
                    dark_image=Image.open("data/images/logo_dark.png"), size=(250, 50))

rating_names = {G : "G", PG : "PG", M : "M", MA : "MA", R : "R", X : "X"}

# Subscription Types
BASE_PLAN = 0
PREMIUM_PLAN = 1
plans = [{"name" : "Basic Plan", "price": 9.99}, 
        {"name" : "Premium Plan", "price": 19.99}]


media = [
    {
        "title": "Crystal Dynamics Intro",
        "type": MOVIE,
        "display_path": "data/images/0.png",
        "thumbnail": "data/images/0.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 Intro Cutscene",
        "type": MOVIE,
        "display_path": "data/images/1.png",
        "thumbnail": "data/images/1.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 Ending Cutscene",
        "type": MOVIE,
        "display_path": "data/images/2.png",
        "thumbnail": "data/images/2.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 compilation",
        "type": SHOW,
        "display_path": ["data/images/3.png", "data/images/temp.png"],
        "thumbnail": "data/images/3.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE, COMPILATION],
    },
    {
        "title": "Gex 1 Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/4.png",
        "thumbnail": "data/images/4.png",
        "rating": G,
        "genre": [GEX_1, TRAILER],
    },
    {
        "title": "Gex 1 Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/5.png",
        "thumbnail": "data/images/5.png",
        "rating": G,
        "genre": [GEX_1, TRAILER],
    },
    {
        "title": "Gex Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/6.png",
        "thumbnail": "data/images/6.png",
        "rating": G,
        "genre": [GEX_1, GAMEPLAY],
    },
    {
        "title": "Gex Letsplay Series",
        "type": SHOW,
        "display_path": ["data/images/7.png", "data/images/temp.png"],
        "thumbnail": "data/images/7.png",
        "rating": G,
        "genre": [GEX_1, GAMEPLAY],
    },
    {
        "title": "Gex Review",
        "type": MOVIE,
        "display_path": "data/images/8.png",
        "thumbnail": "data/images/8.png",
        "rating": G,
        "genre": [GEX_1, REVIEW],
    },
    {
        "title": "Gex: Enter the Gecko Title",
        "type": MOVIE,
        "display_path": "data/images/9.png",
        "thumbnail": "data/images/9.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Intro",
        "type": MOVIE,
        "display_path": "data/images/10.png",
        "thumbnail": "data/images/10.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Bloody Baboon",
        "type": MOVIE,
        "display_path": "data/images/11.png",
        "thumbnail": "data/images/11.png",
        "rating": PG,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Chinese Secret",
        "type": MOVIE,
        "display_path": "data/images/12.png",
        "thumbnail": "data/images/12.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Lock 'n Load",
        "type": MOVIE,
        "display_path": "data/images/13.png",
        "thumbnail": "data/images/13.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Father",
        "type": MOVIE,
        "display_path": "data/images/14.png",
        "thumbnail": "data/images/14.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Pardon my Tongue",
        "type": MOVIE,
        "display_path": "data/images/15.png",
        "thumbnail": "data/images/15.png",
        "rating": M,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Concept Art",
        "type": MOVIE,
        "display_path": "data/images/16.png",
        "thumbnail": "data/images/16.png",
        "rating": G,
        "genre": [GEX_2],
    },
    {
        "title": "Gex: Enter the Gecko Cutscene compilation",
        "type": SHOW,
        "display_path": ["data/images/17.png"],
        "thumbnail": "data/images/17.png",
        "rating": G,
        "genre": [GEX_2, COMPILATION],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/18.png",
        "thumbnail": "data/images/18.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/19.png",
        "thumbnail": "data/images/19.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 3",
        "type": MOVIE,
        "display_path": "data/images/20.png",
        "thumbnail": "data/images/20.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/21.png",
        "thumbnail": "data/images/21.png",
        "rating": G,
        "genre": [GEX_2, GAMEPLAY],
    },
    {
        "title": "Gex: Enter the Gecko Letsplay Series",
        "type": SHOW,
        "display_path": ["data/images/22.png"],
        "thumbnail": "data/images/22.png",
        "rating": G,
        "genre": [GEX_2, GAMEPLAY],
    },
    {
        "title": "Gex: Enter the Gecko Review",
        "type": MOVIE,
        "display_path": "data/images/23.png",
        "thumbnail": "data/images/23.png",
        "rating": G,
        "genre": [GEX_2, REVIEW],
    },
    {
        "title": "Gex 3: Deep Cover Gecko Intro",
        "type": MOVIE,
        "display_path": "data/images/24.png",
        "thumbnail": "data/images/24.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 1",
        "type": MOVIE,
        "display_path": "data/images/25.png",
        "thumbnail": "data/images/25.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 2",
        "type": MOVIE,
        "display_path": "data/images/26.png",
        "thumbnail": "data/images/26.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 3",
        "type": MOVIE,
        "display_path": "data/images/27.png",
        "thumbnail": "data/images/27.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 4",
        "type": MOVIE,
        "display_path": "data/images/28.png",
        "thumbnail": "data/images/28.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 5",
        "type": MOVIE,
        "display_path": "data/images/29.png",
        "thumbnail": "data/images/29.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 6",
        "type": MOVIE,
        "display_path": "data/images/30.png",
        "thumbnail": "data/images/30.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 7",
        "type": MOVIE,
        "display_path": "data/images/31.png",
        "thumbnail": "data/images/31.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 8",
        "type": MOVIE,
        "display_path": "data/images/32.png",
        "thumbnail": "data/images/32.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 9",
        "type": MOVIE,
        "display_path": "data/images/33.png",
        "thumbnail": "data/images/33.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 10",
        "type": MOVIE,
        "display_path": "data/images/34.png",
        "thumbnail": "data/images/34.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 11",
        "type": MOVIE,
        "display_path": "data/images/35.png",
        "thumbnail": "data/images/35.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 12",
        "type": MOVIE,
        "display_path": "data/images/36.png",
        "thumbnail": "data/images/36.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 13",
        "type": MOVIE,
        "display_path": "data/images/37.png",
        "thumbnail": "data/images/37.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Western",
        "type": MOVIE,
        "display_path": "data/images/38.png",
        "thumbnail": "data/images/38.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: War",
        "type": MOVIE,
        "display_path": "data/images/39.png",
        "thumbnail": "data/images/39.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Goon",
        "type": MOVIE,
        "display_path": "data/images/40.png",
        "thumbnail": "data/images/40.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Outro",
        "type": MOVIE,
        "display_path": "data/images/41.png",
        "thumbnail": "data/images/41.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Cutscene Compilation",
        "type": SHOW,
        "display_path": ["data/images/42.png"],
        "thumbnail": "data/images/42.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE, COMPILATION],
    },
    {
        "title": "Gex 3: Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/43.png",
        "thumbnail": "data/images/43.png",
        "rating": PG,
        "genre": [GEX_3, TRAILER],
    },
    {
        "title": "Gex 3: Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/44.png",
        "thumbnail": "data/images/44.png",
        "rating": PG,
        "genre": [GEX_3, TRAILER],
    },
    {
        "title": "Gex 3: Trailer 3",
        "type": MOVIE,
        "display_path": "data/images/45.png",
        "thumbnail": "data/images/45.png",
        "rating": PG,
        "genre": [GEX_3, TRAILER],
    },
    {
        "title": "Gex 3: Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/46.png",
        "thumbnail": "data/images/46.png",
        "rating": PG,
        "genre": [GEX_3, GAMEPLAY],
    },
    {
        "title": "Gex 3: Letsplay",
        "type": SHOW,
        "display_path": ["data/images/47.png"],
        "thumbnail": "data/images/47.png",
        "rating": PG,
        "genre": [GEX_3, GAMEPLAY],
    },
    {
        "title": "Gex 3: Review",
        "type": MOVIE,
        "display_path": "data/images/48.png",
        "thumbnail": "data/images/48.png",
        "rating": PG,
        "genre": [GEX_3, REVIEW],
    },
    {
        "title": "Gex Trilogy: Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/49.png",
        "thumbnail": "data/images/49.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/50.png",
        "thumbnail": "data/images/50.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/51.png",
        "thumbnail": "data/images/51.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, GAMEPLAY],
    },
    {
        "title": "Gex Trilogy: Letsplay",
        "type": SHOW,
        "display_path": ["data/images/52.png"],
        "thumbnail": "data/images/52.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, GAMEPLAY],
    },
    {
        "title": "Gex Trilogy: Review",
        "type": MOVIE,
        "display_path": "data/images/53.png",
        "thumbnail": "data/images/53.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, REVIEW],
    }
]


class Media:
    def __init__(self, id: int):

        self.id = id
        self.title = media[id]["title"]
        self.display_path = media[id]["display_path"]
        self.thumbnail = ctk.CTkImage(light_image=Image.open(media[id]["thumbnail"]), size=(320, 180))
        self.rating = media[id]["rating"]
        self.genre = media[id]["genre"]
        self.type = media[id]["type"]


class Movie(Media):
    def __init__(self, id):
        super().__init__(id)
        self.display = ctk.CTkImage(light_image=Image.open(self.display_path), size=(640, 360))


class Show(Media):
    def __init__(self, id):
        super().__init__(id)
        # these currently are just place holders as viewing individual episodes is
        # not in the scope of this project
        self.display_list = []
        for path in self.display_path:
            self.display_list.append(ctk.CTkImage(light_image=Image.open(path), size=(640, 360)))
