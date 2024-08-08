import os

from kivy.uix.screenmanager import ScreenManager

from kivy_reloader.utils import load_kv_path
from .main_screen import *

main_screen_kv = os.path.join("mobileApp", "screens", "main_manager.kv")
load_kv_path(main_screen_kv)


class MainManager(ScreenManager):
    pass