import scrapy

class QuotesSpider(scrapy.Spider):
    name = "li_tags"

    def start_requests(self):
        file =  open("../../urls.txt", 'r')
        urls  = file.readlines()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        filename = 'li_tags_file.txt'
        with open(filename, 'a') as f:
            ulElement = response.xpath('//ul[has-class("project-details-list")]');
            f.write(ulElement.xpath('.//li')[0].xpath('./strong/text()').get() + ulElement.xpath('.//li')[0].xpath(
                './text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[1].xpath('./strong/text()').get() + ulElement.xpath('.//li')[1].xpath(
                './text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[2].xpath('./strong/text()').get() + ulElement.xpath('.//li')[2].xpath(
                './text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[3].xpath('./strong/text()').get() + ulElement.xpath('.//li')[3].xpath(
                './text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[4].xpath('./strong/text()').get() + ulElement.xpath('.//li')[4].xpath(
                './text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[5].xpath('./strong/text()').get() + ulElement.xpath('.//li')[5].xpath(
                './text()').get())
            f.write('\n')
            if (len(ulElement.xpath('.//li')) == 6):
                return;
            f.write(ulElement.xpath('.//li')[6].xpath('./strong/text()').get() + ulElement.xpath('.//li')[6].xpath(
                './a/text()').get())
            f.write('\n')
            f.write(ulElement.xpath('.//li')[7].xpath('./strong/text()').get() + ulElement.xpath('.//li')[7].xpath(
                './text()').get())
            f.write('\n')
            if (len(ulElement.xpath('.//li')) == 9):
                f.write(ulElement.xpath('.//li')[8].xpath('./strong/text()').get() + ulElement.xpath('.//li')[8].xpath(
                    './text()').get())
            else:
                f.write(ulElement.xpath('.//li')[8].xpath('./strong/text()').get() + ulElement.xpath('.//li')[8].xpath(
                    './a/text()').get())
                f.write(ulElement.xpath('.//li')[9].xpath('./strong/text()').get() + ulElement.xpath('.//li')[9].xpath(
                    './text()').get())
            f.write('\n')

        self.log('Saved file %s' % filename)