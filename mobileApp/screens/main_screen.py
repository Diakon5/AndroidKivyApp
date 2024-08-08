import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path


class MainScreen(Screen):
    def on_enter(self, *args):
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens", "main_screen.kv")
load_kv_path(main_screen_kv)
