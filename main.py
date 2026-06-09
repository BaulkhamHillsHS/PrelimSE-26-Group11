import csv
import time

import customtkinter as ctk
from PIL import Image

import data


# temporary code for until a gui is made
class temp:
    # will be part of the main window
    def __init__(self) -> None:
        self.media_list = []
        self.visible_list = []
        for i in range(len(data.media)):
            media = data.media[i]
            if media["Type"] == data.MOVIE:
                self.media_list.append(Movie(i))
            elif media["Type"] == data.SHOW:
                self.media_list.append(Show(i))
            self.visible_list.append(i)
        self.genre_filter = [data.GEX, data.THE, data.GECKO]
        self.type_filter = [data.MOVIE, data.SHOW]
        self.ratings_filter = data.X

    def update_visible(self):
        self.visible_list = []
        for i in range(len(self.media_list)):
            media = self.media_list[i]
            if media["rating"] > self.ratings_filter:
                continue
            if media["type"] not in self.type_filter:
                continue
            for genre in media["genre"]:
                if genre in self.genre_filter:
                    break
            else:
                continue
            self.visible_list.append(i)
        print(self.visible_list)


class LogManager:
    def __init__(self) -> None:
        self.log_txt = "log.txt"

    def add_viewing_activity(self, media) -> None:
        with open("self.log_txt", "a") as f:
            f.write(f"{time.time} : watched {media['name']}")

    def add_subscription_activity(self) -> None:
        pass


# will depricate
class SceneManager:
    def __init__(self, ctk_app: ctk.CTk):
        self.ctk_app = ctk_app

    def switch_scene(self, scene, *args) -> None:
        # match LOGIN:
        #   self.ctk_app.buildlogin()
        a = 1
        pass


class AccountManager:
    def __init__(self) -> None:
        # class Constants
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        self.FIELDS = [
            "username",
            "password",
            "plan",
            "payment",
            "active_profile",
            "profiles",
        ]
        # index of current account
        self.current_account = {}
        self.accounts = []

    # attempts to login
    def login(self, username, password) -> int:
        for account in self.accounts:
            if account["username"] == username:
                if account["password"] == password:
                    self.current_account = account
                    return self.LOGIN_SUCCESS
                else:
                    return self.LOGIN_PASS_ERR
        return self.LOGIN_USER_ERR

    def logout(self):
        self.current_account = {}
        # switch to login screen

    def set_profile(self, profile):
        self.current_account["active_profile"] = profile
        # switch to welcome screen
        # update content filters

    def set_plan(self, plan):
        self.current_account["plan"] = plan
        # notify log manager(plan)

    def save_csv(self, path):
        with open(path, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writeheader()
            for account in self.accounts:
                writer.writerow(account)

    def load_csv(self, path):
        self.accounts = []
        with open(path, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                self.accounts.append(row)


#
class Media:
    def __init__(self, id) -> None:
        m_data = data.media[id]
        self.title = m_data["title"]
        self.display_path = m_data["display_path"]
        self.thumbnail = m_data["thumbnail"]
        self.length_sec = m_data["length_sec"]
        self.rating = m_data["rating"]
        self.genre = m_data["genre"]

    def build_card(self) -> None:
        pass

    def card_pressed(self) -> None:
        pass


class Movie(Media):
    def __init__(self, id):
        super.__init__(id)
        self.display = ctk.CTkImage(
            light_image=Image.open(self.display_path), size=(30, 30)
        )


class Show(Media):
    def __init__(self, id):
        super.__init__(id)
        self.display = []
        for path in self.display_path:
            self.display.append(
                ctk.CTkImage(light_image=Image.open(path), size=(30, 30))
            )


# scene_manager = SceneManager()
account_manager = AccountManager()


def main():
    account_manager.load_csv("accounts.csv")
    debug_terminal()


def debug_terminal():
    while True:
        while True:
            username = input("enter username : ")
            password = input("enter password : ")
            login_status = account_manager.login(username, password)
            if login_status == account_manager.LOGIN_SUCCESS:
                print(f"logged into {account_manager.current_account['username']}")
                break
            elif login_status == account_manager.LOGIN_USER_ERR:
                print("Incorrect username")
            else:
                print("Incorrect password")


if __name__ == "__main__":
    main()
