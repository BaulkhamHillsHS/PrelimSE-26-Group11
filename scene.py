import customtkinter as ctk
from PIL import Image

class Scene(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=540, height=720)
        self._build_header()
        self._build_main()

    def _build_header(self):
        '''Build the logo and navigation bar at the top of the screen that is in most scenes in the app.'''
        # add frame and configure grid inside frame
        self._frame_header = ctk.CTkFrame(self, width=400, height=200)
        self._frame_header.pack(fill=ctk.X)
        self._frame_header.rowconfigure(0, weight=1)
        self._frame_header.columnconfigure((0,1,2), weight=1)
        
        # load image and display logo label containing image
        self.img_logo = ctk.CTkImage(light_image=Image.open("images/Gex2Cover.jpg"), size=(80,80))
        # text=' ' (single space) to not display default 'CTkLabel' text on label
        self.lbl_logo = ctk.CTkLabel(self._frame_header, text=' ', image=self.img_logo)
        self.lbl_logo.grid(row=0, column=0)
        
        self.lbl_title = ctk.CTkLabel(self._frame_header, text="GEx VIDEos", font=("Comic Sans MS", 20))
        self.lbl_title.grid(row=0, column=1, sticky='w')
        
    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different."""
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
        '''Build a simple username and password form with a title and a button that links to HomeScene.'''
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
        
        self.btn_login = ctk.CTkButton(self._frame_main, width=200, height=50, text="Start Surfing", command=self.on_button_click)
        self.btn_login.pack(expand=True)
    
    def on_button_click(self):
        '''Verify login details and switch to HomeScene.'''
        username = self.ent_username.get()
        password = self.ent_pw.get()
        #debug
        print(username, password)
        #####need to add verification before this
        self.master._switch_ui(HomeScene)

class HomeScene(Scene):
    def __init__(self, master):
        super().__init__(master)
    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        for i in range(4):
            ctk.CTkLabel(self._frame_main, text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:").pack()