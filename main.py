import trio

from mobileApp import app

trio.run(app.async_run, "trio")