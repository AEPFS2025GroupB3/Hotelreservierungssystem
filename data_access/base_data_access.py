import os

import sqlite3


class BaseDataAccess:
    def __init__(self, db_connection_str: str = None):
        if db_connection_str is None:
            self.__db_connection_str = os.environ.get("DB_FILE")
            if self.__db_connection_str is None:
                raise Exception("DB_FILE environment variable and parameter path is not set.")
        else:
            self.__db_connection_str = db_connection_str

    def _connect(self):
        return sqlite3.connect(self.__db_connection_str, detect_types=sqlite3.PARSE_DECLTYPES)

    def fetchone(self, sql: str, params: tuple | None = ()):
        with self._connect() as conn:
            try: 
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchone()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def fetchall(self, sql: str, params: tuple | None = ()) -> list:
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                result = cur.fetchall()
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
        return result

    def execute(self, sql: str, params: tuple | None = ()) -> tuple[int, int]:
        with self._connect() as conn:
            try:
                cur = conn.cursor()
                cur.execute(sql, params)
                last_row_id = cur.lastrowid
                row_count = cur.rowcount
                conn.commit()
                return last_row_id, row_count
            except sqlite3.Error as e:
                conn.rollback()
                raise e
            finally:
                cur.close()
