import os

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...budgetAssistantApp import MainApp
from kivy.uix.screenmanager import Screen
from ...comps.filteredTextInput import FilteredTextInput
from kivy_reloader.utils import load_kv_path
from kivy.app import App

class AddVehicleScreen(Screen):
    async def add_new_car(self,raw_input: str ,dt=0 ):
        print("TRYING TO ADD")
        app : MainApp = App.get_running_app() 
        try:
            await app.db_write("managed_vehicles_list",({"vehicle_display_name":raw_input},))
            app.root.current = "MainScreen"
        except Exception as e:
            print("Exception", e.args)
            

    def on_enter(self, *args):
        print("AddVehicleScreen on_enter")

add_vehicle_screen = os.path.join("mobileApp", "screens","add_vehicle_screen", "add_vehicle_screen.kv")
load_kv_path(add_vehicle_screen)