#coding=utf-8

import pymysql as mysql

class Base:


    def __init__(self):
        self.db = mysql.connect(host='localhost', user='root', passwd="0000", db='Tripresso', charset="utf8")
        self.cursor = self.db.cursor()

        self.cursor.execute("create table if not exists agencytable ("
                            "agency_id int NOT NULL AUTO_INCREMENT,"
                            "agency_text varchar(255) NOT NULL, "
                            "unique (agency_text),"
                            "PRIMARY KEY (agency_id))")


        self.cursor.execute("create table if not exists bigtable("
                            "id int NOT NULL AUTO_INCREMENT,"
                            "title text NOT NULL,"
                            "product_num varchar(255) NOT NULL, "
                            "product_price text NOT NULL, "
                            "product_days text NOT NULL," 
                            "product_total text NOT NULL," 
                            "product_available text NOT NULL," 
                            "product_date_normal text NOT NULL, "
                            "agency_id int, "        
                            "PRIMARY KEY (id),"
                            "UNIQUE (product_num),"
                            "foreign key (agency_id) references agencytable(agency_id))")



    def add_agency(self,title):
        self.cursor.execute("insert into agencytable(agency_text) values('{}')on duplicate key update agency_text='{}'".format(title,title))
        return


    def add_dat(self,t,n,p,d,tt,a,dn,title):
        self.cursor.execute("alter table bigtable modify title MEDIUMTEXT character set utf8")
        self.cursor.execute("alter table bigtable modify product_days MEDIUMTEXT character set utf8")
        self.cursor.execute("insert into bigtable(title,product_num,product_price,product_days,product_total,product_available,product_date_normal,agency_id) "
                            "values('{}','{}','{}','{}','{}','{}','{}',(select agency_id from agencytable where agency_text='{}')) on duplicate key update product_num ='{}' ".format(t,n,p,d,tt,a,dn,title,n))
        self.db.commit()
        return




    #不用foreign key
    # def check_agency_title(self,title):
    #
    #     self.cursor.execute("create table if not exists {}("
    #                         "id int NOT NULL AUTO_INCREMENT, "
    #                         "title text NOT NULL,  "
    #                         "product_num varchar(255) NOT NULL, "
    #                         "product_price text NOT NULL, "
    #                         "product_days text NOT NULL,"
    #                         "product_total text NOT NULL,"
    #                         "product_available text NOT NULL,"
    #                         "product_date_normal text NOT NULL, "
    #                         "PRIMARY KEY (id),"
    #                         "UNIQUE (product_num))".format(title))
    #     # self.cursor.close()
    #     return
    #
    #
    # def time_to_add_data(self,title,t,n,p,d,tt,a,dn):
    #     self.cursor.execute("alter table {} modify title MEDIUMTEXT character set utf8".format(title))
    #     self.cursor.execute("alter table {} modify product_days MEDIUMTEXT character set utf8".format(title))
    #     self.cursor.execute("insert into {}(title,product_num,product_price,product_days,product_total,product_available,product_date_normal) "
    #                         "values('{}','{}','{}','{}','{}','{}','{}') on duplicate key update product_num ='{}' ".format(title,t,n,p,d,tt,a,dn,n))
    #     self.db.commit()
    #     return print('Done')
