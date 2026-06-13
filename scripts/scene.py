import customtkinter as ctk
from PIL import Image

import data


class Navbar(ctk.CTkFrame):
    """Navigation bar containing buttons with links to different scenes."""

    def __init__(self, master, stream_app):
        super().__init__(master)
        self.stream_app = stream_app
        self.btn_logout = ctk.CTkButton(self, text="Log Out", command=self.click_logout)
        self.btn_logout.grid(row=0, column=0)
        self.btn_home = ctk.CTkButton(self, text="Home", command=self.click_home)
        self.btn_home.grid(row=0, column=1)

    # yes, these are hardcoded. don't ask me how long I wasted trying to avoid this
    def click_logout(self):
        # Navbar runs command, master-> _frame_header, master->Scene subclass, master->StreamingApp
        self.stream_app._switch_ui(LoginScene)

    def click_home(self):
        self.stream_app._switch_ui(HomeScene)


class Scene(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(width=540, height=720)

    def build_frame(self):
        self._build_header()
        self._build_main()

    def _build_header(self):
        """Build the logo and navigation bar at the top of the screen that is in most scenes in the app."""
        # add frame and configure grid inside frame
        self._frame_header = ctk.CTkFrame(self, width=400, height=200)
        self._frame_header.pack(fill=ctk.X)
        self._frame_header.rowconfigure(0, weight=1)
        self._frame_header.columnconfigure((0, 1, 2), weight=1)

        # load image and display logo label containing image
        self.img_logo = ctk.CTkImage(
            light_image=Image.open("data/images/Gex2Cover.jpg"), size=(80, 80)
        )
        # text=' ' (single space) to not display default 'CTkLabel' text on label
        self.lbl_logo = ctk.CTkLabel(self._frame_header, text=" ", image=self.img_logo)
        self.lbl_logo.grid(row=0, column=0)

        self.lbl_title = ctk.CTkLabel(
            self._frame_header, text="GEx VIDEos", font=("Comic Sans MS", 20)
        )
        self.lbl_title.grid(row=0, column=1, sticky="w")

        # the navbar and its button elements which link to other scenes
        self.navbar = Navbar(self._frame_header, self.master)
        self.navbar.grid(row=0, column=2)

    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different."""
        pass
        # old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()


class LoginScene(Scene):
    def __init__(self, master, account_manager):
        self.streaming_app = master
        self.account_manager = account_manager
        super().__init__(master)

    def _build_header(self):
        """Redefined to empty for the login scene, as the user should not have access to the app functions before logging in."""
        pass

    def _build_main(self):
        """Build a simple username and password form with a title and a button that links to HomeScene."""
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


class AccountScene(Scene):
    def __init__(self, master, account_manager):
        self.streaming_app = master
        self.account_manager = account_manager
        super().__init__(master)

    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        account = self.account_manager.current_account
        for i in range(len()):
            ctk.CTkLabel(
                self._frame_main,
                text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:",
            ).pack()
            ctk.CTkButton(
                self._frame_main,
                text=self.media_manager.media_list[i].title,
                command=lambda media=self.media_manager.media_list[i]: (
                    self.media_clicked(media)
                ),
            ).pack()

    def media_clicked(self, media):
        self.log_manager.add_viewing_activity(media)


class HomeScene(Scene):
    def __init__(self, master, log_manager, media_manager):
        self.log_manager = log_manager
        self.media_manager = media_manager
        super().__init__(master)

    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        for i in range(len(self.media_manager.media_list)):
            ctk.CTkLabel(
                self._frame_main,
                text=f"{i}\nthumbnail\nTitle:\nMovie/TV Show:\nLength:\nRating:\nGenre:",
            ).pack()
            ctk.CTkButton(
                self._frame_main,
                text=self.media_manager.media_list[i].title,
                # lambda so the the command can pass a parameter
                command=lambda media=self.media_manager.media_list[i]: (
                    self.media_clicked(media)
                ),
            ).pack()

    def media_clicked(self, media):
        self.log_manager.add_viewing_activity(media)
        # switch to viewing scene(media)
