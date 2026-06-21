import customtkinter as ctk
import tkinter as tk
import scene
import utils

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("green")


class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Scene Ids
        self.NONE = -1
        self.LOGIN = 1
        self.PROFILE = 2
        self.ACCOUNT = 3
        self.HOME = 4
        self.VIEW = 5
        self.SUBSCRIBE = 6

        # managers
        self.account_manager = utils.AccountManager()
        self.account_manager.load_csv()
        self.logger = utils.Logger(self.account_manager)
        self.library = utils.Library(self.account_manager)

        self.title("GEX VIDEOS Streaming App Jeremy Guillermo")
        self.geometry("1280x720")
        self.resizable(False, False)
        self.current_scene = self.NONE

        self.scenes: dict[int, scene.Scene] = {
            self.LOGIN: scene.LoginScene(self, self.account_manager),
            self.HOME: scene.HomeScene(self, self.logger, self.library,self.account_manager),
            self.PROFILE: scene.OpeningProfileScene(self, self.account_manager),
            self.VIEW: scene.ViewMediaScene(self, self.library),
            self.ACCOUNT: scene.AccountScene(self, self.account_manager, self.logger)
        }

        self.cached_scenes = []
        self.switch_scene(self.LOGIN)

    # basically just a state machine
    def switch_scene(self, new_id):
        # currently scenes must use pack() to build
        # unload and hide previous scene - but it still exists and is in cached list
        prev_id = self.current_scene
        if prev_id != self.NONE:
            self.scenes[prev_id].exit_scene()
            self.scenes[prev_id].pack_forget()
        # if a new scene, build it and add to cached list
        if new_id not in self.cached_scenes:
            self.cached_scenes.append(new_id)
            self.scenes[new_id].build_frame()
        # prepare scene and display it in the window
        self.scenes[new_id].enter_scene()
        self.scenes[new_id].pack(expand=True, fill=ctk.BOTH)
        self.current_scene = new_id

    def exit_app(self):
         if tk.messagebox.askyesno("Confirm", "Exit GexVideos?"):
            app.account_manager.save_csv()
            self.destroy()


if __name__ == "__main__":
    app = StreamingApp()
    app.protocol("WM_DELETE_WINDOW", app.exit_app)
    app.mainloop()
    
    



