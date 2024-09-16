from kivy_reloader.app import App


class MainApp(App):
    def build(self):
        from .screens.dashboard_screen.dashboard_screen import DashboardScreen
        from .screens.main_screen.main_screen import MainScreen
        from .screens.main_manager.main_manager import MainManager
        return MainManager()

app = MainApp()