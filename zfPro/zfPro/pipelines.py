# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as pymysql
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


from itemadapter import ItemAdapter
from .items import HousedetailItem, HousebasicItem, CostItem, IntermediaryItem


class ZfproPipeline:
    conn = None
    cur = None

    house_basic_list = []
    house_detail_list = []
    cost_list = []
    intermediary_list = []

    def open_spider(self, spider):
        self.conn = pymysql.connect(host='192.168.2.100', user='root', password='123456', port=3306,
                                    database='zufang')
        self.cur = self.conn.cursor()
    def process_item(self, item, spider):
        # executemany 传入多条数据  要是元组
        if isinstance(item, HousebasicItem):
            # 指定的是一次插入多少条数据
            if len(self.house_basic_list) == 30:
                print("开始写入HousebasicItem")
                print(self.house_basic_list)
                try:
                    sql = 'insert into housebasic_table(verification_code,title,maintain_time,district,street,community_name,lease_type,house_type) ' \
                          ' values(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE title=values(title),maintain_time=values(maintain_time)' \
                          ',district=values(district),street=values(street),community_name=values(community_name)' \
                          ',lease_type=values(lease_type),house_type=values(house_type)'
                    self.cur.executemany(sql, self.house_basic_list)
                    self.conn.commit()
                    # 插入数据后将列表清空
                except Exception as e:
                    print(e)
                    self.conn.rollback()
                finally:
                    self.house_basic_list = []
            else:
                item_tuple = (
                    item['verification_code'], item['title'], item['maintain_time'],
                    item['district'], item['street'], item['community_name'],
                    item['lease_type'],
                    item['house_type'])
                # print(item_tuple)
                self.house_basic_list.append(item_tuple)
        elif isinstance(item, HousedetailItem):
            if len(self.house_detail_list) == 30:
                print("开始写入HousedetailItem")
                print(self.house_detail_list)
                try:
                    sql = 'insert into housedetail_table(verification_code,area,orientation,check_in,floor,elevator,car_park,water,electric,gas,heating) ' \
                          ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),area=values(area)' \
                          ',orientation=values(orientation),check_in=values(check_in),floor=values(floor)' \
                          ',elevator=values(elevator),car_park=values(car_park),water=values(water),electric=values(electric),gas=values(gas),heating=values(heating)'
                    self.cur.executemany(sql, self.house_detail_list)
                    self.conn.commit()
                    # 插入数据后将列表清空
                except Exception as e:
                    print(e)
                    self.conn.rollback()
                finally:
                    self.house_detail_list = []
            else:

                item_tuple = (
                    item['verification_code'], item['area'], item['orientation'],
                    item['check_in'], item['floor'], item['elevator'],
                    item['car_park'], item['water'], item['electric'],
                    item['gas'],
                    item['heating'])
                # print(item_tuple)
                self.house_detail_list.append(item_tuple)
        elif isinstance(item, CostItem):
            if len(self.cost_list) == 30:
                print("开始写入CostItem")
                print(self.cost_list)
                try:
                    sql = 'insert into cost_table(verification_code,rent,payment_type,deposit,service_charge,agency_fee) ' \
                          ' values(%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),rent=values(rent)' \
                          ',payment_type=values(payment_type),deposit=values(deposit),service_charge=values(service_charge)' \
                          ',agency_fee=values(agency_fee)'
                    self.cur.executemany(sql, self.cost_list)
                    self.conn.commit()
                    # 插入数据后将列表清空
                except Exception as e:
                    print(e)
                    self.conn.rollback()
                finally:
                    self.cost_list = []
            else:
                item_tuple = (
                    item['verification_code'], item['rent'], item['payment_type'],
                    item['deposit'], item['service_charge'], item['agency_fee'])
                # print(item_tuple)

                self.cost_list.append(item_tuple)
        elif isinstance(item, IntermediaryItem):
            if len(self.intermediary_list) == 30:
                print("开始写入IntermediaryItem")
                print(self.intermediary_list)
                try:
                    sql = 'insert into intermediary_table(verification_code,intermediary_name,intermediary_number,mechanism_number) ' \
                          ' values(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),intermediary_name=values(intermediary_name)' \
                          ',intermediary_number=values(intermediary_number),mechanism_number=values(mechanism_number)'
                    self.cur.executemany(sql, self.intermediary_list)
                    self.conn.commit()
                    # 插入数据后将列表清空
                except Exception as e:
                    print(e)
                    self.conn.rollback()
                finally:
                    self.intermediary_list = []
            else:
                item_tuple = (
                    item['verification_code'], item['intermediary_name'], item['intermediary_number'],
                    item['mechanism_number'])
                # print(item_tuple)
                self.intermediary_list.append(item_tuple)
        return item
    def close_spider(self, spider):
        if len(self.house_basic_list) > 0:
            print("最后写入house_basic_list:")
            print(self.house_basic_list)
            try:
                sql = 'insert into housebasic_table(verification_code,title,maintain_time,district,street,community_name,lease_type,house_type) ' \
                      ' values(%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE title=values(title),maintain_time=values(maintain_time)' \
                      ',district=values(district),street=values(street),community_name=values(community_name)' \
                      ',lease_type=values(lease_type),house_type=values(house_type)'
                self.cur.executemany(sql, self.house_basic_list)
                self.conn.commit()
                # 插入数据后将列表清空
            except Exception as e:
                print(e)
                self.conn.rollback()
            finally:
                self.house_basic_list = []
        if len(self.house_detail_list) > 0:
            print("最后写入house_detail_list:")
            print(self.house_detail_list)
            try:
                sql = 'insert into housedetail_table(verification_code,area,orientation,check_in,floor,elevator,car_park,water,electric,gas,heating) ' \
                      ' values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),area=values(area)' \
                      ',orientation=values(orientation),check_in=values(check_in),floor=values(floor)' \
                      ',elevator=values(elevator),car_park=values(car_park),water=values(water),electric=values(electric),gas=values(gas),heating=values(heating)'
                self.cur.executemany(sql, self.house_detail_list)
                self.conn.commit()
                # 插入数据后将列表清空
            except Exception as e:
                print(e)
                self.conn.rollback()
            finally:
                self.house_detail_list = []
        if len(self.cost_list) > 0:
            print("最后写入cost_list:")
            print(self.cost_list)
            try:
                sql = 'insert into cost_table(verification_code,rent,payment_type,deposit,service_charge,agency_fee) ' \
                      ' values(%s,%s,%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),rent=values(rent)' \
                      ',payment_type=values(payment_type),deposit=values(deposit),service_charge=values(service_charge)' \
                      ',agency_fee=values(agency_fee)'
                self.cur.executemany(sql, self.cost_list)
                self.conn.commit()
                # 插入数据后将列表清空
            except Exception as e:
                print(e)
                self.conn.rollback()
            finally:
                self.cost_list = []
        if len(self.intermediary_list) > 0:
            print("最后写入intermediary_list:")
            print(self.intermediary_list)
            try:
                sql = 'insert into intermediary_table(verification_code,intermediary_name,intermediary_number,mechanism_number) ' \
                      ' values(%s,%s,%s,%s) ON DUPLICATE KEY UPDATE verification_code=values(verification_code),intermediary_name=values(intermediary_name)' \
                      ',intermediary_number=values(intermediary_number),mechanism_number=values(mechanism_number)'
                self.cur.executemany(sql, self.intermediary_list)
                self.conn.commit()
                # 插入数据后将列表清空
            except Exception as e:
                print(e)
                self.conn.rollback()
            finally:
                self.intermediary_list = []
        self.cur.close()
        self.conn.close()
