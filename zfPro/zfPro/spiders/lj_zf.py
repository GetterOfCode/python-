import scrapy
import time
from ..items import HousebasicItem, HousedetailItem, CostItem, IntermediaryItem


class ZfSpider(scrapy.Spider):
    name = "zf"
    # allowed_domains = ["www.xxx.com"]
    start_urls = ["https://hf.lianjia.com/zufang/pg1"]

    next_url = 'https://hf.lianjia.com/zufang/pg%d/'
    page = 2

    def parse(self, response):
        div_list = response.xpath('//div[@class="content__list"]/div[@class="content__list--item"]')
        for div in div_list:
            # time.sleep(1)
            detail_url = 'https://hf.lianjia.com' + div.xpath('./a/@href').extract_first()
            if 'apartment' in div.xpath('./a/@href').extract_first():
                continue
            print(detail_url)
            yield scrapy.Request(url=detail_url, callback=self.parse_detail)

        if self.page <= 1000:
            # time.sleep(1)
            n_url = self.next_url % self.page
            print("详情页"+n_url)
            self.page += 1
            yield scrapy.Request(url=n_url, callback=self.parse)

    def parse_detail(self, response):
        try:
            # 核验码
            verification_code = \
                response.xpath('/html/body/div[3]/div[1]/div[3]/div[1]/i/text()').extract()[1].strip().replace('\n', '')
            if verification_code.startswith("合肥"):
                verification_code = verification_code.split("核验码")[1]
            else:
                verification_code = verification_code.split("：")[1]
            # 维护时间
            maintain_time = response.xpath(
                '/html/body/div[3]/div[1]/div[3]/div[@class="content__subtitle"]/text()').extract_first().strip().split(
                "：")[1]
            # 房源标题
            title = response.xpath(
                '/html/body/div[3]/div[1]/div[3]/p[@class="content__title"]/text()').extract_first().strip()
            # print(title)
            # print(response.xpath('//p[@class="bread__nav__wrapper oneline"]/a[2]/text()'))
            # 所在区
            district = \
                response.xpath('//p[@class="bread__nav__wrapper oneline"]/a[2]/text()').extract_first().strip().split('租')[
                    0]
            # 所在路
            street = \
                response.xpath('//p[@class="bread__nav__wrapper oneline"]/a[3]/text()').extract_first().strip().split('租')[
                    0]
            # 小区名
            community_name = \
                response.xpath(
                    '//div[@class="bread__nav w1150 bread__nav--bottom"]/h1/a/text()').extract_first().strip().split('租')[
                    0]
            # 出租类型
            lease_type = response.xpath('//*[@id="aside"]/ul/li[1]/text()').extract_first().strip()
            # 户型
            house_type = response.xpath('//*[@id="aside"]/ul/li[2]/text()').extract_first().strip()

            # 面积
            area = response.xpath('//*[@id="info"]/ul[1]/li[2]/text()').extract_first().strip().split('：')[1].split('㎡')[0]
            # 朝向
            orientation = response.xpath('//*[@id="info"]/ul[1]/li[3]/text()').extract_first().strip().split('：')[1]
            # 入住
            check_in = response.xpath('//*[@id="info"]/ul[1]/li[6]/text()').extract_first().strip().split('：')[1]
            # 楼层
            floor = response.xpath('///*[@id="info"]/ul[1]/li[8]/text()').extract_first().strip().split('：')[1]
            # 电梯
            elevator = response.xpath('///*[@id="info"]/ul[1]/li[9]/text()').extract_first().strip().split('：')[1]
            # 车位
            car_park = response.xpath('//*[@id="info"]/ul[1]/li[11]/text()').extract_first().strip().split('：')[1]
            # 用水
            water = response.xpath('///*[@id="info"]/ul[1]/li[12]/text()').extract_first().strip().split('：')[1]
            # 用电
            electric = response.xpath('///*[@id="info"]/ul[1]/li[14]/text()').extract_first().strip().split('：')[1]
            # 燃气
            gas = response.xpath('//*[@id="info"]/ul[1]/li[15]/text()').extract_first().strip().split('：')[1]
            # 采暖
            heating = response.xpath('//*[@id="info"]/ul[1]/li[17]/text()').extract_first().strip().split('：')[1]

            # 房租
            rent = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[2]/text()').extract_first()
            # 付款方式
            payment_type = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[1]/text()').extract_first()
            # 押金
            deposit = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[3]/text()').extract_first()
            # 服务费
            service_charge = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[4]/text()').extract_first()
            # 中介费
            agency_fee = response.xpath('//*[@id="cost"]/div/div[2]/div/ul/li[5]/text()').extract_first()

            # 中介名
            intermediary_name = response.xpath('//*[@id="aside"]/div[2]/div[2]/div[1]/span[2]/text()').extract_first()
            # 中介编号
            intermediary_number = response.xpath('///*[@id="aside"]/div[2]/div[2]/div[3]/a/text()').extract_first()
            intermediary_number = intermediary_number if intermediary_number == None \
                else intermediary_number.split('详情')[0].strip()
            # 机构备案编号
            mechanism_number = response.xpath('//*[@id="aside"]/div[2]/div[2]/div[4]/a/text()').extract_first()
            mechanism_number = mechanism_number if mechanism_number == None \
                else mechanism_number.split('详情')[0].strip()
        except Exception as e:
            print(e)
        else:
            house_basic = HousebasicItem(verification_code=verification_code, maintain_time=maintain_time, title=title
                                         , district=district, street=street, community_name=community_name
                                         , lease_type=lease_type, house_type=house_type)
            yield house_basic
            house_detail = HousedetailItem(verification_code=verification_code, area=area, orientation=orientation
                                           , check_in=check_in, floor=floor, elevator=elevator, car_park=car_park
                                           , water=water, electric=electric, gas=gas, heating=heating)
            yield house_detail

            cost = CostItem(verification_code=verification_code, rent=rent,
                            payment_type=payment_type,
                            deposit=deposit,
                            service_charge=service_charge,
                            agency_fee=agency_fee)
            yield cost

            intermed = IntermediaryItem(verification_code=verification_code,
                                        intermediary_name=intermediary_name,
                                        intermediary_number=intermediary_number,
                                        mechanism_number=mechanism_number)
            yield intermed