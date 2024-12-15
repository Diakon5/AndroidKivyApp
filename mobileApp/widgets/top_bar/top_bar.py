import os
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from mobileApp import MainApp
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty
from kivy_reloader.utils import load_kv_path
from kivy.app import App
import traceback

class TopBar(BoxLayout):
    current_screen_key = StringProperty(None)
    def relay_to_manager(self):
        try:
            app : MainApp = App.get_running_app() 
            app.root.back_out()
        except Exception as e:
            print("Exception:", e.args,traceback.format_exception(e))
            


top_bar_kv = os.path.join("mobileApp", "widgets","top_bar", "top_bar.kv")
load_kv_path(top_bar_kv)