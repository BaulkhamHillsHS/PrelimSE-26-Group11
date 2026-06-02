import customtkinter as ctk
import tkinter as tk

# just for clarity
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("dark-blue")

class StreamingApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("WIP Streaming App Jeremy Guillermo")
        self.geometry("720x540")
        self._build_ui()

    def _build_ui(self):
        pass
    
if __name__ == "__main__":
    app = StreamingApp()
    app.mainloop()
