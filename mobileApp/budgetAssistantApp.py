from kivy_reloader.app import App
from .screens.main_manager import MainManager
from kivy.utils import platform
from kivy.cache import Clock
import aiosqlite as sqlite
from functools import partial
#import sqlite3 as sqlite
from os import getcwd
from os.path import join

class MainApp(App):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.internal_storage_path = join(getcwd(),"debugStorage")
        if platform == "android":
            from android.storage import app_storage_path # type: ignore
            self.internal_storage_path = app_storage_path()
    async def db_init(self,dt=0):
        print(join(self.internal_storage_path,"storage.sqlite"))
        self.conn = await sqlite.connect(join(self.internal_storage_path,"storage.sqlite"))
        cursor = await self.conn.cursor()
        
        await cursor.executescript('''BEGIN;
                                   CREATE TABLE IF NOT EXISTS managed_vehicles_list (vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT, vehicle_display_name TEXT);
                                   CREATE TABLE IF NOT EXISTS documents (document_id INTEGER PRIMARY KEY AUTOINCREMENT, document_scan_date DATETIME, document_print_date DATETIME, document_sum_cache DECIMAL);
                                   CREATE TABLE IF NOT EXISTS document_rows (row_id INTEGER PRIMARY KEY AUTOINCREMENT, document_id INTEGER, purchase_category INT, purchase_name TEXT, purchase_price INT, FOREIGN KEY(document_id) REFERENCES documents(document_id));
                                   COMMIT;''')
    # async def db_init(self):
        # self.conn = await sqlite.connect(join(self.internal_storage_path,"storage.sqlite"))
        # cursor = await self.conn.cursor()
        # 
        # await cursor.executescript('''BEGIN;
                                #    CREATE TABLE IF NOT EXISTS managed_vehicles_list (vehicle_id INT PRIMARY KEY AUTO_INCREMENT, vehicle_display_name TEXT);
                                #    CREATE TABLE IF NOT EXISTS documents (document_id INT PRIMARY KEY AUTO_INCREMENT, document_scan_date DATETIME, document_print_date DATETIME, document_sum_cache DECIMAL);
                                #    CREATE TABLE IF NOT EXISTS document_rows (row_id INT PRIMARY KEY AUTO_INCREMENT, document_id INT FOREIGN KEY NOT NULL,purchase_category INT FOREIGN KEY NOT NULL, purchase_name TEXT, purchase_price INT)
                                #    COMMIT''')
    async def db_read(self):
        pass
    async def db_write(self):
        pass
    async def db_edit(self):
        pass
    async def db_remove(self):
        pass
    def build(self):
        Clock.schedule_once(partial(self.nursery.start_soon,self.db_init))
        return MainManager()