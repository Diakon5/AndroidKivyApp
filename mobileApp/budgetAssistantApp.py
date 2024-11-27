from kivy_reloader.app import App
from .screens.main_manager import MainManager
import aiosqlite


class MainApp(App):
    def db_init(self):
        pass
    def db_read(self):
        pass
    def db_write(self):
        pass
    def db_edit(self):
        pass
    def db_remove(self):
        pass
    def build(self):
        return MainManager()