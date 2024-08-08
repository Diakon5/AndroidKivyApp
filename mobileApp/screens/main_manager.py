import os

from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy_reloader.utils import load_kv_path
from .main_screen import *


class MainManager(ScreenManager):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


manager_screen_kv = os.path.join("mobileApp", "screens", "main_manager.kv")
load_kv_path(manager_screen_kv)
