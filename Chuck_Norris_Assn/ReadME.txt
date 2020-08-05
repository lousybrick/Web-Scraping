
import scrapy 

class QuotesSpider(scrapy.Spider):
    #This is what I will call on my cmd 
    name = "quotes"

    # This method allows you to make requests to get or post 
    def start_requests(self):
        #Make a list of urls
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]

        #Generator function
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse) #(request url response, parse the url response)

    def parse(self, response):
        page = response.url.split("/")[-2] # Indexing the page response
        filename = 'quotes-%s.html' % page #Storing it into an html file
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename) #Storing the file in my directory

#on cmd : scrapy crawl quotes



import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotesJSON"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self,response):

        for q in response.css('div.quote'):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()

            yield {
                'text' : text,
                'author' : author,
                'tags' : tags,
            }

#Command on cmd : scrapy crawl quotesJ -o quotes.json



import scrapy
import urllib

class QuotesSpider(scrapy.Spider):
    name = "quotesRec"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
        ]

        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
    
    def parse(self,response):

        for q in response.css('div.quote'):
            text = q.css('span.text::text').get()
            author = q.css('small.author::text').get()
            tags = q.css('a.tag::text').getall()

            yield {
                'text' : text,
                'author' : author,
                'tags' : tags,
            }

        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback = self.parse)