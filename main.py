import customtkinter as ctk
from PIL import Image
import data

class rating():
    G = 0
    PG = 1
    M = 2
    MA = 3
    R = 4
    X = 5

class media():
    def __init__(self, video_id) -> None:
        media = data.media[video_id]
        display_path =
        thumbnail = None
        length_sec : int
        rating : int
