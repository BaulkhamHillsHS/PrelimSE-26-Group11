# file to store utilities like managers
import csv
import datetime
from ast import literal_eval

import encryption

import data

class Account():
    def __init__(self, data):
        # assigns each value of the row to the correct type
        self._data = {}
        self._data["username"] = str(data["username"])
        self._data["email"] = str(data["email"])
        # convert byte formatted as a string to byte
        self._data["password"] = literal_eval(data["password"])
        self._data["plan"] = int(data["plan"])
        self._data["payment"] = str(data["payment"])
        self._data["active_profile"] = int(data["active_profile"])
        # convert list formatted as a string to list
        self._data["profiles"] = literal_eval(data["profiles"])

    def get_data(self):
        return self._data

    def p_get(self, property):
        if property in self._data:
            return self._data[property]
        else : return None
    
    def set_plan(self, plan):
        self._data["plan"] = plan


class AccountManager:
    def __init__(self) -> None:
        # class Constants
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        self.CSV_PATH = "data/accounts.csv"
        self.FIELDS = ["username", "email", "password", "plan", "payment", "profiles"]
        # index of current account
        self.current_account = {}
        self._accounts = []
        self._profile = 0

    # attempts to login
    def login(self, username, password) -> int:
        for account in self._accounts:
            if account.p_get("username") != username and account.p_get("email") != username:
                continue
            if encryption.validate_password(account.p_get("password"), password):
                self.current_account = account
                return self.LOGIN_SUCCESS
            return self.LOGIN_PASS_ERR
        return self.LOGIN_USER_ERR

    def logout(self):
        self.current_account = {}
        # switch to login screen

    def set_profile(self, profile):
        self._profile = profile
        # switch to welcome screen
        # update content filters

    def get_active_profile(self):
        return self.current_account.p_get("profiles")[self._profile]


    def save_csv(self):
        with open(self.CSV_PATH, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writeheader()
            for account in self._accounts:
                writer.writerow(account.get_data())

    def load_csv(self):
        self._accounts = []
        with open(self.CSV_PATH, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self._accounts.append(Account(row))

    def append_csv(self, new_account):
        with open(self.CSV_PATH, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writerow(new_account)


class LogManager:
    def __init__(self, account_manager: AccountManager) -> None:
        self.path = "data/log.txt"
        self.acc_man: AccountManager = account_manager

    def add_viewing_activity(self, media) -> None:
        with open(self.path, "a") as f:
            f.write(
                f"{datetime.datetime.now()} : {self.acc_man.current_account['username']} watched {media.title}\n"
            )

    def add_subscription_activity(self, current_plan, new_plan) -> None:
        with open(self.path, "a") as f:
            f.write(f"""Invoice for change in subscription plan
Account name : {self.acc_man.current_account["username"]}
Payment Credentials : {self.acc_man.current_account["playment"]}
Old Plan : {data.plans[current_plan]["name"]} @ {data.plans[current_plan]["price"]}/month
New Plan : {data.plans[new_plan]["name"]} @ {data.plans[new_plan]["price"]}/month
""")


class MediaManager:
    def __init__(self, account_manager : AccountManager) -> None:
        self.media_list = []
        self.visible_list = []
        self.acc_man : AccountManager = account_manager
        self.current_viewed : int

        for i in range(len(data.media)):
            media_data = data.media[i]
            if media_data["type"] == data.MOVIE:
                self.media_list.append(data.Movie(i))
            elif media_data["type"] == data.SHOW:
                self.media_list.append(data.Show(i))
            self.visible_list.append(i)

        self.genre_filter = [data.GEX, data.THE, data.GECKO]
        self.type_filter = [data.MOVIE, data.SHOW]
        self.ratings_filter = data.X

    def update_visible(self):
        # update list
        self.visible_list = []
        for i in range(len(self.media_list)):
            media : data.Media = self.media_list[i]
            if media.rating > self.ratings_filter:
                continue
            if media.type not in self.type_filter:
                continue
            for genre in media.genre:
                if genre in self.genre_filter:
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
    "active_profile": 0,
    "profiles": [{"name": "Aupen ", "age": 20, "watchlist": [0, 1, 2]}],
}
self._accounts.append(append_test_account)
self.append_csv(append_test_account)
"""
