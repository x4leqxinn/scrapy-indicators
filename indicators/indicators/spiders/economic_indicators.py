import scrapy
import datetime

class EconomicIndicator(scrapy.Spider):
    name = 'e_indicators'
    start_urls = [
        'https://www.dane.gov.co/index.php/indicadores-economicos'
    ]
    custom_settings = {
        'FEED_URI':'economic-indicators.csv',
        'FEED_FORMAT':'csv',
        'ROBOTSTXT_OBEY':True,
        'FEED_EXPORT_ENCODING':'utf-8',
    }

    def parse(self,response):
        indicators = response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').getall() 
        values = response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').getall()

        for indicator,value in zip(indicators,values):
            info = {
                'indicador': indicator,
                'valor': value,
                'fecha': datetime.date.today()
            }
            yield info