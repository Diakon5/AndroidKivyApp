import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path


class ExpensesScreen(Screen):
    def on_enter(self, *args):
        print("ExpensesScreen on_enter")

expenses_screen_kv = os.path.join("mobileApp", "screens","expenses_screen", "expenses_screen.kv")
load_kv_path(expenses_screen_kv)