import csv
import datetime
from ast import literal_eval

import customtkinter as ctk
from PIL import Image

import data
import encryption
import scene

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class AccountManager:
    def __init__(self) -> None:
        # class Constants
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        self.CSV_PATH = "accounts.csv"
        self.FIELDS = [
            "username",
            "email",
            "password",
            "plan",
            "payment",
            "active_profile",
            "profiles",
        ]
        # index of current account
        self.current_account = {}
        self._accounts = []
        """
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

    # attempts to login
    def login(self, username, password) -> int:
        for account in self._accounts:
            if account["username"] != username and account["email"] != username:
                continue
            if encryption.decrypt(account["password"]).decode("utf-8") != password:
                return self.LOGIN_PASS_ERR
            self.current_account = account
            return self.LOGIN_SUCCESS
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

    def save_csv(self):
        with open(self.CSV_PATH, "w", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writeheader()
            for account in self._accounts:
                writer.writerow(account)

    def load_csv(self):
        self._accounts = []
        with open(self.CSV_PATH, "r", newline="") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # assigns each value of the row to the correct type
                row["username"] = str(row["username"])
                row["email"] = str(row["email"])
                # convert byte formatted as a string to byte
                row["password"] = literal_eval(row["password"])
                row["plan"] = int(row["plan"])
                row["payment"] = str(row["payment"])
                row["active_profile"] = int(row["active_profile"])
                # convert list formatted as a string to list
                row["profiles"] = literal_eval(row["profiles"])

                self._accounts.append(row)

    def append_csv(self, new_account):
        with open(self.CSV_PATH, "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, self.FIELDS)
            writer.writerow(new_account)
            print(new_account)


class LogManager:
    def __init__(self, account_manager: AccountManager) -> None:
        self.path = "log.txt"
        self.account_manager: AccountManager = account_manager

    def add_viewing_activity(self, media) -> None:
        with open(self.path, "a") as f:
            f.write(
                f"{datetime.datetime.now()} : {self.account_manager.current_account['username']} watched {media.title}\n"
            )

    def add_subscription_activity(self, current_plan, new_plan) -> None:
        with open(self.path, "a") as f:
            f.write(f"""Invoice for change in subscription plan
Account name : {self.account_manager.current_account["username"]}
Payment Credentials : {self.account_manager.current_account["playment"]}
Old Plan : {data.plans[current_plan]["name"]} @ {data.plans[current_plan]["price"]}/month
New Plan : {data.plans[new_plan]["name"]} @ {data.plans[new_plan]["price"]}/month
""")


class MediaManager:
    def __init__(self) -> None:
        self.media_list = []
        self.visible_list = []
        for i in range(len(data.media)):
            media = data.media[i]
            if media["type"] == data.MOVIE:
                self.media_list.append(Movie(i))
            elif media["type"] == data.SHOW:
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


class Media:
    def __init__(self, id: int) -> None:
        m_data = data.media[id]
        self.id = id
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


class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Scene Ids
        self.NONE = -1
        self.WELCOME = 0
        self.LOGIN = 1
        self.HOME = 2
        self.VIEW = 3
        self.SUBSCRIBE = 5

        # managers
        self.account_manager = AccountManager()
        self.account_manager.load_csv()
        self.log_manager = LogManager(self.account_manager)
        self.media_manager = MediaManager()

        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self.current_scene = self.NONE

        self.scenes: dict[int, scene.Scene] = {
            self.LOGIN: scene.LoginScene(self, self.account_manager),
            self.HOME: scene.HomeScene(self, self.log_manager, self.media_manager),
        }

        self.cached_scenes = []
        # scenes that have been loaded in that can be simply reloaded with pack() or grid() instead
        # of instantiating a new object
        self.switch_scene(self.LOGIN)

    def switch_scene(self, scene_id):
        # currentrly scene must use pack
        # extra logic for grid can be added later
        #
        if self.current_scene != self.NONE:
            self.scenes[self.current_scene].destroy()
        self.scenes[scene_id].build_frame()
        self.scenes[scene_id].pack()
        self.current_scene = scene_id


if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()
