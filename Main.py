# Importuojame Python bibliotekas:
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Duomenys paimti iš CSV failo, iš tinklapio www.biip.lt:
data = pd.read_csv('Ezerai_ir_zuvys.csv')
df = pd.DataFrame(data)

# Pridedame papildomus stulpelius rankiniu būdu į CSV failą:
# df["Kuoju Gausumas"] = 0
# df["Kuoju Biomase"] = 0
# df["Plakis Gausumas"] = 0
# df["Plakis Biomase"] = 0
# df["Raude Gausumas"] = 0
# df["Raude Biomase"] = 0
# df["Pugzlys Gausumas"] = 0
# df["Pugzlys Biomase"] = 0
# df.to_csv("Ezerai_ir_zuvys.csv", index=False)

# Keičiame/koreguojame stulpelių pavadinimus:
# df = df.rename(columns={"Biomase (kg)i": "Biomase, kg", "Gausumas (vnt.)i": "Gausumas (vnt)",
#                         "Plesriu zuvu gausumas (%)i": "Plesriu zuvu (gausumas), %", "Plesriu zuvu biomase (%)i":
#                         "Plesriu zuvu (biomase), %", "Karsis_Gausumas": "Karsis (Gausumas)", "Eserys(Gausumas)":
#                         "Eserys (Gausumas)", "Kuoju Gausumas": "Kuoja (Gausumas)", "Kuoju Biomase": "Kuoja (Biomase)",
#                         "Plakis Gausumas": "Plakis (Gausumas)", "Plakis Biomase": "Plakis (Biomase)",
#                         "Raude Gausumas": "Raude (Gausumas)", "Raude Biomase": "Raude (Biomase)", "Pugzlys Gausumas":
#                         "Pugzlys (Gausumas)", "Pugzlys Biomase": "Pugzlys (Biomase)",
#                         "zuvu istekliu bukles indeksasi": "Zuvu istekliu bukles indeksai"}, inplace=False)
# df.to_csv("Ezerai_ir_zuvys.csv", index=False)

# Formatuojame esamus rezultatus lentelėje:
# df["Eserys (Gausumas)"] = df["Eserys (Gausumas)"].replace({"-": 0})
# df["Karsis (Gausumas)"] = df["Karsis (Gausumas)"].replace({"-": 0})
# df.to_csv("Ezerai_ir_zuvys.csv", index=False)

# Koreguojame naujuose stulpeliuose reikšmes, rankiniu būdu, paimdami jas iš tinklapio www.biip.lt:
# df.loc[df["Vandens telkinio pavadinimas"] == "Aisetas", "Kuoja (Gausumas)"] = 10
# df.loc[df["Vandens telkinio pavadinimas"] == "Alnis", "Kuoja (Gausumas)"] = 23.1
# df.loc[df["Vandens telkinio pavadinimas"] == "Antakmeniu ezeras", "Kuoja (Gausumas)"] = 81.5
# df.loc[df["Vandens telkinio pavadinimas"] == "Antanavo HE tvenkinys", "Kuoja (Gausumas)"] = 27
# df.loc[df["Vandens telkinio pavadinimas"] == "Aukstadvario HE tvenkinys", "Kuoja (Gausumas)"] = 20
# df.loc[df["Vandens telkinio pavadinimas"] == "Gavys", "Kuoja (Gausumas)"] = 46
# df.loc[df["Vandens telkinio pavadinimas"] == "Juodieji Lakajai", "Kuoja (Gausumas)"] = 15.4
# df.loc[df["Vandens telkinio pavadinimas"] == "Kretuonas", "Kuoja (Gausumas)"] = 16
# df.loc[df["Vandens telkinio pavadinimas"] == "Luokesai", "Kuoja (Gausumas)"] = 15.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Lenas", "Kuoja (Gausumas)"] = 63.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Lusiai", "Kuoja (Gausumas)"] = 7.2
# df.loc[df["Vandens telkinio pavadinimas"] == "Mastis", "Kuoja (Gausumas)"] = 48
# df.loc[df["Vandens telkinio pavadinimas"] == "Prutas", "Kuoja (Gausumas)"] = 31
# df.loc[df["Vandens telkinio pavadinimas"] == "Sablauskiu tvenkinys", "Kuoja (Gausumas)"] = 53.8
# df.loc[df["Vandens telkinio pavadinimas"] == "Spindzius", "Kuoja (Gausumas)"] = 42.2
# df.loc[df["Vandens telkinio pavadinimas"] == "Utenos tvenkinys", "Kuoja (Gausumas)"] = 47.5
# df.loc[df["Vandens telkinio pavadinimas"] == "Cicirys", "Kuoja (Gausumas)"] = 17.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Slavantas", "Kuoja (Gausumas)"] = 19.4

# df.loc[df["Vandens telkinio pavadinimas"] == "Aisetas", "Kuoja (Biomase)"] = 0.614
# df.loc[df["Vandens telkinio pavadinimas"] == "Alnis", "Kuoja (Biomase)"] = 1.794
# df.loc[df["Vandens telkinio pavadinimas"] == "Antakmeniu ezeras", "Kuoja (Biomase)"] = 2.236
# df.loc[df["Vandens telkinio pavadinimas"] == "Antanavo HE tvenkinys", "Kuoja (Biomase)"] = 4.854
# df.loc[df["Vandens telkinio pavadinimas"] == "Aukstadvario HE tvenkinys", "Kuoja (Biomase)"] = 1.523
# df.loc[df["Vandens telkinio pavadinimas"] == "Gavys", "Kuoja (Biomase)"] = 2.370
# df.loc[df["Vandens telkinio pavadinimas"] == "Juodieji Lakajai", "Kuoja (Biomase)"] = 1.282
# df.loc[df["Vandens telkinio pavadinimas"] == "Kretuonas", "Kuoja (Biomase)"] = 0.564
# df.loc[df["Vandens telkinio pavadinimas"] == "Luokesai", "Kuoja (Biomase)"] = 0.656
# df.loc[df["Vandens telkinio pavadinimas"] == "Lenas", "Kuoja (Biomase)"] = 1.411
# df.loc[df["Vandens telkinio pavadinimas"] == "Lusiai", "Kuoja (Biomase)"] = 0.490
# df.loc[df["Vandens telkinio pavadinimas"] == "Mastis", "Kuoja (Biomase)"] = 2.198
# df.loc[df["Vandens telkinio pavadinimas"] == "Prutas", "Kuoja (Biomase)"] = 1.400
# df.loc[df["Vandens telkinio pavadinimas"] == "Sablauskiu tvenkinys", "Kuoja (Biomase)"] = 1.817
# df.loc[df["Vandens telkinio pavadinimas"] == "Spindzius", "Kuoja (Biomase)"] = 2.967
# df.loc[df["Vandens telkinio pavadinimas"] == "Utenos tvenkinys", "Kuoja (Biomase)"] = 3.380
# df.loc[df["Vandens telkinio pavadinimas"] == "Cicirys", "Kuoja (Biomase)"] = 3.913
# df.loc[df["Vandens telkinio pavadinimas"] == "Slavantas", "Kuoja (Biomase)"] = 1.584

# df.loc[df["Vandens telkinio pavadinimas"] == "Almajas", "Plakis (Gausumas)"] = 15.4
# df.loc[df["Vandens telkinio pavadinimas"] == "Atesys", "Plakis (Gausumas)"] = 9.8
# df.loc[df["Vandens telkinio pavadinimas"] == "Aviris", "Plakis (Gausumas)"] = 7.4
# df.loc[df["Vandens telkinio pavadinimas"] == "Baltosios Ancios tvenkinys", "Plakis (Gausumas)"] = 23.1
# df.loc[df["Vandens telkinio pavadinimas"] == "Dvariuku tvenkinys", "Plakis (Gausumas)"] = 30.8
# df.loc[df["Vandens telkinio pavadinimas"] == "Galuonai", "Plakis (Gausumas)"] = 4.4
# df.loc[df["Vandens telkinio pavadinimas"] == "Isnarai", "Plakis (Gausumas)"] = 14.9
# df.loc[df["Vandens telkinio pavadinimas"] == "Kertuojai", "Plakis (Gausumas)"] = 22
# df.loc[df["Vandens telkinio pavadinimas"] == "Lukstas", "Plakis (Gausumas)"] = 48
# df.loc[df["Vandens telkinio pavadinimas"] == "Viesintas", "Plakis (Gausumas)"] = 10
# df.loc[df["Vandens telkinio pavadinimas"] == "Zarasas", "Plakis (Gausumas)"] = 5.4

# df.loc[df["Vandens telkinio pavadinimas"] == "Almajas", "Plakis (Biomase)"] = 0.284
# df.loc[df["Vandens telkinio pavadinimas"] == "Atesys", "Plakis (Biomase)"] = 0.286
# df.loc[df["Vandens telkinio pavadinimas"] == "Aviris", "Plakis (Biomase)"] = 0.133
# df.loc[df["Vandens telkinio pavadinimas"] == "Baltosios Ancios tvenkinys", "Plakis (Biomase)"] = 0.492
# df.loc[df["Vandens telkinio pavadinimas"] == "Dvariuku tvenkinys", "Plakis (Biomase)"] = 0.977
# df.loc[df["Vandens telkinio pavadinimas"] == "Galuonai", "Plakis (Biomase)"] = 0.067
# df.loc[df["Vandens telkinio pavadinimas"] == "Isnarai", "Plakis (Biomase)"] = 0.180
# df.loc[df["Vandens telkinio pavadinimas"] == "Kertuojai", "Plakis (Biomase)"] = 0.353
# df.loc[df["Vandens telkinio pavadinimas"] == "Lukstas", "Plakis (Biomase)"] = 0.751
# df.loc[df["Vandens telkinio pavadinimas"] == "Viesintas", "Plakis (Biomase)"] = 0.274
# df.loc[df["Vandens telkinio pavadinimas"] == "Zarasas", "Plakis (Biomase)"] = 0.196

# df.loc[df["Vandens telkinio pavadinimas"] == "Arinas", "Raude (Gausumas)"] = 4.1
# df.loc[df["Vandens telkinio pavadinimas"] == "Utenykstis", "Raude (Gausumas)"] = 1.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Vajuonis", "Raude (Gausumas)"] = 1.3

# df.loc[df["Vandens telkinio pavadinimas"] == "Arinas", "Raude (Biomase)"] = 0.153
# df.loc[df["Vandens telkinio pavadinimas"] == "Utenykstis", "Raude (Biomase)"] = 0.135
# df.loc[df["Vandens telkinio pavadinimas"] == "Vajuonis", "Raude (Biomase)"] = 0.135

# df.loc[df["Vandens telkinio pavadinimas"] == "Apvardai", "Pugzlys (Gausumas)"] = 4.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Labunavos tvenkinys", "Pugzlys (Gausumas)"] = 14.8
# df.loc[df["Vandens telkinio pavadinimas"] == "Paezeriu ezeras", "Pugzlys (Gausumas)"] = 3.5
# df.loc[df["Vandens telkinio pavadinimas"] == "Pravalas", "Pugzlys (Gausumas)"] = 1.3
# df.loc[df["Vandens telkinio pavadinimas"] == "Snaigynas", "Pugzlys (Gausumas)"] = 1.0

# df.loc[df["Vandens telkinio pavadinimas"] == "Apvardai", "Pugzlys (Biomase)"] = 0.041
# df.loc[df["Vandens telkinio pavadinimas"] == "Labunavos tvenkinys", "Pugzlys (Biomase)"] = 0.172
# df.loc[df["Vandens telkinio pavadinimas"] == "Paezeriu ezeras", "Pugzlys (Biomase)"] = 0.058
# df.loc[df["Vandens telkinio pavadinimas"] == "Pravalas", "Pugzlys (Biomase)"] = 0.029
# df.loc[df["Vandens telkinio pavadinimas"] == "Snaigynas", "Pugzlys (Biomase)"] = 0.011
# df.to_csv("Ezerai_ir_zuvys.csv", index=False)

# Sukuriamas grafiką, patikrintų ežerų ir tvenkinių kiekis rajonuose:
x = df.groupby("Savivaldybe").count()
total = df["Vandens telkinio pavadinimas"].max()
plt.bar(x.index, x["Vandens telkinio pavadinimas"], color="darkred", edgecolor="black")
plt.ylim(0, 10)
plt.xlabel("Rajonai")
plt.xticks(rotation=90)
plt.subplots_adjust(bottom=0.35, top=0.85)
plt.ylabel("Ežerų ir tvenkinių kiekis")
plt.title("Suskaičiuoti patikrinti ežerai ir tvenkiniai pagal rajonus")
# plt.savefig("GrafikasNr1.png")
plt.show()

# Lyginame kokią dalį užima plėšri žuvis pagal visų sugautų žuvų kiekį:
biomase_kg = 100
df["Plesrios(kg)"] = (df["Biomase, kg"] * df["Plesriu zuvu biomase, %"] / biomase_kg).round(3)
df.head(10)
df.to_csv("Ezerai_ir_zuvys.csv", index=False)

# Sukuriamas grafikas biomase pagal plėšrias žuvis:
sns.lineplot(data=df, x="Plesrios(kg)", y="Biomase, kg")
plt.title("Biomasė pagal plėšrias žuvis")
# plt.savefig("GrafikasNr2.png")
plt.show()

# Kuriamas grafikas, kiek kokių žuvų yra gausiausia:
data1 = df["Eserys (Gausumas)"].sum()
data2 = df["Karsis (Gausumas)"].sum()
data3 = df["Kuoja (Gausumas)"].sum()
data4 = df["Plakis (Gausumas)"].sum()
data5 = df["Raude (Gausumas)"].sum()
data6 = df["Pugzlys (Gausumas)"].sum()
labels = ["Ešerys", "Karšis", "Kuoja", "Plakis", "Raudė", "Pugžlys"]
plt.pie([data1, data2, data3, data4, data5, data6], labels=labels, autopct="%1.1f%%",
        colors=sns.color_palette("Set2"))
plt.title("Žuvų paplitimas")
# plt.savefig("GrafikasNr3.png")
plt.show()

# Kuriamas grafikas, žuvys užimančios dydžiausią biomasės dalį:
data1 = df["Eserys (Biomase)"].sum()
data2 = df["Karsis (Biomase)"].sum()
data3 = df["Kuoja (Biomase)"].sum()
data4 = df["Plakis (Biomase)"].sum()
data5 = df["Raude (Biomase)"].sum()
data6 = df["Pugzlys (Biomase)"].sum()
labels = ["Ešerys", "Karšis", "Kuoja", "Plakis", "Raudė", "Pugžlys"]
explode = [0.05, 0.05, 0.05, 0.05, 0.05, 0.05]
plt.pie([data1, data2, data3, data4, data5, data6], labels=labels, autopct="%.0f%%",
        colors=sns.color_palette("pastel"), explode=explode, pctdistance=0.80, startangle=90)
hole = plt.Circle((0, 0), 0.65, facecolor="white")
plt.gcf().gca().add_artist(hole)
plt.title("Žuvys užimančios dydžiausią biomasę")
# plt.savefig("GrafikasNr4.png")
plt.show()
