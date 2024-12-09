from kivy_reloader.app import App
#from kivy.base import async_runTouchApp
#from kivy.app import App
#import trio
from .screens.main_manager import MainManager
from kivy.utils import platform
from kivy.properties import BooleanProperty
from kivy.cache import Clock
import anysqlite as sqlite
from functools import partial
from os import getcwd
from os.path import join
from .db_schema import schema_version, schema_sql

class MainApp(App):

    db_ready = BooleanProperty(False)
    # async def async_run(self, async_lib="trio"):
    #     async with trio.open_nursery() as nursery:
    #         print("pre nursery")
    #         self.nursery = nursery
    #         print("post nursery")
    #         self._run_prepare()
    #         await async_runTouchApp(async_lib=async_lib)
    #         self._stop()
    #         nursery.cancel_scope.cancel()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.internal_storage_path = join(getcwd(),"debugStorage")
        if platform == "android":
            from android.storage import app_storage_path # type: ignore
            from android import mActivity # type: ignore
            context = mActivity.getApplicationContext()
            result =  context.getExternalFilesDir(None)   # don't forget the argument
            if result:
                self.internal_storage_path = str(result.toString())
            else:
                self.internal_storage_path = app_storage_path()

    async def db_open(self,dt=0):
        print("OPENING DATABASE")
        self.conn = await sqlite.connect(join(self.internal_storage_path,"storage.sqlite"))
        print("DATABASE IS OPEN")
        try:
            cursor = await self.conn.cursor()
            await cursor.execute("SELECT name FROM sqlite_schema WHERE name='schema_meta'")
            meta = await cursor.fetchone()
            if meta == None:
                await self.db_init()
                return
            await cursor.execute("SELECT version FROM schema_meta;")
            version = await cursor.fetchone()
            if version[0] != schema_version:
                #include schema updating code later
                pass
            self.db_ready = True
        except sqlite.OperationalError as e:
            print("Sqlite Error:", e.sqlite_errorname)
        except Exception as e:
            print("unknown error:", e.args)
        finally:
            await cursor.close()

    async def db_init(self,dt=0):
        cursor = await self.conn.cursor()
        command = str.join(";",schema_sql)
        await cursor.executescript(f"BEGIN;{command};COMMIT;") #This isn't recommended but the schema_sql has no user input, so it should be fine
        await cursor.executescript("BEGIN;INSERT INTO schema_meta VALUES (1);COMMIT;")
        await cursor.close()

    async def db_read_single_table(self, table : str, columns: str, filter: str = "1=1"):
        cursor = await self.conn.cursor()
        await cursor.execute(f"SELECT {columns} FROM {table} WHERE ?",(filter,))
        values = await cursor.fetchall()
        return values
    async def db_write(self, table: str, values: tuple[dict[str,str]]):
        cursor = await self.conn.cursor()
        first_dict: set = values[0].keys()
        columns = str.join(", ",first_dict)
        params = str.join(", ",[f":{x}" for x in first_dict])
        print(columns, params)
        #values = self.sanitize(values)
        await cursor.executemany(f"INSERT INTO {table} ({columns}) VALUES ({params});", values)
        await cursor.execute("COMMIT;") #

        await cursor.close()

    async def db_edit(self):
        pass

    async def db_remove(self):
        pass

    def build(self):
        Clock.schedule_once(partial(self.nursery.start_soon,self.db_open))
        print("app_build")
        return MainManager()