# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class SpiderproPipeline:
    fp = None
    def open_spider(self,spider):
        print('')
        self.fp = open(spider.name+'.txt','w',encoding='utf8')
    def process_item(self, item, spider):
        self.fp.write(item['title']+' '+item['author']+'\n')
        return item
    def close_spider(self,spider):
        self.fp.close()
class DbPipeline:
    def open_spider(self,spider):
    def process_item(self, item, spider):
    def close_spider(self,spider):