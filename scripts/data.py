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
    OTHER : "Other"
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

rating_names = {G : "G", PG : "PG", M : "M", MA : "MA", R : "R", X : "X"}

plans = [{"name" : "Basic Plan", "price": 9.99}, 
        {"name" : "Premium Plan", "price": 19.99}]

# need to replace "path"s with image paths
media = [
    {
        "title": "Gex 1 Intro Cutscene",
        "type": MOVIE,
        "display_path": "path",
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": G,
        "genre": [GEX, THE, GECKO],
    },
    {
        "title": "Gex 1 Ending Cutscene",
        "type": MOVIE,
        "display_path": "path",
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": G,
        "genre": [GEX, THE, GECKO],
    },
    {
        "title": "Gex 1 compilation",
        "type": SHOW,
        "display_path": ["path", "path2"],
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": G,
        "genre": [GEX, GECKO],
    },
    {
        "title": "Hardcore Gex",
        "type": MOVIE,
        "display_path": ["path"],
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": X,
        "genre": [GEX],
    },
]


class Media:
    def __init__(self, id: int) -> None:

        self.id = id
        self.title = media[id]["title"]
        self.display_path = media[id]["display_path"]
        self.thumbnail = media[id]["thumbnail"]
        self.length_sec = media[id]["length_sec"]
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
        # self.display = ctk.CTkImage(
        #    light_image=Image.open(self.display_path), size=(30, 30)
        # )


class Show(Media):
    def __init__(self, id):
        super().__init__(id)
        self.display = []
        # for path in self.display_path:
        #    self.display.append(
        #        ctk.CTkImage(light_image=Image.open(path), size=(30, 30))
        #    )
