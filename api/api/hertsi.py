import requests
import datetime

class Hertsi:
    def __init__(self, url, day):
        self.uri = url
        self.menu = {"ravintola": "Hertsi", "linjastot" : {}, "uri" : self.uri}
        url = "http://www.sodexo.fi/ruokalistat/output/daily_json/12812/" + str(day.year) + "/" + str(day.month) + "/" + str(day.day) + "/fi"

        response = requests.get(url)

        if response.status_code == 200:
            jsonMenu = response.json()['courses']
            if len(jsonMenu) != 0:
                for item in jsonMenu:
                    self.menu["linjastot"][item["category"].lower()] = {"nimi": item["title_fi"], "hinta": item["price"].replace(" ", "")}
                    if "properties" in item:
                        self.menu["linjastot"][item["category"].lower()]["lisätiedot"] = item["properties"]
        else:
            raise ValueError("Virheelliset parametrit tai Sodexon API saavuttamattomissa.")

    def getAll(self):
        return self.menu

    def getOneMenu(self, menu):
        try:
            oneMenu = {"ravintola": "Hertsi", menu : self.menu["linjastot"][menu.lower()], "uri" : self.menu["uri"]}
            return oneMenu
        except KeyError:
            raise KeyError("Virheellinen menu.")
