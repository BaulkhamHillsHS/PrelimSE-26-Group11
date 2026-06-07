import csv

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

csv_text = """username,password,plan,payment,active_profile,profile_name1
"""
fields = [
    "index",
    "username",
    "password",
    "plan",
    "payment",
    "active_profile",
    "profiles",
]
credentials = {
    0: {
        "username": "Gex",
        "password": "1234567890",
        "plan": PLAN_1,
        "payment": 1234567891000000,
        "active_profile": 0,
        "profiles": [{"name": "I love Gex", "rating": "", "watchlist": ""}],
    },
    1: {
        "username": "Gex2",
        "password": "123454567890",
        "plan": PLAN_1,
        "payment": 123453467891000000,
        "active_profile": 0,
        "profiles": [{"name": "I lo4354ve Gex", "rating": "", "watchlist": ""}],
    },
}
with open("accounts.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fields)
    writer.writeheader()
    for key, val in sorted(credentials.items()):
        row = {"index": key}
        row.update(val)
        writer.writerow(row)
with open("accounts.csv", "r", newline="") as csvfile:
    reader = csv.DictReader(csvfile)
    for i in reader:
        print(i)
media = {
    -1: {
        "title": "",
        "type": MOVIE,
        "display_path": "path",
        "thumbnail": "path",
        "length_sec": 1000,
        "rating": M,
        "genre": [GEX, THE, GECKO],
    },
    -2: {
        "title": "",
        "type": SHOW,
        "display_path": "path",
        "thumbnail": ["path", "path2"],
        "length_sec": 1000,
        "rating": M,
        "genre": [GEX, GECKO],
    },
}
