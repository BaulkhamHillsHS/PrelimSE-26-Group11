import csv
import datetime

import customtkinter as ctk
from PIL import Image

import data

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class Media:
    def __init__(self, id: int) -> None:
        m_data = data.media[id]
        self.id = id  # this should also be its index when in the home scene
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
    def __init__(self, id: int):
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


class AccountManager:
    def __init__(self) -> None:
        # class Constants
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        self.FIELDS = [
            "username",
            "email",
            "password",
            "plan",
            "payment",
            "active_profile",
            "profiles",
            "watchlist",
        ]
        # index of current account
        self.current_account = {}
        self.accounts = []

    # attempts to login
    def login(self, username, password) -> int:
        for account in self.accounts:
            if account["username"] != username and account["email"] != username:
                continue
            if account["password"] != password:
                self.current_account = account
                return self.LOGIN_PASS_ERR
            return self.LOGIN_SUCCESS
        return self.LOGIN_USER_ERR

    def logout(self):
        self.current_account = {}

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

    def append_csv(self, path):
        pass


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
        self.account_manager.load_csv("accounts.csv")
        self.log_manager = LogManager(self.account_manager)

        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self.current_scene = self.NONE

        self.scenes: dict[int, Scene] = {
            self.LOGIN: LoginScene(self, self.account_manager),
            self.HOME: HomeScene(self, self.log_manager),
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


class Scene(ctk.CTkFrame):
    def __init__(self, master: StreamingApp):
        super().__init__(master)
        self.configure(width=540, height=720)

    def build_frame(self):
        self._build_header()
        self._build_main()

    def _build_header(self):
        self._frame_header = ctk.CTkFrame(self, width=400, height=200)
        self._frame_header.pack(fill=ctk.X)
        # self.image = ctk.CTkImage(light_image=Image.open("Gex2Cover.jpg"))
        self.title = ctk.CTkLabel(
            self._frame_header, text="GEx VIDEos"
        )  # , image=self.image)
        self.title.pack()

    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different"""
        pass
        # old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()


class LoginScene(Scene):
    def __init__(self, master: StreamingApp, account_manager):
        super().__init__(master)
        self.streaming_app = master
        self.account_manager = account_manager

    def _build_header(self):
        """Redefined to empty for the login scene, as the user should not have access to the app functions before logging in."""
        pass

    def _build_main(self):
        self._frame_main = ctk.CTkFrame(self, width=400, height=400)
        self._frame_main.pack(expand=True, fill=ctk.Y)
        self.lbl_title = ctk.CTkLabel(
            self._frame_main, text="GEx VIDEos", font=("Comic Sans MS", 20)
        )
        self.lbl_title.pack(expand=True)

        self.lbl_username = ctk.CTkLabel(self._frame_main, text="Enter Username:")
        self.lbl_username.pack(anchor=ctk.S)
        self.ent_username = ctk.CTkEntry(
            self._frame_main, placeholder_text="eg. Gex T. Gecko"
        )
        self.ent_username.pack(expand=True)

        self.lbl_pw = ctk.CTkLabel(self._frame_main, text="Enter Password:")
        self.lbl_pw.pack(anchor=ctk.S)
        self.ent_pw = ctk.CTkEntry(
            self._frame_main, placeholder_text="eg. its_tail_time"
        )
        self.ent_pw.pack(expand=True)

        self.btn_login = ctk.CTkButton(
            self._frame_main,
            width=200,
            height=50,
            text="Start Surfing",
            command=self.login_button_clicked,
        )
        self.btn_login.pack(expand=True)

    def login_button_clicked(self):
        login_status = self.account_manager.login(
            self.ent_username.get(), self.ent_pw.get()
        )
        if login_status == self.account_manager.LOGIN_SUCCESS:
            print("yippee")
            self.streaming_app.switch_scene(self.streaming_app.HOME)
        if login_status == self.account_manager.LOGIN_USER_ERR:
            print("wring user  | ", self.ent_username.get())
        if login_status == self.account_manager.LOGIN_PASS_ERR:
            print("password wrong")


class HomeScene(Scene):
    def __init__(self, master, log_manager):
        super().__init__(master)
        self.log_manager: LogManager = log_manager
        self.media_list: list[Media] = []
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

    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        for i in range(len(self.media_list)):
            ctk.CTkLabel(
                self._frame_main,
                text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:",
            ).pack()
            ctk.CTkButton(
                self._frame_main,
                text=self.media_list[i].title,
                command=lambda media=self.media_list[i]: self.media_clicked(media),
            ).pack()

    def media_clicked(self, media):
        self.log_manager.add_viewing_activity(media)
        # switch to viewing scene(media)

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


if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()


#
