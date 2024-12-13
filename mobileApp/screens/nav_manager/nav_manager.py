import os

from kivy.uix.screenmanager import ScreenManager, ScreenManagerException
from kivy_reloader.utils import load_kv_path

class NavManager(ScreenManager):
    def __init__(self,*args,**kwargs):
        self._navigation_stack = list()
        self.session_data = dict()
        super().__init__(*args,**kwargs)
        
    def navigate_to(self, screen_name:str, specific_screen_data : tuple[str,]|None = None):
        if not self.has_screen(screen_name):
            raise ScreenManagerException(f"no screen named {screen_name}")
        print("Navigating from:",self.current_screen.name)
        self._navigation_stack.append(self.current)
        self.current = screen_name
        print("Navigating to:",self.current_screen.name)
        print("Saved previous as:",self._navigation_stack[-1])
        if specific_screen_data is not None:
            self.session_data[specific_screen_data[0]] = specific_screen_data[1]
    def back_out(self, remove_key: str|None = None):
        print("Backing out from:",self.current)
        previous = self._navigation_stack.pop()
        print("Backing out to:",previous)
        if self.current == previous:
            self.current = "MainScreen"
        else:
            self.current = previous
        if remove_key is not None:
            self.session_data.pop(remove_key)


manager_screen_kv = os.path.join("mobileApp", "screens","nav_manager", "nav_manager.kv")
load_kv_path(manager_screen_kv)
