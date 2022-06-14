import mysql.connector as mydb

# コネクションの作成
conn = mydb.connect(
    host='mysql',
    port='3306',
    user='root',
    password='root',
    database='test_database'
)


# コネクションが切れた時に再接続してくれるよう設定
conn.ping(reconnect=True)

# 接続できているかどうか確認
print(conn.is_connected())

# DB操作用にカーソルを作成
cur = conn.cursor()

sql = ('''
INSERT INTO article 
    (name, age)
VALUES 
    (%s, %s)
''')

data = [
    ('加藤', 23),
    ('榊', 42),
    ('小室', 32)
]

cur.executemany(sql, data)
conn.commit()
print(f"{cur.rowcount} records inserted.")

# DB操作が終わったらカーソルとコネクションを閉じる
cur.close()
conn.close()