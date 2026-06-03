# Constants
# Subscription Types
PLAN_1 = 0
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
# ratings
G = 0
PG = 1
M = 2
MA = 3
R = 4
X = 5


credentials = {
    0: {
        "username": "Gex",
        "password": "123457890",
        "plan": PLAN_1,
        "credit_card": 1234567891000000,
        "active_profile": 0,
        "profiles": {0: {"name": "", "age": "", "watchlist": ""}},
    }
}


media = {
    "example": {
        "title": "",
        "type": SHOW,
        "display_path": "path",
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": M,
        "genre": [GEX, THE, GECKO],
    }
}
