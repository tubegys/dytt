import pymysql

db = pymysql.connect(
    host='127.0.0.1',
    user='root',
    passwd='123',
    db='db_gys',
    charset='utf8'
)
cursor = db.cursor()
insert_sql = 'insert into tb_dytt(film_title,create_date)values(%s,%s)'
cursor.execute(insert_sql,('11111', '222222'))
db.commit()

db.close()