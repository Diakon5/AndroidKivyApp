import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path


class DashboardScreen(Screen):
    def on_enter(self, *args):
        print("DashboardScreen on_enter")

dashboard_screen_kv = os.path.join("mobileApp", "screens","dashboard_screen", "dashboard_screen.kv")
load_kv_path(dashboard_screen_kv)
