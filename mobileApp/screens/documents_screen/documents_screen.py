import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path


class DocumentsScreen(Screen):
    def on_enter(self, *args):
        print("DocumentsScreen on_enter")

documents_screen_kv = os.path.join("mobileApp", "screens","documents_screen", "documents_screen.kv")
load_kv_path(documents_screen_kv)