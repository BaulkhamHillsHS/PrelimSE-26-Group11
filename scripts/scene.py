import customtkinter as ctk
import tkinter as tk
from PIL import Image
from utils import *


#placed at the top of every scenes
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


        # buttons to swtich to home and accounts
        # conditional to prevent errors entering scenes without an account
        if build_navbar:
            self.navbar = ctk.CTkFrame(self, width=200, height=100)

            self.btn_home = ctk.CTkButton(self.navbar, width=70, text="Home", command=self.click_home)
            self.btn_home.grid(row=0, column=0, padx=4)
            self.btn_profiles = ctk.CTkButton(self.navbar, width=70, text="Account", command=self.click_account)
            self.btn_profiles.grid(row=0, column=1, padx=4)
            self.navbar.grid(row=0, column=2, sticky="e")



    def click_home(self):
        self.app.switch_scene(self.app.HOME)

    def click_account(self):
        self.app.switch_scene(self.app.ACCOUNT)




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
    
    # called separatedly from enter_scene as forget_pack handles cached scenes
    def build_frame(self):
        self._build_header()
        self._build_main()

    def _build_header(self):
        self._frame_header = Header(self, self.app)
        self._frame_header.pack(fill=ctk.X)

    def _build_main(self):
        pass



class LoginScene(Scene):
    def __init__(self, master, account_manager : AccountManager):
        self.acc_man : AccountManager = account_manager
        super().__init__(master)


    def _build_header(self):
        self._frame_header = Header(self, self.app, False)
        self._frame_header.pack(fill=ctk.X)

    def _build_main(self):
        #Build a simple username and password form with a title and a button that links to HomeScene
        self._frame_main = ctk.CTkFrame(self, width=400, height=400)
        self._frame_main.pack(expand=True)

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
            text="Enter the Media Dimension",
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
        # deletes previously entered entry
        self.lbl_error.configure(text = "")
        self.ent_username.delete(0,"end")
        self.ent_pw.delete(0,"end")


# initial profile selection after login
class OpeningProfileScene(Scene):
    def __init__(self, master, account_manager):
        self.acc_man = account_manager
        self.prev_account = None
        super().__init__(master)

    # resets scene if there is a new account
    def enter_scene(self):
        if self.acc_man.get_current_index() != self.prev_account:
            self._frame_main.destroy()
            self._build_main()

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


# scene holding all the info relevant to account management
class AccountScene(Scene):
    def __init__(self, master, account_manager, loggerager):
        self.acc_man : AccountManager = account_manager
        self.logger : Logger = loggerager
        self.profile_buttons = []
        self.plan_buttons = []
        self.prev_account = None
        self._frame_main = None
        super().__init__(master)

    # resets scene if there is a new account
    def enter_scene(self):
        if self.acc_man.get_current_index() != self.prev_account:
            self._frame_main.destroy()
            self._build_main()

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

        # logout
        self.btn_logout = ctk.CTkButton(self._frame_main, width=70, text="Log Out", command=self.click_logout).pack()

    def media_clicked(self, profile):
        self.acc_man.set_profile(profile)
        self._frame_main.destroy()
        self._build_main()        

    def plan_clicked(self, plan):
        if tk.messagebox.askyesno("Confirm", f"Switch to {data.plans[plan]["name"]} Plan?"):
            self.logger.add_subscription_activity(self.acc_man.current_account.get("plan"), plan)
            self.acc_man.current_account.set_plan(plan)
            self._frame_main.destroy()
            self._build_main()

    def click_logout(self):
        if tk.messagebox.askyesno("Confirm", f"Logout of {self.acc_man.current_account.get("username")}?"):
            self.app.switch_scene(self.app.LOGIN)


# displays a grid of all thumbnails
class HomeScene(Scene):
    def __init__(self, master, logger, media_manager, account_manager):
        self.logger : Logger = logger
        self.library : Library = media_manager
        self.acc_man : AccountManager = account_manager
        super().__init__(master)
        self._frame_main = ctk.CTkFrame(self, width=1280, height=720)
        self._scroll_frame = ctk.CTkScrollableFrame(self._frame_main, width=1280, height=720)
        self._list_frame = None
        

    def enter_scene(self):
        if self.acc_man.current_account != None:
            self.library.ratings_filter = self.acc_man.get_active_profile().get("age")
            self.library.update_visible()
            self._build_list()
        else:
            raise ValueError("Entered homescene without an account")
        
    def _build_list(self):
        if self._list_frame:
            self._list_frame.destroy() # to reset the frame
        self._list_frame = ctk.CTkFrame(self._scroll_frame, width=1008, height=500)

        card_count = 0
        ctk.CTkLabel(self._list_frame, text="test")
        for index in self.library.visible_list:
            # In the future adding a way to cache cards or image lables would help
            # optimise loading speed

            # loading the thumbnails asynchronously would also get rid of the long stall
            # when building the scene
            media_card = ctk.CTkFrame(self._list_frame, width=336, height=240)
            media_card.grid(row = card_count//3, column = card_count % 3)

            # watch button
            ctk.CTkButton(
                media_card,
                text="",
                image=self.library.media_list[index].thumbnail, 
                fg_color="transparent",
                bg_color="transparent",
                # lambda so the the command can pass a parameter
                command=lambda media_index=index: self.media_clicked(media_index),
            ).pack()

            # add/remove watchlist
            checked_state = ctk.IntVar(value=0)
            if index in self.acc_man.get_active_profile().get("watchlist"):
                checked_state = ctk.IntVar(value=1)
            ctk.CTkCheckBox(media_card, text="Watchlist", variable=checked_state, 
                command=lambda media_index=index: self.watchlist_clicked(media_index)).pack()
                
            # media description
            genres = []
            for genre in self.library.media_list[index].genre:
                genres.append(data.genres[genre])
            text = f"""\
{self.library.media_list[index].title}
{self.library.media_list[index].rating} or above only
{', '.join(genres)}"""
            
            ctk.CTkLabel(media_card,text=text,).pack()
            card_count += 1
        self._list_frame.pack()


    def _build_main(self):
        # currently builds a pack of labels with different metadata
        
        self._frame_main.pack()

        self._filter_frame = ctk.CTkFrame(self._frame_main, width=400, height=200)
        self._filter_frame.pack()

        self._watchlist_switch = ctk.CTkSwitch(self._filter_frame, text="Watchlist",
            command=self.watchlist_switched).grid(row=0, column=0)

        self._genre_filter = ctk.CTkComboBox(self._filter_frame, values=["Filter by Catagory"] + data.genre_list,
            command=self.category_combo).grid(row=0, column=1)
        
        self._scroll_frame.pack()
        

    def media_clicked(self, media_id):
        # watches media in viewpage
        self.logger.add_viewing_activity(self.library.media_list[media_id])
        self.library.current_viewed = media_id
        self.acc_man.get_active_profile().append_history(media_id)
        # removed from watchlist if in watchlist
        if media_id in self.acc_man.get_active_profile().get("watchlist"):
            index = self.acc_man.get_active_profile().get("watchlist").index(media_id)
            self.acc_man.get_active_profile().watchlist.pop(index)
        self.app.switch_scene(self.app.VIEW)

    def watchlist_clicked(self, media_id):
        # toggles profile watchlist bool for this media
        if media_id not in self.acc_man.get_active_profile().get("watchlist"):
            self.acc_man.get_active_profile().watchlist.append(media_id)
        else:
            index = self.acc_man.get_active_profile().get("watchlist").index(media_id)
            self.acc_man.get_active_profile().watchlist.pop(index)
            if self.library.is_watchlist:
                self.library.update_visible()
                self._build_list()

    def category_combo(self, value):
        # updates genre filter
        if value == "Filter by Catagory":
            self.library.genre_filter = None
        else:
            self.library.genre_filter = data.genre_list.index(value)
        self.library.update_visible()
        self._build_list()

    def watchlist_switched(self):
        # toggles watchlist state
        self.library.is_watchlist = not self.library.is_watchlist
        self.library.update_visible()
        self._build_list()



class ViewMediaScene(Scene):
    def __init__(self, master, media_manager):
        self.library : Library = media_manager
        self._frame_main = None
        super().__init__(master)

    def enter_scene(self):
        self.build_main()

    def build_main(self):
        if self._frame_main:
            self._frame_main.destroy() # to reset the frame
        self._frame_main = ctk.CTkFrame(self, width=400, height=200)
        self._frame_main.pack()
        if self.library.media_list[self.library.current_viewed].type == data.MOVIE:
            self._build_movie()
        else:
            self._build_show()

    def _build_movie(self):
        # Image in place of video
        ctk.CTkLabel(
                self._frame_main,
                text="",
                image=self.library.media_list[self.library.current_viewed].display,
            ).pack()
        #title
        ctk.CTkLabel(self._frame_main, text=self.library.media_list[self.library.current_viewed].title).pack()

    def _build_show(self):
        # Image in place of episode 1
        ctk.CTkLabel(
                self._frame_main,
                text="",
                image=self.library.media_list[self.library.current_viewed].display_list[0],
            ).pack()
        #title
        ctk.CTkLabel(self._frame_main, text=self.library.media_list[self.library.current_viewed].title).pack()

