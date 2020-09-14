from scrapy import Spider,Request
class New(Spider):
    name='news'
    start_urls=['https://www.nydailynews.com/']     # this new york Daily news website
    
    def parse(self,response):
        links=response.css('h6 a::attr(href)').extract() # this conatins all links of the news on the site
        link=response.css('div.recommender a::attr(href)').extract() # this conatins all the recommendation that site suggests
        print(len(links))  # to printout the number of links
        for url in links:
            url='https://www.nydailynews.com'+url  # this is complete the Url 
            yield Request(url=url,callback=self.parsedetail)
        
    def parsedetail(self,response):
        try:
            title=response.css('h1.spaced-bottom::text').extract()  # this tag contins all the headlines
        except:
            title=""
        try:
            story=response.css('div.card-content p::text').extract()  # This Tage conatins all the story of the news
        except:
            story=""
        yield{
            'headline':title,
            'story_in_detail':story
        }
   