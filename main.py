from pickle import TRUE
from shlex import split
from statistics import median_low

import customtkinter as ctk
from PIL import Image

import data


# temporary code for until a gui is made
class temp:
    def __init__(self) -> None:
        self.media_list = {}
        self.visible_list = []
        for key in data.media:
            if data.media[key]["Type"] == data.MOVIE:
                self.media_list[key] = Movie(key)
            elif data.media[key]["Type"] == data.SHOW:
                self.media_list[key] = Show(key)
            self.visible_list.append(key)
        self.genre_filter = []
        self.ratings_filter = []

    def update_visible(self):
        pass


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
        # class enums
        self.LOGIN_SUCCESS = 0
        self.LOGIN_USER_ERR = 1
        self.LOGIN_PASS_ERR = 2
        # index of current account
        self.current_account = -1

    # attempts to login
    def login(self, username, password) -> int:
        for index in data.credentials:
            if data.credentials[index]["username"] == username:
                if data.credentials[index]["password"] == password:
                    self.current_account = index
                    return self.LOGIN_SUCCESS
                else:
                    return self.LOGIN_PASS_ERR
        return self.LOGIN_USER_ERR

    def logout(self):
        self.current_account = -1

    def add_profile(self):
        pass

    def set_profile(self):
        pass


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
    debug_terminal()


def debug_terminal():
    while TRUE:
        while True:
            username = input("enter username : ")
            password = input("enter password : ")
            login_status = account_manager.login(username, password)
            if login_status == account_manager.LOGIN_SUCCESS:
                print(
                    f"logged into {data.credentials[account_manager.current_account]['username']}"
                )
                break
            elif login_status == account_manager.LOGIN_USER_ERR:
                print("Incorrect username")
            else:
                print("Incorrect password")
        command = input(
            f"{data.credentials[account_manager.current_account]['username']}>"
        )
        command_list = command.split(" ")
        if len(command_list) <= 0:
            continue
        if command_list[0] == "profile":
            if len(command_list) <= 1:
                pass


if __name__ == "__main__":
    main()
