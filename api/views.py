from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import datetime
from api.hertsi import *
from api.reaktori import *

class DayMenuView(APIView):
    def get(self, request, year, month, day):
        try:
            day = datetime.date(year=int(year), month=int(month), day=int(day))
            formatString = ""
            fullUrl = request.build_absolute_uri()

            if "?format=json" in fullUrl:
                fullUrl = fullUrl.split("?")[0]
                formatString = "?format=json"

            hertsi = Hertsi(fullUrl + "Hertsi/" + formatString, day)
            reaktori = Reaktori(fullUrl + "Reaktori/" + formatString, day)
            menus = {"ravintolat" : [hertsi.getAll(), reaktori.getAll()], "uri": request.build_absolute_uri()}
            response = Response(menus, status=status.HTTP_200_OK)
            return response
        except (KeyError, ValueError) as error:
            response = Response({"Virhe": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            return response

class RestaurantMenuView(APIView):
    def get(self, request, year, month, day, restaurant):
        try:
            day = datetime.date(year=int(year), month=int(month), day=int(day))
            menu = {}
            if (restaurant.lower() == "hertsi"):
                hertsi = Hertsi(request.build_absolute_uri(), day)
                menu = hertsi.getAll()
            elif (restaurant.lower() == "reaktori"):
                reaktori = Reaktori(request.build_absolute_uri(), day)
                menu = reaktori.getAll()
            else:
                raise ValueError("Virheellinen ravintola.")
            response = Response(menu, status=status.HTTP_200_OK)
            return response
        except (KeyError, ValueError) as error:
            response = Response({"Virhe": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            return response

class RestaurantOneMenuView(APIView):
    def get(self, request, year, month, day, restaurant, menuName):
        try:
            day = datetime.date(year=int(year), month=int(month), day=int(day))
            menu = {}
            if (restaurant.lower() == "hertsi"):
                hertsi = Hertsi(request.build_absolute_uri(), day)
                menu = hertsi.getOneMenu(menuName)
            elif (restaurant.lower() == "reaktori"):
                reaktori = Reaktori(request.build_absolute_uri(), day)
                menu = reaktori.getOneMenu(menuName)
            else:
                raise ValueError("Virheellinen ravintola tai linjasto.")
            response = Response(menu, status=status.HTTP_200_OK)
            return response
        except (KeyError, ValueError) as error:
            response = Response({"Virhe": str(error)}, status=status.HTTP_400_BAD_REQUEST)
            return response
