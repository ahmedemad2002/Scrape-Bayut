import scrapy


class UrlsSpider(scrapy.Spider):
    name = "urls"
    BASE_URL = "https://www.bayut.eg"
    start_urls = [f"https://www.bayut.eg/en/egypt/properties-for-rent/page-{i}/?rent_frequency=any" for i in range(2, 185)]

    def parse(self, response):
        urls = set(response.css('a._287661cb::attr(href)').getall())
        for url in urls:
            yield scrapy.Request(url=self.BASE_URL+url, callback=self.parsepage)
            
    def parsepage(self, response):
        imgs = response.css('div.fe270b0a img::attr(src)').getall()
        property_attrs = response.css('span.fc2d1086 *::text').getall()
        property_info = response.css('ul._033281ab li')
        property_info = {li.css('span._3af7fa95::text').get(): li.css('span._812aa185::text').get() for li in property_info}
        yield{
            'url': response.url,
            'id': response.url.split('-')[1].split('.')[0],
            'imgs': imgs,
            'price': response.css('span._105b8a67::text').get(),
            'location': response.css('div._1f0f1758::text').get(),
            'Amenities': response.css('span._005a682a::text').getall(),
        }|{f'attr_{i+1}': attr for i, attr in enumerate(property_attrs)}|property_info
