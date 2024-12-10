import os

from kivy.uix.screenmanager import Screen

from kivy_reloader.utils import load_kv_path

class AddVehicleScreen(Screen):
    def on_enter(self, *args):
        print("AddVehicleScreen on_enter")

add_vehicle_screen = os.path.join("mobileApp", "screens","add_vehicle_screen", "add_vehicle_screen.kv")
load_kv_path(add_vehicle_screen)