import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from ...budgetAssistantApp import MainApp
from kivy.properties import ListProperty, BooleanProperty
from kivy.uix.screenmanager import Screen
from kivy.app import App
from kivy_reloader.utils import load_kv_path


class DocumentsScreen(Screen):
    db_ready = BooleanProperty(None)
    rows = ListProperty([("id","default1","default2","default3")])
    async def list_documents(self, dt=0): ##To future self: ALWAYS TRY EXCEPT YOUR CALLS MORON
        try:
            print("TRYING TO LIST")
            app : MainApp = App.get_running_app() 
            output = await app.db_read_single_table("documents","*")
            self.rows = output
            print(self.rows)
            print("CONNECTED")
        except Exception as e:
            print("Exception", e.args)
    def on_enter(self, *args):
        app : MainApp = App.get_running_app()
        if self.db_ready:
            app.nursery.start_soon(self.list_cars)
        print("DocumentsScreen on_enter")

documents_screen_kv = os.path.join("mobileApp", "screens","documents_screen", "documents_screen.kv")
load_kv_path(documents_screen_kv)