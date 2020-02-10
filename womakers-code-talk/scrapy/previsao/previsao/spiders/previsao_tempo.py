# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import scrapy

class Previsao(scrapy.Spider):
   name = "previsao"

   start_urls = [
       "https://www.climatempo.com.br/previsao-do-tempo/15-dias/cidade/558/saopaulo-sp"
   ]

   def parse(self, response):
       dias = response.xpath('//div[contains(@id, "resumeDay")]')

       for dia in dias:
           dia_semana = dia.xpath('.//div[contains(@class, "title")]//p/text()[1]').extract_first().strip()
           data = dia.xpath('.//div[contains(@class, "title")]//p/text()[2]').extract_first().strip()
           max_temp = dia.xpath('.//p[contains(@id, "tempMax")]/text()').extract_first()
           min_temp = dia.xpath('.//p[contains(@id, "tempMin")]/text()').extract_first()
           desc = dia.xpath('.//div[contains(@class, "description-block")]//span/text()').extract_first()
           print("Dia: " + dia_semana + data)
           print("Máxima: " + max_temp)
           print("Mínima: " + min_temp)
           print("Descrição: " + desc)
           yield{
               'dia_sem': dia_semana,
               'data': data,
               'max_temp': max_temp,
               'min_temp': min_temp,
               'desc': desc,
           }

