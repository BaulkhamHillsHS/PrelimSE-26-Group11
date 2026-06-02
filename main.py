import customtkinter as ctk
from PIL import Image
import data




class SceneManager():
    def __init__(self, ctk_app : ctk.ctk):
        self.ctk_app = ctk_app
    def switch_scene(self, scene, *args): -> None
        # match LOGIN:
        #   self.ctk_app.buildlogin()
        pass

class Media():
    def __init__(self, id) -> None:
        self.m_data = data.media[id]
        self.title = m_data[title]
        self.display_path = m_data[path]
    
        self.thumbnail = m_data[thumbnail]
        self.length_sec = m_data[length_sec]
        self.rating = m_data[rating]
        self.genre = m_data[genre]

    def get_display(self) -> ctk.CTkImage:
        pass

    def build_card(self) -> void:
        
        

class Movie(Media):
    def __init__(self, id) -> None:
        super.__init__(self, id)
    
    def get_display(self) -> ctk.CTkImage:
        if display == None:
            display =  customtkinter.CTkImage(light_image=Image.open(self.display_path[key]),
                                 size=(30, 30))
        return display

class Show(Media)
    def __init__(self, id) -> None:
        super.__init__(self, id)
        self.display = None
    
    def get_display(self, key) -> ctk.CTkImage:
        if display[key] == None:
            display[key] =  customtkinter.CTkImage(light_image=Image.open(self.display_path[key]),
                                 size=(30, 30))
        return display[key]