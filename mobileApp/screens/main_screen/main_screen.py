from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...budgetAssistantApp import MainApp

import os
from kivy.factory import Factory
from kivy.uix.screenmanager import Screen
from kivy.properties import ListProperty
from kivy_reloader.utils import load_kv_path
from kivy.app import App
from kivy.cache import Clock
from functools import partial

class MainScreen(Screen):
    rows = ListProperty([("id","name")])
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
    def on_enter(self, *args):
        
        app = App.get_running_app()
        print(type(app))
        print(type(app.nursery))
        Clock.schedule_once(partial(app.nursery.start_soon,self.listCars))
        print("MainScreen on_enter")

main_screen_kv = os.path.join("mobileApp", "screens","main_screen", "main_screen.kv")
load_kv_path(main_screen_kv)
