import customtkinter as ctk
from PIL import Image
import data




class SceneManager():
    def __init__(self, ctk_app : ctk.CTk):
        self.ctk_app = ctk_app
    def switch_scene(self, scene, *args) -> None:
        # match LOGIN:
        #   self.ctk_app.buildlogin()
        a = 1
        pass

class AccountManager():
    def __init__(self) -> None:
        self.profile_count = 0
        self.current_profile = None
    def register_user(self):
        current_profile = 0
        data.credentials[0] = {
            "username": "Gex",
            "password": "123457890",
            "plan": data.PLAN_1,
            "credit_card": 1234567891000000,
            "profiles": {0: {"name": "", "age": "", "watchlist": ""}},
        }
        self.profile_count += 1
    def login(self):
        pass
    def logout(self):
        pass
    def add_profile(self):
        pass

class Media():
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


class Movie(Media):
    def __init__(self, id):
        super.__init__(id)
        self.display = ctk.CTkImage(light_image=Image.open(self.display_path), size=(30, 30))


class Show(Media)
    def __init__(self, id):
        super.__init__(id)
        self.display = []
        for path in self.display_path:
            self.display.append(ctk.CTkImage(light_image=Image.open(path), size=(30, 30)))



scene_manager = SceneManager()
