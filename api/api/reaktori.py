import requests
import datetime
from sets import Set

class Reaktori:
    def __init__(self, url, day):
        self.uri = url
        self.menu = {"ravintola" : "Reaktori", "menu" : {}, "uri" : self.uri}
        url = "http://www.amica.fi/modules/json/json/Index?costNumber=0812&firstDay=" + day.year + "-" + day.month + "-" + day.day +
                "&lastDay=" + day.year + "-" + day.month + "-" + day.day + "&language=fi"

        response = requests.req(url)

        if response.status_code == 200:
            jsonWeekMenu = response.json()['MenusForDays']
            for weekday in jsonWeekMenu:
                if str(day.year + "-" + day.month + "-" + day.day) in weekday["Date"]:
                    jsonMenu = weekday["SetMenus"]
                        for item in jsonMenu:
                            names = item["Components"]
                            foodName = ""
                            foodProperties = ""
                            foodPropertiesSet = Set()
                            for name in names:
                                partialNameProperties = name.split("(")
                                partialName = partialNameProperties[0]
                                partialProperties = nameProperties[1].replace(")", "").replace(" ", "").split(",")
                                    for property_ in partialProperties:
                                        foodProperties.add(property_)

                                if foodName == "":
                                    foodName = partialName
                                else:
                                    foodname += "& " + partialName
                                foodProperties = str.join(",", foodPropertiesSet)

                            self.menu["menu"][item["Name"]] = {"nimi": foodName, "hinta": item["Price"].replace("€", ""), "lisätiedot": foodProperties}
        else:
            raise ValueError("Virheelliset parametrit tai Amican API saavuttamattomissa.")

    def getAll(self):
        return self.menu

    def getOneMenu(self, menu):
        try:
            oneMenu = {"ravintola": "Reaktori", menu : self.menu[menu], uri : self.menu[uri]}
            return oneMenu
        except KeyError:
            raise KeyError("Virheellinen menu.")
