# -*- coding: utf-8 -*- 
from elcinema_now import ElcinemaNowSpider
from scrapy.contrib.spiders import Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor

class ElcinemaNowSpiderEN(ElcinemaNowSpider):
  name = "elcinema_now_en"
  domain_name = "elcinema.com"
  CONCURRENT_REQUESTS = 1

  """
    USAGE:
    scrapy crawl elcinema_now 
  """
  start_urls = ["http://www.elcinema.com/en/now/eg","http://www.elcinema.com/en/now/ae","http://www.elcinema.com/en/now/lb"]

  rules = (
    #pagination
    Rule(SgmlLinkExtractor(allow=('/\d+'),restrict_xpaths=('//div[contains(@class,"pagination")]/ul/li'), unique=True), follow=True),
    #Movies
    Rule(SgmlLinkExtractor(restrict_xpaths=('//div[@class="row"]/div//span/a'), unique=True), follow=True,callback='start'),
  )
  site_language = "en"
