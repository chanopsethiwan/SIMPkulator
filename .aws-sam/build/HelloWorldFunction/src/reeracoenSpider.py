import scrapy
import boto3
import urllib.request
import os
from .reeracoenHtmlTable import ReeracoenPynamoHtml
import json

class ReeracoenspiderSpider(scrapy.Spider):
    name = "reeracoenspider"
    start_urls = ["https://www.reeracoen.co.th/th/jobs"]
    # start_urls = []
    # for i in range(1,97):
    #     start_urls.append(f"https://www.reeracoen.co.th/th/jobs?page={i}") 
    def parse(self, response):
        products = response.css('span.id')
        for product in products:
            jobId = product.css('span.id::text').get().replace('รหัส:', '')
            link = f"https://www.reeracoen.co.th/en/jobs/{jobId}"
            iterator = ReeracoenPynamoHtml.query(link)
            html_list = list(iterator)
            lst = []
            for html in html_list:
                lst.append(html.returnJson())
            if len(lst) != 0:
                return {
            "statusCode": 200,
            "body": json.dumps({
                "message": 'Stopping scrape, found duplicated Url',
            })}
            htmlItem = ReeracoenPynamoHtml(html = link)
            htmlItem.save()
            linkFileName = f'{link.replace("/", "Œ")}.html'
            urllib.request.urlretrieve(link, f'/tmp/{linkFileName}') #must use tmp folder for editing files
            s3 = boto3.client('s3')
            s3.put_object(Bucket=os.environ.get('S3_BUCKET'), Key=linkFileName, Body=open(f"/tmp/{linkFileName}", "rb") )
            yield{
                'url' : link
            }