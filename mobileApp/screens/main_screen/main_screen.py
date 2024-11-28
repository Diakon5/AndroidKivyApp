import os
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import ObjectProperty
from kivy_reloader.utils import load_kv_path


class MainScreen(Screen):
    vehicleListScroll = ObjectProperty(None)

    def addNewCar(self):
        row = Factory.Button()
        self.vehicleListScroll.add_widget(row)
    def on_enter(self, *args):
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
