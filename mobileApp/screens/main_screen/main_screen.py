from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mobileApp import MainApp
import os
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty, BooleanProperty
from kivy_reloader.utils import load_kv_path
from kivy.app import App

class MainScreen(Screen):
    db_ready = BooleanProperty(None)
    rows = ListProperty([("id","Loading Data, please wait")])
    async def list_cars(self, dt=0): ##To future self: ALWAYS TRY EXCEPT YOUR CALLS MORON
        try:
            print("TRYING TO LIST")
            app : MainApp = App.get_running_app() 
            output = await app.db_read_single_table("managed_vehicles_list","*")
            self.rows = output
            print(self.rows)
            print("CONNECTED")
        except Exception as e:
            print("Exception", e.args)
    def on_enter(self, *args):
        app : MainApp = App.get_running_app()
        if self.db_ready:
            app.nursery.start_soon(self.list_cars)
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
