import requests
import datetime
import json

class Reaktori:
    def __init__(self, url, day):
        self.uri = url
        self.menu = {"ravintola" : "Reaktori", "linjastot" : {}, "uri" : self.uri}
        url = "http://www.amica.fi/modules/json/json/Index?costNumber=0812&firstDay=" + str(day.year) + "-" + str(day.month) + "-" + str(day.day) + "&lastDay=" + str(day.year) + "-" + str(day.month) + "-" + str(day.day) + "&language=fi"

        response = requests.get(url)
        if response.status_code == 200:
            jsonWeekMenu = response.json()["MenusForDays"]
            for weekday in jsonWeekMenu:
                if '{:%Y-%m-%d}'.format(day) in weekday["Date"]:
                    jsonMenu = weekday["SetMenus"]
                    for item in jsonMenu:
                        names = item["Components"]
                        foodName = ""
                        foodProperties = ""
                        foodPropertiesSet = set()
                        for name in names:
                            partialNameProperties = name.split("(")
                            partialName = partialNameProperties[0]
                            partialProperties = partialNameProperties[1].replace(")", "").replace(" ", "").split(",")
                            for property_ in partialProperties:
                                foodPropertiesSet.add(property_)

                            if foodName == "":
                                foodName = partialName
                            else:
                                foodName += "& " + partialName
                            foodProperties = str.join(", ", foodPropertiesSet)

                        self.menu["linjastot"][item["Name"].lower().lower()] = {"nimi": foodName.rstrip(), "hinta": item["Price"].replace("€", ""), "lisätiedot": foodProperties}
        else:
            raise ValueError("Virheelliset parametrit tai Amican API saavuttamattomissa.")

    def getAll(self):
        return self.menu

    def getOneMenu(self, menu):
        try:
            oneMenu = {"ravintola": "Reaktori", menu : self.menu["linjastot"][menu], "uri" : self.menu["uri"]}
            return oneMenu
        except KeyError:
            raise KeyError("Virheellinen menu.")
