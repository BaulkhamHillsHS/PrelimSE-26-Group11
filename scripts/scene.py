import customtkinter as ctk
import tkinter as tk
from PIL import Image
from utils import *

class Navbar(ctk.CTkFrame):
    """Navigation bar containing buttons with links to different scenes."""

    def __init__(self, master, stream_app):
        super().__init__(master)
        self.stream_app = stream_app
        self.btn_home = ctk.CTkButton(self, width=70, text="Home", command=self.click_home)
        self.btn_home.grid(row=0, column=0, padx=4)
        self.btn_profiles = ctk.CTkButton(self, width=70, text="Account", command=self.click_account)
        self.btn_profiles.grid(row=0, column=1, padx=4)

    # yes, these are hardcoded. don't ask me how long I wasted trying to avoid this
    

    def click_home(self):
        self.stream_app.switch_scene(self.stream_app.HOME)
        
    def click_profiles(self):
        self.stream_app.switch_scene(self.stream_app.PROFILE)

    def click_account(self):
        self.stream_app.switch_scene(self.stream_app.ACCOUNT)

class FilterBar(ctk.CTkFrame):
    def __init__(self, master, genres: list[str]=["gex", "the", "gecko"]):
        super().__init__(master)
        ctk.CTkLabel(self, text="Filter by:").grid(row=0, column=0, padx=20)
        # by default will be set to "all" upon creation
        # all is created by the method and does not have to be passed in in the list of genres
        self.radio_var = tk.IntVar(value=0)
        genres.insert(0, "all")
        for i in range(len(genres)):
            radio = ctk.CTkRadioButton(self,text=genres[i], variable=self.radio_var, value=i, command=self.radio_clicked)
            radio.grid(row=0, column=i+1)
    
    def radio_clicked(self):
        ##### add updating of the filters/visible media cards etc.
        # radio_var.get() carries the int value of the genre (the int value of the radio button)
        print(self.radio_var.get())
        

class Header(ctk.CTkFrame):
    def __init__(self, scene, app, build_navbar = True):
        super().__init__(master=scene)
        self.app = app
        self.configure(width=400, height=200)
        self.rowconfigure(0, weight=1)
        self.columnconfigure((0,1,2,3), weight=1)
        
        # load image and display logo label containing image
        # text=' ' (single space) to not display default 'CTkLabel' text on label
        self.lbl_logo = ctk.CTkLabel(self, text=" ", image=data.LOGO,width=80)
        self.lbl_logo.grid(row=0, column=0, sticky="w")



        if build_navbar:
            self.navbar = ctk.CTkFrame(self, width=200, height=100)

            self.btn_home = ctk.CTkButton(self.navbar, width=70, text="Home", command=self.click_home)
            self.btn_home.grid(row=0, column=0, padx=4)
            self.btn_profiles = ctk.CTkButton(self.navbar, width=70, text="Account", command=self.click_account)
            self.btn_profiles.grid(row=0, column=1, padx=4)
            self.navbar.grid(row=0, column=2, sticky="w")

        self.btn_home = ctk.CTkButton(self, width=70, text="Quit", command=self.quit_clicked)
        self.btn_home.grid(row=0, column=3, padx=4, sticky="e")

    def click_home(self):
        self.app.switch_scene(self.app.HOME)

    def click_account(self):
        self.app.switch_scene(self.app.ACCOUNT)

    def quit_clicked(self):
        # add a confirm
        self.app.exit_app()
# based on state design pattern
class Scene(ctk.CTkFrame):
    def __init__(self, app):
        super().__init__(master=app)
        self.app = app
        self.configure(width=540, height=720)

    def enter_scene(self):
        pass

    def exit_scene(self):
        pass

    def build_frame(self):
        self._build_header()
        self._build_main()

    def _build_header(self):
        """Build the logo and navigation bar at the top of the screen that is in most scenes in the app."""
        # add frame and configure grid inside frame
        self._frame_header = Header(self, self.app)
        self._frame_header.pack(fill=ctk.X)

    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different."""
        pass
        # old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()


class LoginScene(Scene):
    def __init__(self, master, account_manager : AccountManager):
        self.acc_man : AccountManager = account_manager
        super().__init__(master)


    def _build_header(self):
        self._frame_header = Header(self, self.app, False)
        self._frame_header.pack(fill=ctk.X)

    def _build_main(self):
        """Build a simple username and password form with a title and a button that links to HomeScene."""
        self._frame_main = ctk.CTkFrame(self, width=400, height=400)
        self._frame_main.pack(expand=True, fill=ctk.Y)

        # Username
        self.lbl_username = ctk.CTkLabel(self._frame_main, text="Enter Username:")
        self.lbl_username.pack(anchor=ctk.S)
        self.ent_username = ctk.CTkEntry(self._frame_main, placeholder_text="eg. Gex T. Gecko")
        self.ent_username.pack(expand=True)

        # Password
        self.lbl_pw = ctk.CTkLabel(self._frame_main, text="Enter Password:")
        self.lbl_pw.pack(anchor=ctk.S)
        self.ent_pw = ctk.CTkEntry(self._frame_main, placeholder_text="eg. its_tail_time", show="*")
        self.ent_pw.pack(expand=True)

        # login button
        self.btn_login = ctk.CTkButton(
            self._frame_main,
            width=200,
            height=50,
            text="Start Surfing",
            command=self.login_button_clicked,
        )
        self.btn_login.pack(expand=True)

        # error message
        self.lbl_error = ctk.CTkLabel(self._frame_main, text="", text_color="red")
        self.lbl_error.pack(expand=True)

    def login_button_clicked(self):
        login_status = self.acc_man.login(self.ent_username.get(), self.ent_pw.get())
        if login_status == self.acc_man.LOGIN_SUCCESS:
            self.app.switch_scene(self.app.PROFILE)
        if login_status == self.acc_man.LOGIN_USER_ERR:
            self.lbl_error.configure(text = "Invalid username")
        if login_status == self.acc_man.LOGIN_PASS_ERR:
            self.lbl_error.configure(text = "Invalid password")
    def enter_scene(self):
        self.lbl_error.configure(text = "")
        self.ent_username.delete(0,"end")
        self.ent_pw.delete(0,"end")


class OpeningProfileScene(Scene):
    def __init__(self, master, account_manager):
        self.acc_man = account_manager
        super().__init__(master)

    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        account = self.acc_man.current_account
        for i in range(len(account.get("profiles"))):
            ctk.CTkButton(
                self._frame_main,
                text=account.get("profiles")[i].get("name"),
                command=lambda profile=i: self.profile_clicked(profile),
            ).pack()

    def _build_header(self):
        self._frame_header = Header(self, self.app, False)
        self._frame_header.pack(fill=ctk.X)

    def profile_clicked(self, profile):
        self.acc_man.set_profile(profile)
        self.app.switch_scene(self.app.HOME)


class AccountScene(Scene):
    def __init__(self, master, account_manager, log_manager):
        self.acc_man : AccountManager = account_manager
        self.log_man : LogManager = log_manager
        self.profile_buttons = []
        self.plan_buttons = []
        super().__init__(master)

    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        account = self.acc_man.current_account

        self.lbl_account = ctk.CTkLabel(self._frame_main, text=account.get("username")).pack()
        #profile
        self.lbl_profiles = ctk.CTkLabel(self._frame_main, text="profiles").pack()
        #profile buttons
        for i in range(len(account.get("profiles"))):
            if account.get("profiles")[i] == self.acc_man.get_active_profile():
                ctk.CTkButton(
                self._frame_main,
                text=account.get("profiles")[i].get("name"),
                state="disabled"
                ).pack()
            else:
                ctk.CTkButton(
                    self._frame_main,
                    text=account.get("profiles")[i].get("name"),
                    command=lambda media=i: self.media_clicked(media),
                ).pack()
        #plans
        self.lbl_plan = ctk.CTkLabel(self._frame_main, text="plans").pack()
        for i in range(len(data.plans)):
            if account.get("plan") == i:
                ctk.CTkButton(
                self._frame_main,
                text=data.plans[i]["name"],
                command=lambda plan=i: self.plan_clicked(plan),
                state="disabled"
                ).pack()
            else:
                ctk.CTkButton(
                    self._frame_main,
                    text=data.plans[i]["name"],
                    command=lambda plan=i: self.plan_clicked(plan),
                ).pack()
        self.btn_logout = ctk.CTkButton(self._frame_main, width=70, text="Log Out", command=self.click_logout).pack()

    def media_clicked(self, profile):
        self.acc_man.set_profile(profile)
        self._frame_main.destroy()
        self._build_main()

        

    def plan_clicked(self, plan):
        if tk.messagebox.askyesno("Confirm", f"Switch to {data.plans[plan]["name"]} Plan?"):
            self.log_man.add_subscription_activity(self.acc_man.current_account.get("plan"), plan)
            self.acc_man.current_account.set_plan(plan)
            self._frame_main.destroy()
            self._build_main()
    def click_logout(self):
        if tk.messagebox.askyesno("Confirm", f"Logout of {self.acc_man.current_account.get("username")}?"):
            self.app.switch_scene(self.app.LOGIN)


class HomeScene(Scene):
    def __init__(self, master, log_manager, media_manager, account_manager):
        self.log_man = log_manager
        self.med_man : MediaManager = media_manager
        self.acc_man : AccountManager = account_manager
        super().__init__(master)
        self._list_frame = None
        

    def enter_scene(self):
        if self.acc_man.current_account != {}:
            self.med_man.ratings_filter = self.acc_man.get_active_profile().get("age")
            self.med_man.update_visible()
            self._build_list()
        else:
            raise ValueError("Entered homescene without an account")
        
    def _build_list(self):
        if self._list_frame:
            self._list_frame.destroy() # to reset the frame
        self._list_frame = ctk.CTkScrollableFrame(self._frame_main, width=380, height=700)
        for index in self.med_man.visible_list:

            # watch button
            ctk.CTkButton(
                self._list_frame,
                text="",
                image=self.med_man.media_list[index].thumbnail,
                # lambda so the the command can pass a parameter
                command=lambda media_index=index: self.media_clicked(media_index),
            ).pack()

            # add/remove watchlist
            checked_state = ctk.IntVar(value=0)
            if index in self.acc_man.get_active_profile().get("watchlist"):
                checked_state = ctk.IntVar(value=1)
            ctk.CTkCheckBox(self._list_frame, text="Watchlist", variable=checked_state, 
                command=lambda media_index=index: self.watchlist_clicked(media_index)).pack()
                

            genres = []
            for genre in self.med_man.media_list[index].genre:
                genres.append(data.genres[genre])

            text = f"""\
{self.med_man.media_list[index].title}
{self.med_man.media_list[index].rating} or above only
{', '.join(genres)}"""
            
            ctk.CTkLabel(self._list_frame,text=text,).pack()
        self._list_frame.pack()


    def _build_main(self):
        # currently builds a pack of labels with different metadata
        self._frame_main = ctk.CTkFrame(self, width=400, height=720)
        self._frame_main.pack()

        self._filter_frame = ctk.CTkFrame(self._frame_main, width=400, height=200)
        self._filter_frame.pack()

        self._watchlist_switch = ctk.CTkSwitch(self._filter_frame, text="Watchlist",
            command=self.watchlist_switched).grid(row=0, column=0)

        self._genre_filter = ctk.CTkComboBox(self._filter_frame, values=["Filter by Catagory"] + data.genre_list,
            command=self.category_combo).grid(row=0, column=1)
        self._build_list()
        

    def media_clicked(self, media_id):
        self.log_man.add_viewing_activity(self.med_man.media_list[media_id])
        self.med_man.current_viewed = media_id
        self.acc_man.get_active_profile().append_history(media_id)
        # removed from watchlist if in watchlist
        if media_id in self.acc_man.get_active_profile().get("watchlist"):
            index = self.acc_man.get_active_profile().get("watchlist").index(media_id)
            self.acc_man.get_active_profile().watchlist.pop(index)
        self.app.switch_scene(self.app.VIEW)

    def watchlist_clicked(self, media_id):
        if media_id not in self.acc_man.get_active_profile().get("watchlist"):
            self.acc_man.get_active_profile().watchlist.append(media_id)
        else:
            index = self.acc_man.get_active_profile().get("watchlist").index(media_id)
            self.acc_man.get_active_profile().watchlist.pop(index)


    
    def category_combo(self, value):
        if value == "Filter by Catagory":
            self.med_man.genre_filter = None
        else:
            self.med_man.genre_filter = data.genre_list.index(value)
        self.med_man.update_visible()
        self._build_list()

    def watchlist_switched(self):
        self.med_man.is_watchlist = not self.med_man.is_watchlist
        self.med_man.update_visible()
        self._build_list()



class ViewMediaScene(Scene):
    def __init__(self, master, media_manager):
        self.med_man : MediaManager = media_manager
        self._frame_main = None
        super().__init__(master)

    def enter_scene(self):
        self.build_main()

    def build_main(self):
        if self._frame_main:
            self._frame_main.destroy() # to reset the frame
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        if self.med_man.media_list[self.med_man.current_viewed].type == data.MOVIE:
            self._build_movie()
        else:
            self._build_show()

    def _build_movie(self):
        # currently builds a pack of labels with different metadata
        ctk.CTkLabel(
                self._frame_main,
                text="",
                image=self.med_man.media_list[self.med_man.current_viewed].display,
            ).pack()
        ctk.CTkLabel(self._frame_main, text=self.med_man.media_list[self.med_man.current_viewed].title).pack()

    def _build_show(self):
        # currently builds a pack of labels with different metadata
        ctk.CTkLabel(
                self._frame_main,
                text="",
                image=self.med_man.media_list[self.med_man.current_viewed].display_list[0],
            ).pack()
        ctk.CTkLabel(self._frame_main, text=self.med_man.media_list[self.med_man.current_viewed].title).pack()

