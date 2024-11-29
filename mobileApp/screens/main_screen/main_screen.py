from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...budgetAssistantApp import MainApp

import os
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.metrics import dp
from kivy.properties import ObjectProperty, ListProperty
from kivy_reloader.utils import load_kv_path
from kivy.app import App



class MainScreen(Screen):
    vehicleListScroll = ObjectProperty(None)
    rows = ListProperty([("id","name")])
    async def addNewCar(self): ##To future self: ALWAYS TRY EXCEPT YOUR CALLS MORON
        try:
            app : MainApp = App.get_running_app() 
            output = await app.db_read_single_table("managed_vehicles_list","*")
            self.rows = output
            print(self.rows)
            print("CONNECTED")
        except Exception as e:
            print("Exception", e.args)
    def on_enter(self, *args):
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
