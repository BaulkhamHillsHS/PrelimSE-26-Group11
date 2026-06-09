
import customtkinter as ctk
import tkinter as tk
# I don't have pillow installed so currently this is meaningless
#from PIL import Image

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self._build_ui()

    def _build_ui(self):
        scene = Scene(self)
        scene.pack(fill="both")
        

class Scene(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self._build_header()
        self._build_main()

    def _build_header(self):
        self._frame_header = ctk.CTkFrame(self, width=400, height=200)
        #self.image = ctk.CTkImage(light_image=Image.open("Gex2Cover.jpg"))
        self.title = ctk.CTkLabel(self._frame_header, text="GEx VIDEos") #, image=self.image)
        self.title.pack()
        self._frame_header.pack(fill="x")

    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different"""
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        for i in range(4):
            ctk.CTkLabel(self._frame_main, text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:").pack()
        self._frame_main.pack()
        #old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()
    
if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()