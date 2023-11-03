import scrapy


class PropertyfinderSpider(scrapy.Spider):
    name = "propertyfinder"
    
    headers = {
        ':authority': 'www.propertyfinder.eg',
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.60",
        'Cookies': 'sp=c9202659-460c-4e87-8ade-0502989fec13; _gcl_au=1.1.868019822.1697248249; __rtbh.uid=%7B%22eventType%22%3A%22uid%22%2C%22id%22%3A%22018b2be0fd1b00017c609b36d6df05081002107900bd0%22%7D; __rtbh.lid=%7B%22eventType%22%3A%22lid%22%2C%22id%22%3A%227e4foqB91CBzpVpIFaH6%22%7D; _scid=4b9a5be6-040d-43a6-a215-f79f85b4600f; _gid=GA1.2.680062070.1697248250; _sctr=1%7C1697230800000; _fbp=fb.1.1697248253412.1950444389; _hjSessionUser_385772=eyJpZCI6ImI2NjdjM2RmLTFlOGUtNTg1NC04ZjMwLWI1MGYxODU0MjY5MiIsImNyZWF0ZWQiOjE2OTcyNDgyNTU2MTUsImV4aXN0aW5nIjp0cnVlfQ==; ak_bmsc=686D5618E22EEE84A09CA8E7D50A1812~000000000000000000000000000000~YAAQDuF6XJjiER2LAQAAxCQsLxXgLbUS5Q2RH7DCg0Q8kcPMyiMlwdjZvU+DixrdIhDDm4QTY3wisBSJYshm1v117eMCHv53cMj1Kp0PkAqiQcT5ZEU2sBtIV83bRhpIhsbJ41FTaf7oaLil+pcAI5F+ISZmRScwsVTvVHWqRQO+HhCyndQM8I4maxzh81uwLQ5CkGFM8Wi7uZa4gY8yOMqXt1wmzO/DdNWZxJWWiT52j33PQ/KQGIG8ukSu/2MzX2w0OyjpGoHYO5EaRGgQxJSEHsEK4jcY4V8md+470lfw+oF4XKl4wZj1k3EL0fjls4U6SkaeDQMCjVohmMGQF6haDKMcH1YoG55L8oSszT4OKLSv3aaPtVGx0kKB+IytofF8IxQ6OtDUfOqIR3xcGQoUF4NzFKNVZrrWCkXMX4f5mj6ikdCfjpeNf+6E1cfsIwIA1gfsbhRCvWTaEVKiJvI4JeEVh7QQKqbL1ZnKyhYZ3X+KP3bspo3VD5T2Zhy+FJm0DuB5wwt2Wg==; consentGroup=control; ga4_measurement_id_cookie=G-17NF7T4FBV; g_state={"i_p":1697389905703,"i_l":2}; __gads=ID=5f438ccdf5e21719:T=1697248249:RT=1697304633:S=ALNI_MYnt29eBwZo22zw-uFQDwwXPlJDpA; __gpi=UID=00000cba64b1dfdf:T=1697248249:RT=1697304633:S=ALNI_Mb_BpJv7dC0nNf9Q2lVRu58dvPQ9w; _scid_r=4b9a5be6-040d-43a6-a215-f79f85b4600f; cto_bundle=1_gGJ19qT2Nsb0JnWkozUUFybHpENCUyQklzTnZsc1Y4a1FmYlZTRVVtaGRwUmhlbmZPb0dnZ0JiRWxyMm5KZ3BMMmM0bGdTR3BaUFdYOUtPRnFJNFRtMWY5dTUyalpTVjc4eGw1bm1lTmViZnFRN0oxUHM5YjdxTzFtQXc0UEh1YVRQZ1hlVDdobkluT2lMUEt4VSUyQiUyQmJUWmw3QmclM0QlM0Q; _ga=GA1.2.816209843.1697248249; _ga_17NF7T4FBV=GS1.1.1697303505.2.1.1697304696.51.0.0; utag_main=v_id:018b2be0fd1b00017c609b36d6df05081002107900bd0$_sn:2$_se:116$_ss:0$_st:1697306496305$dc_visit:2$ses_id:1697303504582%3Bexp-session$_pn:16%3Bexp-session$dc_event:21%3Bexp-session$dc_region:eu-west-1%3Bexp-session; _sp_id.32cc=9f705803-fdc5-4a10-a349-9d26732cb66d.1697248247.2.1697304830.1697249606.78251eea-40d6-4bf4-8405-00068b49ef98; bm_sv=2655F1C79685AFA0853523DD8633A2AC~YAAQDuF6XPaeEh2LAQAApbSELxUbs1t+EUDUqkQyXaByhxCSMIHmGQ/hIG8ZPlXtjirXgq1/FXRkcJI40NF519veMMsapb06S5Pt7uPpZyCLTTFM/4l3t/i/oQNHpfDkLykSz3mudbQ3fj8jzmq7HEzc71gXrnxmQ8T4UkN0v/LxLP39HEcbL1GHgKYSAdK3FpmgGgF9sxxwy/YRuJSeGKR5rxzkCPbC/paqTXcdrYtZ4arN01frjIIXZMny96Bb9koBkfLh4WAn~1; _dd_s=',
        'Upgrade-Insecure-Requests': '1',
        'Sec-Fetch-User': '?1',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Ch-Ua-Platform': '"Windows"',
        'Sec-Ch-Ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"'
    }

    def start_requests(self):
        url = "https://www.propertyfinder.eg/_next/data/Z9-v0KFZneRKsJqc_lGVy/en/rent/properties-for-rent.html.json?page=4&categorySlug=rent&propertyTypeSlug=properties&saleType=for-rent&pattern=%2FcategorySlug%2FpropertyTypeSlug-saleType.html"
        yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)
    
    def parse(self, response):
        urls = response.css('a.property-card-module_property-card__link__L6AKb::attr(href)').getall()
        for url in urls:
            yield {'url': url}
            # yield scrapy.Request(url=url, callback=self.parseproperty)

