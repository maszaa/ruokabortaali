import requests
import datetime

class Hertsi:
    def __init__(self, url, day):
        self.uri = url
        self.menu = {"menu" : {}, "uri" : self.uri}
        url = "http://www.sodexo.fi/ruokalistat/output/daily_json/12812/" + day.year + "/" + day.month + "/" + day.day + "/fi"

        response = requests.req(url)

        if response.status_code == 200:
            jsonMenu = response.json()['courses']
                if jsonMenu.amount != 0:
                for item in jsonMenu:
                    self.menu["menu"][item["category"]] = {"nimi": item["title_fi"], "hinta": item["price"].replace(" ", ""), "lisätiedot": item["properties"]}
        else:
            raise ValueError("Virheelliset parametrit tai Sodexon API saavuttamattomissa.")

    def getAll(self):
        return self.menu

    def getOneMenu(self, menu):
        try:
            oneMenu = {menu : self.menu[menu], uri : self.menu[uri]}
            return oneMenu
        except KeyError:
            raise KeyError("Virheellinen menu.")
