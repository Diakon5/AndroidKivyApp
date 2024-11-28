import os

from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy_reloader.utils import load_kv_path


class MainScreen(Screen):
    vehicleListScroll = ObjectProperty(None)
    def on_enter(self, *args):
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
