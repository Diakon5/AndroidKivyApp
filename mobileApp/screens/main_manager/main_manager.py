import os

from kivy.uix.screenmanager import ScreenManager
from kivy_reloader.utils import load_kv_path


class MainManager(ScreenManager):
    pass


manager_screen_kv = os.path.join("mobileApp", "screens","main_manager", "main_manager.kv")
load_kv_path(manager_screen_kv)
