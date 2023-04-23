import scrapy
from ..items import SpiderproItem


class ExampleSpider(scrapy.Spider):
    name = "jd_spy"
    # allowed_domains = ["example.com"]
    start_urls = ["http://jandan.com/"]

    def parse(self, response):
        div_list = response.xpath("//div[@id='content']/div[@class='post f list-post']")
        for div in div_list:
            div_title = div.xpath("./div[@class='indexs']/h2/a/text()")[0].extract()

            div_author = div.xpath("./div[@class='indexs']/div[@class='time_s']/a/text()")[0].extract()
            # print(div_title+' '+div_author)
            item = SpiderproItem()
            item['title'] = div_title
            item['author'] = div_author
            yield item

