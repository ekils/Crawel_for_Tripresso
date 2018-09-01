#coding=utf-8

from selenium import webdriver
from bs4 import BeautifulSoup
import  time
import re

import database

class CW_class:

    def __init__(self):

        self.db = database.Base()
        self.service_args = []
        self.service_args.append('--load-images=no')
        self.service_args.append('--disk-cache=yes')
        self.service_args.append('--ignore-ssl-errors=true')
        self.driver = webdriver.PhantomJS(executable_path='/usr/local/Cellar/phantomjs/2.1.1/bin/phantomjs',service_args=self.service_args)
        self.__url = 'http://www.orangetour.com.tw/EW/GO/GroupList.asp'  #   誠心誠意
        # self.__url = 'https://www.gloriatour.com.tw/EW/GO/GroupList.asp' # 華泰

    @property
    def url(self):
        return self.__url

    def main(self, page=None):


        count = 1
        agency = []
        if page!=None:
            print(f'key in page:{page}')
            p =page
        else:
            p=1

        self.driver.set_window_size(1024, 768)
        u = self.url
        self.driver.get(u)


        pat_title = re.compile('(?:http|https)://www\..*\.com')
        t = pat_title.search(u).group()
        agency_title = (t.split('www.')[1]).split('.com')[0]


        # self.db.check_agency_title(agency_title)
        self.db.add_agency(agency_title)

        while p >=1:
            print(count)
            pg = count * 2 + 1

            self.driver.find_element_by_xpath(f"//*[@id='panel-1']/nav/ul[@class='pagination']/li[{pg}]/a").click()
            time.sleep(5)
            soup = BeautifulSoup(self.driver.page_source, "html.parser")

            l = (soup.find_all('div', 'thumbnail'))  # 網站用thumbnail 做區塊

            for i in range(len(l)//2):  # 因為重複
                a = l[i].find('div', 'product_name').contents[1]
                a = (str(a).replace(" ", "")).replace('\n', '')
                pat = re.compile('</span>.*<div')
                title = ((pat.search(a).group()).split('</span>')[2]).split('<div')[0]
                product_num = (l[i].find('span', 'product_num').string)
                product_price = (l[i].find('div', 'product_price').find('strong').string)
                product_days = (l[i].find('div', 'product_days').string)
                product_total = (l[i].find('div', 'product_total').find('span', 'number').string)
                product_available = (l[i].find('div', 'product_available').find('span', 'number').string)
                product_date_normal = (l[i].find('div', 'product_date normal').string)

                dic = {
                    'title': title,
                    'product_num': product_num,
                    'product_price': product_price,
                    'product_days': product_days,
                    'product_total': product_total,
                    'product_available': product_available,
                    'product_date_normal': product_date_normal
                }
                agency.append(dic)

            # print(len(agency))
            count= count+1
            p = p-1
        print(agency_title)
        # print(agency)

        for i in agency:
            # self.db.time_to_add_data(agency_title,i['title'],i['product_num'],i['product_price'],i['product_days'],i['product_total'],i['product_available'],i['product_date_normal'])
            self.db.add_dat(i['title'],i['product_num'],i['product_price'],i['product_days'],i['product_total'],i['product_available'],i['product_date_normal'],agency_title,)


if __name__ == '__main__':
    cw= CW_class()
    cw.main(3)
