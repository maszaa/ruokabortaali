# ruokabortaali
REST API ja webkäli TTY:llä sijaitsevien ravintoloiden ruokalistoille

## Ryhmän jäsenet
* Samuli Kohomäki / samuli.kohomaki@student.tut.fi
* Matti Hämäläinen / matti.m.hamalainen@student.tut.fi

## Idea
Yhdistetään TTY:llä sijaitsevien ravintoloiden APIen tarjoamat ruokalistatiedot REST APIksi ja luodaan tätä APIa hyödyntävä webclient.

## APIt
* Sodexo (Hertsi): http://www.sodexo.fi/ruokalistat/output/daily_json/12812/[vuosi]/[kk]/[pv]/fi
* Amica (Reaktori): http://www.amica.fi/modules/json/json/Index?costNumber=0812&firstDay=[vvvv-kk-pv]&lastDay=[vvvv-kk-pv]&language=fi

## Tekniikka
Django, Django REST, HTML, jQuery

## REST-rajapinnan dokumentaatio

### api/[vvvv]/[kk]/[pv]/?format=json
jossa *vvvv* on vuosi, *kk* kalenterikuukauden numero (01/1-12) ja *pv* kalenterikuukauden päivän numero (01/1-31)
* **HTTP Method:** GET
* **Content-Type:** application/json
* **Status code:**
  * 200: Pyyntö ok
  * 403: Virheellinen käyttäjän pyyntö
* **Paluuarvot:**
  * 200: Käyttäjän pyytämän päivän ruokalistat
  * 403: Virheilmoitus

### api/[vvvv]/[kk]/[pv]/[ravintola]/?format=json
jossa *vvvv* on vuosi, *kk* kalenterikuukauden numero (01/1-12), *pv* kalenterikuukauden päivän numero (01/1-31) ja *ravintola* Hertsi tai Reaktori (kirjainkoolla ei väliä)
* **HTTP Method:** GET
* **Content-Type:** application/json
* **Status code:**
  * 200: Pyyntö ok
  * 403: Virheellinen käyttäjän pyyntö
* **Paluuarvot:**
  * 200: Käyttäjän pyytämän ravintolan halutun päivän ruokalistat
  * 403: Virheilmoitus

### api/[vvvv]/[kk]/[pv]/[ravintola]/[linjasto]/?format=json
jossa *vvvv* on vuosi, *kk* kalenterikuukauden numero (01/1-12), *pv* kalenterikuukauden päivän numero (01/1-31), *ravintola* Hertsi tai Reaktori (kirjainkoolla ei väliä) ja *linjasto* warm salad, wok, soup, vegerarian, pizza, vitality tai popular ravintolan ollessa Hertsi, tai keittolounas, jälkiruoka, special, a´la carte, iltaruoka, leipäateria, smoothie, linjasto, kasvislounas tai salaattilounas ravintolan ollessa Reaktori
* **HTTP Method:** GET
* **Content-Type:** application/json
* **Status code:**
  * 200: Pyyntö ok
  * 403: Virheellinen käyttäjän pyyntö
* **Paluuarvot:**
  * 200: Käyttäjän pyytämän ravintolan linjaston halutun päivän ruokalistat
  * 403: Virheilmoitus

## Miten ajetaan
* Client-sovellus: https://ruokabortaali.herokuapp.com/
* Client-sovellus kiinteällä päiväyksellä (12.12.2016): https://ruokabortaali.herokuapp.com/test/
* REST API: https://ruokabortaali.herokuapp.com/api/
