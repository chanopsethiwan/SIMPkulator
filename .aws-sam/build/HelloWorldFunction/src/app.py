import json
from .reeracoenSpider import ReeracoenspiderSpider
from scrapy.crawler import CrawlerRunner
from twisted.internet import reactor

# import requests


def hello_world(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
        }),
    }

def reeracoenScrape(event, context):
    runner = CrawlerRunner()
    d = runner.crawl(ReeracoenspiderSpider)
    d.addBoth(lambda _: reactor.stop())
    try:
        reactor.run() # the script will block here until the crawling is finished
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Scrape completed",
            }),
        }
    except Exception as e:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "message": f"Scrape failed, {e}",
            }),
        }

