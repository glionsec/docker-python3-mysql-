import mysql.connector

cnx = None

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='root',  # パスワード
        host='mysql',  # ホスト名(IPアドレス）
        database='test_database', #データベース
        port='3306' #ポート番号
    )

    if cnx.is_connected:
        print("Connected!")

except mysql.connector.Error as e:
    if e.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User name or password is invalid.")
    elif e.errno == errorcode.ER_ACCOUNT_HAS_BEEN_LOCKED:
        print("This account is locked.")
    else:
        print(e)

except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()