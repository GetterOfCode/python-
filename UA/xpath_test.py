from lxml import etree
if __name__ == '__main__':
    tree = etree.parse('./test.html')
    # print(tree.xpath('/html/body/div/p'))
    list = tree.xpath('//div[@class = "song"]/p/text()')
    # for i in list:
    #     print(i)
    tree.xpath('//')
