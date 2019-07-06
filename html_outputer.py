# coding:utf-8
# HTML输出器
import MySQLdb
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class HtmlOutputer(object):
    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def clear_data(self):
        self.datas = []

    def output_mysql(self):
        # 打开数据库连接
        db = MySQLdb.connect(host="127.0.0.1",
                             user="root",
                             passwd="598c43b01dae99f7",
                             db="data",
                             port=3306,
                             charset='utf8')
        for data in self.datas:
            # 使用cursor()方法获取操作游标
            cursor = db.cursor()
            # SQL 插入语句
            sql = "insert into mydata(title, img, video) " \
                  "values (%(title)s, %(img)s, %(video)s)"
            values = {"title": data['title'],
                      "img": data['img'],
                      "video": data['video']}
            try:
                # 执行sql语句
                cursor.execute(sql, values)
                # 提交到数据库执行
                db.commit()
            except:
                # Rollback in case there is any error
                db.rollback()

        # 关闭数据库连接
        db.close()
