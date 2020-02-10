import scrapy
from scrapy import Request, Spider
 
class ElPais(Spider):
   name = "el_pais"
   start_urls = [
       'https://brasil.elpais.com/tag/incendios/a'
   ]
 
   def parse(self, response):
       artigos = response.xpath('//article[contains(@id, "brasil-politica")]\
                               //div//h2//a')

       for artigo_link in artigos:
           url = artigo_link.xpath('./@href').extract_first()
           yield Request(
               url=response.urljoin(url),
               callback=self.parse_artigos,
           )
          
   def parse_artigos(self, response):
       titulo = response.xpath('//h1/text()').extract_first()
       subtitulo = response.xpath('//h2/text()').extract_first()
       conteudo = response.xpath('//section[contains(@class, "article_body")]//p/text()').extract()
       url_atual = response.url
 
       yield {
           'titulo': titulo,
           'subtitulo': subtitulo,
           'conteudo': conteudo,
           'link': url_atual,
       }
