from kivy_reloader.app import App
from .screens.main_manager import MainManager


class MainApp(App):
    def build(self):
        return MainManager()