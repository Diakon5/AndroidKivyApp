import trio

from mobileApp import app
from kivy.core.window import Window
from sys import platform

if platform == "linux":
    Window.size = (360, 360*18/9)

trio.run(app.async_run, "trio")