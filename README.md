# ruokabortaali
REST API ja webkäli TTY:llä sijaitseville ravintoloille

## Idea
Yhdistetään TTY:llä sijaitsevien ravintoloiden APIen tarjoamat tiedot REST APIksi ja luodaan tätä APIa hyödyntävä webclient.

## APIt
* Sodexo (Hertsi): http://www.sodexo.fi/ruokalistat/output/daily_json/12812/[vuosi]/[kk]/[pv]/fi
* Amica (Reaktori): http://www.amica.fi/modules/json/json/Index?costNumber=0812&firstDay=[alkamispäivä]&lastDay=[loppumispäivä]&language=fi
* jos aika riittää - Juvenes (Newton & Konehuone: http://www.juvenes.fi/DesktopModules/Talents.LunchMenu/LunchMenuServices.asmx/GetMenuByWeekday?KitchenId=[ravintolaId]&MenuTypeId=[menuId]&Week=[vkoNro]&Weekday=[vkoPv]&lang='fi'&format=json

## Tekniikka
Django, Django REST, jade
