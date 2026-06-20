import customtkinter as ctk
from PIL import Image
# Constants
# Subscription Types
BASE_PLAN = 0
PREMIUM_PLAN = 1

# Scene Ids
WELCOME = 0
LOGIN = 1
HOME = 2
VIEW = 3
SUBSCRIBE = 5
# Genres
GEX = 0
THE = 1
GECKO = 2

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

plans = [{"name" : "Basic Plan", "price": 9.99}, 
        {"name" : "Premium Plan", "price": 19.99}]

# need to replace "path"s with image paths
media = [
    {
        "title": "Crystal Dynamics Intro",
        "type": MOVIE,
        "display_path": "data/images/0_gex_cdlogo.png",
        "thumbnail": "data/images/0_gex_cdlogo.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 Intro Cutscene",
        "type": MOVIE,
        "display_path": "data/images/1_gex1_intro.png",
        "thumbnail": "data/images/1_gex1_intro.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 Ending Cutscene",
        "type": MOVIE,
        "display_path": "data/images/2_gex1_outro.png",
        "thumbnail": "data/images/2_gex1_outro.png",
        "rating": G,
        "genre": [GEX_1, CUTSCENE],
    },
    {
        "title": "Gex 1 compilation",
        "type": SHOW,
        "display_path": ["data/images/3_gex1_comp.png", "data/images/temp.png"],
        "thumbnail": "data/images/3_gex1_comp.png",
        "rating": G,
        "genre": [GEX, CUTSCENE, COMPILATION],
    },
    {
        "title": "Gex 1 Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/3_gex1_comp.png",
        "thumbnail": "data/images/3_gex1_comp.png",
        "rating": G,
        "genre": [GEX_1, TRAILER],
    },
    {
        "title": "Gex 1 Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_1, TRAILER],
    },
    {
        "title": "Gex Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_1, GAMEPLAY],
    },
    {
        "title": "Gex Letplay Series",
        "type": SHOW,
        "display_path": ["data/images/temp.png"],
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_1, GAMEPLAY],
    },
    {
        "title": "Gex Review",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_1, REVIEW],
    },
    {
        "title": "Gex: Enter the Gecko Title",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Intro",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Bloody Baboon",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Chinese Secret",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Lock 'n Load",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Father",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Pardon my Tongue",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": M,
        "genre": [GEX_2, CUTSCENE],
    },
    {
        "title": "Gex: Enter the Gecko Concept Art",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2],
    },
    {
        "title": "Gex: Enter the Gecko Cutscene compilation",
        "type": SHOW,
        "display_path": ["data/images/temp.png"],
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Trailer 3",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, TRAILER],
    },
    {
        "title": "Gex: Enter the Gecko Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, GAMEPLAY],
    },
    {
        "title": "Gex: Enter the Gecko Letsplay Series",
        "type": SHOW,
        "display_path": ["data/images/temp.png"],
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, GAMEPLAY],
    },
    {
        "title": "Gex: Enter the Gecko Review",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": G,
        "genre": [GEX_2, GAMEPLAY],
    },
    {
        "title": "Gex 3: Deep Cover Gecko Intro",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 1",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 3",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 4",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 5",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 6",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 7",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 8",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 9",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 10",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 11",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 12",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Agent Xtra 13",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Western",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: War",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Goon",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Outro",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Cutscene Compilation",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex 3: Letsplay",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_3, CUTSCENE],
    },
    {
        "title": "Gex Trilogy: Trailer 1",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Trailer 2",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Walkthrough",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Letsplay",
        "type": SHOW,
        "display_path": ["data/images/temp.png"],
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    },
    {
        "title": "Gex Trilogy: Review",
        "type": MOVIE,
        "display_path": "data/images/temp.png",
        "thumbnail": "data/images/temp.png",
        "rating": PG,
        "genre": [GEX_TRILOGY, TRAILER],
    }
]


class Media:
    def __init__(self, id: int) -> None:

        self.id = id
        self.title = media[id]["title"]
        self.display_path = media[id]["display_path"]
        self.thumbnail = ctk.CTkImage(light_image=Image.open(media[id]["thumbnail"]), size=(320, 180))
        self.rating = media[id]["rating"]
        self.genre = media[id]["genre"]
        self.type = media[id]["type"]

    def build_card(self) -> None:
        pass

    def card_pressed(self) -> None:
        pass


class Movie(Media):
    def __init__(self, id):
        super().__init__(id)
        self.display = ctk.CTkImage(
            light_image=Image.open(self.display_path), size=(640, 360)
        )


class Show(Media):
    def __init__(self, id):
        super().__init__(id)
        # these currently are just place holders as viewing individual episodes is
        # not in the scope of this project
        self.display_list = []
        for path in self.display_path:
            self.display_list.append(
                ctk.CTkImage(light_image=Image.open(path), size=(640, 360))
            )
