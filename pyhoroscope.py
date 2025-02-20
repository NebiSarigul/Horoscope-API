from lxml import html
import requests
from datetime import datetime, timezone

####################################################################
# API
####################################################################

class Horoscope:

    @staticmethod
    def get_todays_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/daily-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//div[@class=\"ms-3\"]/p/text()"))
        date = date.replace("']", "").replace("['", "")
        date_utc = datetime.now(timezone.utc)
        date_website = "-".join(date.split('-')[::-1])
        date_local = str(date_utc.astimezone()).split(' ')[0]

        horoscope = str(tree.xpath(
        "//p[@id=\"horo_content\"]/text()"))

        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        dict = {
            'date': date_website,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
    
    @staticmethod
    def get_tomorrow_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/tomorrow-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        date = str(tree.xpath(
            "//div[@class=\"ms-3\"]/p/text()"))
        date = date.replace("']", "").replace("['", "")
        date_utc = datetime.now(timezone.utc)
        date_website = "-".join(date.split('-')[::-1])
        date_local = str(date_utc.astimezone()).split(' ')[0]
        
        horoscope = str(tree.xpath(
        "//p[@id=\"horo_content\"]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("[\"", "").replace("\"]", "").replace("[\'", "").replace("\']", "")
        dict = {
            'date': date_website,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_weekly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/weekly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        week = str(tree.xpath(
            "//div[@class=\"ms-3\"]/p/text()"))
        week = week.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
        "//p[@id=\"horo_content\"]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'week': week,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_monthly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/monthly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        month = str(tree.xpath(
            "//div[@class=\"ms-3\"]/p/text()"))
        month = month.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
        "//p[@id=\"horo_content\"]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'month': month,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict

    @staticmethod
    def get_yearly_horoscope(sunsign):
        url = "http://www.ganeshaspeaks.com/horoscopes/yearly-horoscope/" + sunsign
        response = requests.get(url)
        tree = html.fromstring(response.content)
        year = str(tree.xpath(
            "//div[@class=\"ms-3\"]/p/text()"))
        year = year.replace("']", "").replace("['", "")
        horoscope = str(tree.xpath(
        "//p[@id=\"horo_content\"]/text()"))
        horoscope = horoscope.replace("\\n", "").replace("  ", "").replace("']", "").replace("['", "")
        dict = {
            'year': year,
            'horoscope': horoscope,
            'sunsign': sunsign
        }

        return dict
