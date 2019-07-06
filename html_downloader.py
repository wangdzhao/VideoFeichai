# coding:utf-8
# HTML下载器
import urllib2
import zlib
import brotli


class HtmlDownloader(object):
    def download(self, url):
        if url is None:
            return None
        # 构建一个已经登录过的用户的headers信息
        headers = {
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,"
                      "application/signed-exchange;v=b3",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "zh-CN,zh;q=0.9",
            "cache-control": "max-age=0",
            "Connection": "keep-alive",
            "cookie": "__cfduid=dc4e6eb6c19ecaada3ddfb3e7ba5273551561794652; PHPSESSID=rj9ipa44nvhol6k9l5mq9js0h2; kt_ips=222.212.204.46; kt_tcookie=1; kt_is_visited=1; kt_tcookie=1; kt_qparams=id%3D40782%26dir%3D083df3018b44c39b0e8f07600c79530d%26mode%3Dasync%26action%3Djs_stats%26rand%3D1561809712293",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/75.0.3770.80 Safari/537.36",
        }
        request = urllib2.Request(url, headers=headers)
        response = urllib2.urlopen(request)
        if response.getcode() != 200:
            return None
        content = response.read()
        encoding = response.headers.get('Content-Encoding')
        if encoding == 'gzip':
            html = zlib.decompress(content, 16 + zlib.MAX_WBITS)
        elif encoding == "br":
            html = brotli.decompress(content)
        else:
            html = content
        result = html.decode("utf8")
        return result
