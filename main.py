import trio

from mobileApp import MainApp
from kivy.core.window import Window
from sys import platform

if platform == "linux":
    Window.size = (360, 360*18/9)

app = MainApp()
trio.run(app.async_run, "trio")