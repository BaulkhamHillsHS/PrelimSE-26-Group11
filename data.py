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

plans = {"base_plan": {"monthly_price": 9.99}, "premium_plan": {"monthly_price": 19.99}}

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
]
