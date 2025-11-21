import sqlite3
from db import sqlqueries
from config import path_db


def init_db():
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(sqlqueries.CREATE_SHOPS)
    print('БД ПОДКЛЮЧЕНО БРАТ!')
    conn.commit()
    conn.close()


def add_buys(shops):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(sqlqueries.INSERT_SHOPS, (shops,))
    shops_id = cursor.lastrowid
    conn.commit()
    conn.close()
    return shops_id


def get_buys(filters):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if filters == 'purchased':
        cursor.execute(sqlqueries.SELECT_SHOPS_PURCHASED)
    elif filters == 'unpurchased':
        cursor.execute(sqlqueries.SELECT_SHOPS_UNPURCHASED)
    else:
        cursor.execute(sqlqueries.SELECT_SHOPS)

    shoplist = cursor.fetchall()
    conn.close()
    return shoplist


def update_buys(shops_id, new_shops=None, kupleno=None):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()

    if kupleno is not None:
        cursor.execute(
            "UPDATE shoplist SET kupleno = ? WHERE id = ?",
            (kupleno, shops_id)
        )

    if new_shops is not None:
        cursor.execute(
            sqlqueries.UPDATE_SHOPS,
            (new_shops, shops_id)
        )

    conn.commit()
    conn.close()


def delete_buys(shops_id):
    conn = sqlite3.connect(path_db)
    cursor = conn.cursor()
    cursor.execute(sqlqueries.DELETE_SHOPS, (shops_id,))
    conn.commit()
    conn.close()
