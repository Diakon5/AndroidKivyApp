import trio

from mobileApp import MainApp

from kivy.utils import platform

if platform == "linux":
    from kivy.core.window import Window
    Window.size = (360, 360*18/9)

app = MainApp()
trio.run(app.async_run, "trio")