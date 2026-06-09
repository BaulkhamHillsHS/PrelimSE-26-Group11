import csv
import time

import customtkinter as ctk
from PIL import Image

import data

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self._build_ui()

    def _build_ui(self):
        scene = LoginScene(self)
        scene.pack(expand=True, fill=ctk.BOTH)
        

class Scene(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=540, height=720)
        self._build_header()
        self._build_main()

    def _build_header(self):
        self._frame_header = ctk.CTkFrame(self, width=400, height=200)
        self._frame_header.pack(fill=ctk.X)
        #self.image = ctk.CTkImage(light_image=Image.open("Gex2Cover.jpg"))
        self.title = ctk.CTkLabel(self._frame_header, text="GEx VIDEos") #, image=self.image)
        self.title.pack()
    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different"""
        pass
        #old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()

class LoginScene(Scene):
    def __init__(self, master):
        super().__init__(master)
    def _build_header(self):
        '''Redefined to empty for the login scene, as the user should not have access to the app functions before logging in.'''
        pass
    def _build_main(self):
        self._frame_main = ctk.CTkFrame(self, width=400, height=400)
        self._frame_main.pack(expand=True, fill=ctk.Y)
        self.lbl_title = ctk.CTkLabel(self._frame_main, text="GEx VIDEos", font=("Comic Sans MS", 20))
        self.lbl_title.pack(expand=True)
        
        self.lbl_username = ctk.CTkLabel(self._frame_main, text="Enter Username:")
        self.lbl_username.pack(anchor=ctk.S)
        self.ent_username = ctk.CTkEntry(self._frame_main, placeholder_text="eg. Gex T. Gecko")
        self.ent_username.pack(expand=True)
        
        self.lbl_pw = ctk.CTkLabel(self._frame_main, text="Enter Password:")
        self.lbl_pw.pack(anchor=ctk.S)
        self.ent_pw = ctk.CTkEntry(self._frame_main, placeholder_text="eg. its_tail_time")
        self.ent_pw.pack(expand=True)
        
        self.btn_login = ctk.CTkButton(self._frame_main, width=200, height=50, text="Start Surfing")
        self.btn_login.pack(expand=True)

class HomeScene(Scene):
    def __init__(self, master):
        super().__init__(master)
    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        for i in range(4):
            ctk.CTkLabel(self._frame_main, text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:").pack()

if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()



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

"""
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
"""
