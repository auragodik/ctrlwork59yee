CREATE_SHOPS = """
CREATE TABLE IF NOT EXISTS shoplist(
id INTEGER PRIMARY KEY AUTOINCREMENT,
shops TEXT NOT NULL,
kupleno INTEGER DEFAULT 0
)
"""
INSERT_SHOPS =  "INSERT INTO shoplist (shops) VALUES (?)"

SELECT_SHOPS = "SELECT id, shops, kupleno FROM shoplist"

SELECT_SHOPS_PURCHASED = "SELECT id, shops, kupleno FROM shoplist WHERE kupleno = 1"

SELECT_SHOPS_UNPURCHASED = "SELECT id, shops, kupleno FROM shoplist WHERE kupleno = 0"

UPDATE_SHOPS = "UPDATE shoplist SET shops = ? WHERE id = ?"

DELETE_SHOPS = "DELETE FROM shoplist WHERE id = ?"