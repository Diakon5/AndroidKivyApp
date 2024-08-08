from kivy_reloader.app import App


class MainApp(App):
    def build(self):

        from .screens.main_manager import MainManager
        return MainManager()

app = MainApp()