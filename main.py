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
LOGIN_SUCCESS = 0
LOGIN_USER_ERR = 1
LOGIN_PASS_ERR = 2
class AccountManager():
    def __init__(self) -> None:
        self.profile_count = 0
        self.current_account = None

    def login(self, username, password) -> int:
        for index in data.credentials:
            if data.credentials[index]["username"] == username:
                if data.credentials[index]["password"] == password:
                    self.current_account = index
                    return LOGIN_SUCCESS
                else :
                    return LOGIN_PASS_ERR
        return LOGIN_USER_ERR

    def logout(self):
        pass
    def add_profile(self):
        pass
    def set_profile(self):
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
