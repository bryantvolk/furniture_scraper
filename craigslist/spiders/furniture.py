# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class FurnitureSpider(scrapy.Spider):
    name = 'furniture'
    allowed_domains = ['nh.craigslist.org']
    start_urls = ['https://nh.craigslist.org/search/fua/']

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs:
            title = job.xpath('a/text()').extract_first()
            city = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
            relative_url = job.xpath('a/@href').extract_first()
            url = response.urljoin(relative_url)
            yield Request(url, callback=self.parse_page, meta={'URL':url, 'Title':title, 'City':city})

        relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
        next_url = response.urljoin(relative_next_url)
        yield Request(next_url, callback=self.parse)

    def parse_page(self, response):
        url = response.meta.get('URL')
        title = response.meta.get('Title')
        city = response.meta.get('City')
        description = "".join(line for line in response.xpath('//*[@id="postingbody"]/text()').extract())
        condition = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
        price = response.xpath('//*[@class="price"]/text()').extract_first()
        print price
        yield{'URL':url, 'Title':title,'City':city,'Price':price, 'Description':description, 'Condition':condition}
