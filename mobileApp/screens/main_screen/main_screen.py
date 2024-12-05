from typing import TYPE_CHECKING

import kivy.properties

if TYPE_CHECKING:
    from ...budgetAssistantApp import MainApp
import os
import kivy
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy_reloader.utils import load_kv_path
from kivy.app import App

class MainScreen(Screen):
    rows = ListProperty([("id","Loading Data, please wait")])
    async def listCars(self, dt=0): ##To future self: ALWAYS TRY EXCEPT YOUR CALLS MORON
        try:
            print("TRYING TO LIST")
            app : MainApp = App.get_running_app() 
            output = await app.db_read_single_table("managed_vehicles_list","*")
            self.rows = output
            print(self.rows)
            print("CONNECTED")
        except Exception as e:
            print("Exception", e.args)
    async def add_new_car(self,dt=0):
        print("TRYING TO ADD")
        app : MainApp = App.get_running_app() 
        try:
            
            self.rows.append(("*","Car1"))
            await app.db_write("managed_vehicles_list",({"vehicle_display_name":"Car1"}))
        except Exception as e:
            print(e.args)
    def on_enter(self, *args):
        app : MainApp = App.get_running_app()
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
