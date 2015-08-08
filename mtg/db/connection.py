import pymysql

conn_params = {
        'host'      :'localhost',
        'user'      :'mtguser',
        'password'  :'mtgpass',
        'charset'   :'utf8',
        'database'  :'mtg'
}

def connect():
    return pymysql.connect(**conn_params)
