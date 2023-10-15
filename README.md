# Baigiamasis darbas

# Informacija:
Projekto tema: Lietuvos geografinės analizės projektas

Darbą paruošė: Kęstutis Čepulis
# Trumpas darbo aprašymas:

Darbas apima Lietuvos tvenkinius ir ežerus kuriuose buvo atliktas žuvų išteklių tyrimas. Visa informacija traukta iš tinklapio www.biip.lt

Darbui atlikti buvo naudota Python kalba, CSV failas ir Python bibliotekos: Pandas, Seaborn, Matplotlib.

Atlikti darbai projekte:
1. Duomenų ištraukimas iš CSV failo.
2. Duomenų papildymas į CSV failą.
3. Esamų duomenų formatavimas ir palyginimas.
4. Duomenų vizualizavimas grafikais.

# Main.py

Tai pagrindinis baigiamojo darbo failas, kuriame buvo atlikti visi duomenų ištraukimai, papildymai, vizualizacijos ir skaičiavimai.

Smulkus darbo aprašymas:
1. Pridėtas CSV failas į Python programą duomenų analizai iš tinklapio www.biip.lt
2. Kadangi su CSV faile trūko lentelių, kokie yra nurodyti www.biip.lt tinklapyje, buvo pridėti rankiniu būdu.
3. Pakeisti stulpelių pavadinimai į norimus naudojant rename komandą.
4. Formatuoti duomenys, kad būtų galima atlikti skaičiavimus. Iš "-" pakeista į "0" naudojant replace komandą.
5. Į pridėtus papildomus stulpelius pridėti reikiami rezultatai iš www.biip.lt tinklapio naudojant loc komandą.
6. Atlikti reikiami skaičiavimai ir sukurtas grafikas naudojant matplotlib.pyplot biblioteką ir bar grafiką. Grafikas nurodo, kiek ežerų ir tvenkinių buvo patikrinta tam tikruose rajonuose:
 
GrafikasNr.1  
![image](https://github.com/VerCyd/Final_Project/assets/144364760/6e8f46bc-ab0a-44e4-bf54-5a020c2fb7fe)

7. Lyginu kokią dalį plėšri žuvis sudaro visu sugautų žuvų kiekiu. Plėšrių žuvų biomasę procentais verčiame į kilogramus naudojan Pandas.
8. Kuriamas grafikas naudojan Seaborn bilbioteką ir lineplot grafiką, kuris nurodo, kaip keičiasi plėšių žuvų biomasė.
GrafikasNr2
![image](https://github.com/VerCyd/Final_Project/assets/144364760/d7fadf9c-51ac-44b9-8c33-1f159a290bf5)



