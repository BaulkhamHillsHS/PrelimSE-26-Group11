import csv
import datetime
from ast import literal_eval
import encryption
import data

# file to store utilities like managers

# class for individual profiles within accounts
class Profile():
    def __init__(self, data):

        self._name = data["name"]
        self._age = data["age"]
        self._history = []
        self.watchlist = []
        for watch in data["watchlist"]:
            self.watchlist.append(int(watch))
        
    def get(self, property):
        match property:
            case "name":
                return self._name
            case "age":
                return self._age
            case "watchlist":
                return self.watchlist
            case "history":
                return self._history

    def get_data(self) -> dict:
        return {"name" : self._name,
                "age" : self._age,
                "watchlist" : self.watchlist,
                "history" : self._history}

    def append_history(self, media):
        self._history.append(media)

    

class Account():
    def __init__(self, data):
        self._data = data
        # assigns each value of the row to the correct type
        self._username = data["username"]
        self._email = data["email"]
        self._password = data["password"] # convert byte formatted as a string to byte
        self._plan = data["plan"]
        self._payment = data["payment"]
        profiles = data["profiles"]
        self._profiles : list[Profile] = [] # list of profile objects
        for profile in  profiles:
            self._profiles.append(Profile(profile))
    
    def __del__(self):
        for profile in self._profiles:
            del profile

    def get_data(self) -> dict:
        profile_data = []
        for profile in self._profiles:
            profile_data.append(profile.get_data())
        return {"username" : self._username,
                "email" : self._email,
                "password" : self._password,
                "plan" : self._plan,
                "payment" : self._payment,
                "profiles" : profile_data}


    def get(self, property):
        match property:
            case "username":
                return self._username
            case "email":
                return self._email
            case "password":
                return self._password
            case "plan":
                return self._plan
            case "payment":
                return self._payment
            case "profiles":
                return self._profiles
    
    def set_plan(self, plan):
        self._plan = plan


class AccountManager:
    def __init__(self) -> None:
        # class Constants
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        self.CSV_PATH = "data/accounts.csv"
        self.FIELDS = ["username", "email", "password", "plan", "payment", "profiles"]
        # index of current account
        self.current_account = None
        self._current_account_index = None
        self._accounts = []
        self._profile = 0
        # list of dicts that gets saves as a csv
        self._account_data = []

    # attempts to login
    def login(self, username, password) -> int:
        for i in range(len(self._account_data)):
            account = self._account_data[i]
            if account["username"] != username and account["email"] != username:
                continue
            if encryption.validate_password(account["password"], password):
                if self._current_account_index:
                    # updates account data if there was a previous account
                    self._account_data[self._current_account_index] = self.current_account.get_data()
                # creats account instance
                self.current_account = Account(account)
                self._current_account_index = i
                return self.LOGIN_SUCCESS
            return self.LOGIN_PASS_ERR
        return self.LOGIN_USER_ERR

    def logout(self):
        # updates account data
        if self._current_account_index:
            self._account_data[self._current_account_index] = self.current_account.get_data()
        del self.current_account
        self.current_account = None

    def set_profile(self, profile):
        self._profile = profile


    def get_active_profile(self) -> Profile:
        return self.current_account.get("profiles")[self._profile]

    def get_current_index(self) -> int:
        return self._current_account_index

    def save_csv(self):
        # saves self._account_data to csv
        if self._current_account_index:
            self._account_data[self._current_account_index] = self.current_account.get_data()
        with open(self.CSV_PATH, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writeheader()
            for account in self._account_data:
                writer.writerow(account)

    def load_csv(self):
        self._accounts = []
        with open(self.CSV_PATH, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                row_data = {}
                # assigns each value of the row to the correct type
                row_data["username"] = str(row["username"])
                row_data["email"] = str(row["email"])
                # convert byte formatted as a string to byte
                row_data["password"] = literal_eval(row["password"])
                row_data["plan"] = int(row["plan"])
                row_data["payment"] = str(row["payment"])
                # convert list formatted as a string to list
                row_data["profiles"] = literal_eval(row["profiles"])
                self._account_data.append(row_data)

    def append_csv(self, new_account):
        with open(self.CSV_PATH, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writerow(new_account)


class Logger:
    def __init__(self, account_manager: AccountManager) -> None:
        self.path = "data/log.txt"
        self.acc_man: AccountManager = account_manager

    def add_viewing_activity(self, media) -> None:
        with open(self.path, "a") as f:
            f.write(f"{datetime.datetime.now()} : {self.acc_man.current_account.get('username')} watched {media.title}\n")

    def add_subscription_activity(self, current_plan, new_plan) -> None:
        with open(self.path, "a") as f:
            f.write(f"""==========================================
Invoice for change in subscription plan
Account name : {self.acc_man.current_account.get("username")}
Payment Credentials : {self.acc_man.current_account.get("playment")}
Date : {datetime.date.today()}
Old Plan : {data.plans[current_plan]["name"]} @ ${data.plans[current_plan]["price"]}/month
New Plan : {data.plans[new_plan]["name"]} @ ${data.plans[new_plan]["price"]}/month
==========================================
""")


class Library:
    def __init__(self, account_manager : AccountManager):
        self.media_list : list[data.Media] = []
        self.visible_list : list[int] = []
        self.acc_man : AccountManager = account_manager
        self.current_viewed : int
        self.is_watchlist = False

        # makes media and visible list
        for i in range(len(data.media)):
            media_data = data.media[i]
            if media_data["type"] == data.MOVIE:
                self.media_list.append(data.Movie(i))
            elif media_data["type"] == data.SHOW:
                self.media_list.append(data.Show(i))
            self.visible_list.append(i)

        self.genre_filter = None
        self.type_filter = [data.MOVIE, data.SHOW]
        self.ratings_filter = data.X

    def update_visible(self):
        # update list
        self.visible_list = []
        for i in range(len(self.media_list)):
            if self.is_watchlist:
                if i not in self.acc_man.get_active_profile().get("watchlist"):
                    continue
            media : data.Media = self.media_list[i]
            if media.rating > self.ratings_filter:
                continue
            if media.type not in self.type_filter:
                continue
            if self.genre_filter != None:
                for genre in media.genre:
                    if genre == self.genre_filter:
                        break
                else:
                    continue
            self.visible_list.append(i)


""" appending example
append_test_account = {
    "username": "Aupen_D_Teszd",
    "email": "aupen.teszd@gmail.com",
    "password": "b'gAAAAABqLUAW6jgMaaVp2I3VHapsXqb87kTx7720GtpynBb92X_QNPLbwGfsecwxrVD8yyGkmYqd1_Hg5v4Y5zPo9fvBk-0jSA=='",
    "plan": data.PREMIUM_PLAN,
    "payment": "1234567890",
    "profiles": [{"name": "Aupen ", "age": 20, "watchlist": [0, 1, 2], "history" : []}],
}
self._accounts.append(append_test_account)
self.append_csv(append_test_account)
"""
