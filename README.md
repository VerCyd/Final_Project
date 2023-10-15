# Baigiamasis darbas

## Informacija:
Projekto tema: Lietuvos geografinės analizės projektas

Darbą paruošė: Kęstutis Čepulis
## Trumpas darbo aprašymas:

Darbas apima Lietuvos tvenkinius ir ežerus kuriuose buvo atliktas žuvų išteklių tyrimas. Visa informacija traukta iš tinklapio www.biip.lt

Darbui atlikti buvo naudota Python kalba, CSV failas ir Python bibliotekos: Pandas, Seaborn, Matplotlib, Plotly.

Atlikti darbai projekte:
1. Duomenų ištraukimas iš CSV failo.
2. Duomenų papildymas į CSV failą.
3. Esamų duomenų formatavimas ir palyginimas.
4. Duomenų vizualizavimas grafikais.

## Main.py

Tai pagrindinis baigiamojo darbo failas, kuriame buvo atlikti visi duomenų ištraukimai, papildymai, vizualizacijos ir skaičiavimai.

Smulkus darbo aprašymas:
1. Pridėtas CSV failas į Python programą duomenų analizei iš tinklapio www.biip.lt
2. Kadangi su CSV faile trūko lentelių, kokie yra nurodyti www.biip.lt tinklapyje, buvo pridėti rankiniu būdu.
3. Pakeisti stulpelių pavadinimai į norimus naudojant rename komandą.
4. Formatuoti duomenys, kad būtų galima atlikti skaičiavimus. Iš "-" pakeista į "0" naudojant replace komandą.
5. Į pridėtus papildomus stulpelius pridėti reikiami rezultatai iš www.biip.lt tinklapio naudojant loc komandą.
6. Atlikti reikiami skaičiavimai ir sukurtas grafikas naudojant matplotlib.pyplot biblioteką ir bar grafiką. Grafikas nurodo, kiek ežerų ir tvenkinių buvo patikrinta tam tikruose rajonuose:

GrafikasNr1:

![image](https://github.com/VerCyd/Final_Project/assets/144364760/6e8f46bc-ab0a-44e4-bf54-5a020c2fb7fe)

7. Lyginu kokią dalį plėšri žuvis sudaro su visų sugautų žuvų kiekiu. Plėšrių žuvų biomasę procentais verčiame į kilogramus naudojant Pandas.
8. Kuriamas grafikas naudojant Seaborn biblioteką ir lineplot grafiką, kuris nurodo, kaip keičiasi plėšrių žuvų biomasė.

GrafikasNr2:

![image](https://github.com/VerCyd/Final_Project/assets/144364760/d7fadf9c-51ac-44b9-8c33-1f159a290bf5)

9. Atliekami skaičiavimai ir su atliktais skaičiavimais kuriamas grafikas naudojant matplotlib.pyplot biblioteką ir pie grafiką. Grafikas vaizduoja koks yra žuvų paplitimas visuose tirtuose ežeruose ar tvenkiniuose.

GrafikasNr3:

![image](https://github.com/VerCyd/Final_Project/assets/144364760/de8af25c-e2bb-4743-8ad7-34631b415035)


10. Atliekami skaičiavimai ir su atliktais skaičiavimais kuriamas grafikas naudojant matplotlib.pyplot biblioteką ir pie grafiką. Grafikas vaizduoja kokia yra žuvų biomasė visuose tirtuose ežeruose ar tvenkiniuose.

GrafikasNr4:
![image](https://github.com/VerCyd/Final_Project/assets/144364760/ab9e62e0-a7d6-42c4-8ffe-aebc27ddfb96)


## Išvados:
Pagal atliktus tyrimus, galima teigti, kad daugiausia patikrintų ežerų ir tvenkinių buvo Ignalinos ir Molėtų rajonuose (nieko keisto, nes čia yra daugiausia ežerų).
Tyrimai rodo, kad plėšrios žuvys naikina neplėšrias žuvis, nes jų biomasė per metus laiko sparčiai pakilo. 
Atsižvialngiant į paskutiniuosius grafikus yra aišku, kad labiausiai paplitusi žuvis tirtuose ežeruose ar tvenkiniuose yra Kuoja, o antroje vietoje Plakis. Bet atsižvelgiant į žuvų biomasę, Plakis nukrenta į žemesnę vietą. Plakis sudaro tik 7% biomasės, kur Ešerys - 18%, Karšis - 8% ir Kuoja - 66%. Didesnis žuvies paplitimas nereiškia didesnės biomasės. Biomasė priklauso ir nuo žuvies svorio. 


# Kur žvejoti:
Darbas buvo atliktas kai uošvis pasigyrė pagavęs didelę žuvį Ignalinos rajone ir neatskleidė kokiame ežere pagavo.

## Trumpas darbo aprašymas:
Darbe naudotos bibliotekos: geocoder, carrier, folium, phonenumbers.

## Programa:
Programos tikslas: įvedus telefono numerį parodyti vietą kurioje žvejoja žvejys, parodytų kordinates. 

## Išvados:

Įvedus savo telefono numerį, rašo ne esamą operatorių, o koks buvo įsigyjus sim kortelę. Kordinates parodo irgi blogai. Įvedus gautas kordinates į google map's, rodo, kad aš esu prie Medininkų miške, nors mano telefonas yras su manimi ir aš esu Ignalinos rajone. 




