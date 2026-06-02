import customtkinter as ctk
import tkinter as tk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self._build_ui()

    def _build_ui(self):
        self._build_header()
        self._build_main()
    
    def _build_header(self):
        pass

    def _build_main(self):
        """Blank usually, just for child classes to inherit and make different"""
        pass
        #old comments probably good to preserve for documentation
        # add: build main frame - frame.build - each subclass has a different build func ig
        # generic scene -> specific scene which inherits from generic and then polymorphism on build_main()

    
if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()
