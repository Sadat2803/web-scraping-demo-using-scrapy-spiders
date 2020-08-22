import scrapy

class QuotesSpider(scrapy.Spider):
    name = "h1_tags"

    def start_requests(self):
        file =  open("urls.txt", 'r')
        urls  = file.readlines()
        print(urls)
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        title = response.xpath('//h1/text()').getall()
        filename = 'h1_tags_file.txt'
        with open(filename, 'a') as f:
            f.write(title[1])
            f.write('\n')
        self.log('Saved file %s' % filename)