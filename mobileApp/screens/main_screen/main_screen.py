import os
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ListProperty
from kivy_reloader.utils import load_kv_path


class MainScreen(Screen):
    vehicleListScroll = ObjectProperty(None)
    rows = ListProperty([("id","name")])
    def addNewCar(self):
        pass
    def on_enter(self, *args):
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
