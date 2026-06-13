import customtkinter as ctk
import scene
import utils

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")


class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        # Scene Ids
        self.NONE = -1
        self.WELCOME = 0
        self.LOGIN = 1
        self.HOME = 2
        self.VIEW = 3
        self.SUBSCRIBE = 5

        # managers
        self.account_manager = utils.AccountManager()
        self.account_manager.load_csv()
        self.log_manager = utils.LogManager(self.account_manager)
        self.media_manager = utils.MediaManager()

        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self.current_scene = self.NONE

        self.scenes: dict[int, scene.Scene] = {
            self.LOGIN: scene.LoginScene(self, self.account_manager),
            self.HOME: scene.HomeScene(self, self.log_manager, self.media_manager),
        }

        self.cached_scenes = []
        # scenes that have been loaded in that can be simply reloaded with pack() or grid() instead
        # of instantiating a new object
        self.switch_scene(self.LOGIN)

    def switch_scene(self, scene_id):
        # currentrly scene must use pack
        # extra logic for grid can be added later
        #
        if self.current_scene != self.NONE:
            self.scenes[self.current_scene].destroy()
        self.scenes[scene_id].build_frame()
        self.scenes[scene_id].pack()
        self.current_scene = scene_id


if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()
