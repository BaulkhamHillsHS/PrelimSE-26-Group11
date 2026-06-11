# Constants
# Subscription Types
BASE_PLAN = 0
PREMIUM_PLAN = 1

# Genres
GEX = 0
THE = 1
GECKO = 2
# types
SHOW = 0
MOVIE = 1
# ratings
G = 0
PG = 1
M = 2
MA = 3
R = 4
X = 5

plans = {
    BASE_PLAN: {"name": "Base Plan", "monthly_price": 9.99},
    PREMIUM_PLAN: {"name": "Base Plan", "monthly_price": 19.99},
}

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
