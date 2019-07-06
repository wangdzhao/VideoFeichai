# coding:utf-8
# HTML解析器

from bs4 import BeautifulSoup


class HtmlParser(object):

    def _get_new_data(self, soup):
        # 如果没有文件内容，直接返回
        if soup.find('div', attrs={'class': 'headline'}) is None:
            return None
        res_data = {}
        # 获取title
        res_data['title'] = soup.find('meta', attrs={'property': 'og:title'}).attrs['content']
        # 获取img
        res_data['img'] = soup.find('meta', attrs={'property': 'og:image'}).attrs['content']
        # 获取mp4
        res_data['video'] = soup.find('div', attrs={'class': 'item', 'style': 'display:none'}).find("a").attrs['href']
        return res_data

    def parse(self, html_cont):
        if html_cont is None:
            return
        soup = BeautifulSoup(html_cont, 'html.parser')
        new_data = self._get_new_data(soup)
        return new_data
