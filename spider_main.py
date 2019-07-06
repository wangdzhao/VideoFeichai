# coding:utf8
# 调度程序
# 单线程版本
import html_downloader
import html_outputer
import html_parser


class SpiderMain(object):
    def __init__(self):
        # 模板下载器，下载数据解析器，解析数据输入器。 模块调度器
        self.downloader = html_downloader.HtmlDownloader()
        self.parser = html_parser.HtmlParser()
        self.outputer = html_outputer.HtmlOutputer()

    def craw(self, filename):
        num = 0
        try:
            f = open(filename)
            for line in f:
                html_cont = self.downloader.download(line)
                new_data = self.parser.parse(html_cont)
                self.outputer.collect_data(new_data)
                num += 1
                if num % 100 == 0:
                    self.outputer.output_mysql()
                    self.outputer.clear_data()
                print str(num) + " success"
            self.outputer.output_mysql()
            self.outputer.clear_data()
            f.close()
        except:
            print str(num) + " error"


if __name__ == "__main__":
    obj_spider = SpiderMain()
    obj_spider.craw("/craw/input.txt")
