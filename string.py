tekst = "Anna, pawel, tomEK"

lista = tekst.split(",")
print(tekst)
print(lista)

imie = lista[0]
print(imie)
print(type(lista))


imieDuze = imie.upper()
print(imieDuze)
imieMale = imie.lower()
print(imieMale)


#sprawdzanie zawartosci
zawartosc = imie.isalpha()
print(zawartosc)

imie = ""
zawartosc = imie.isalpha()
print(zawartosc)

imie = "Julia"

print("\nDane użytkownika:\nMasz na imię: " + imie)


text1 = "Jan\n"
text2 = "Nowak\n"
print(text1 + text2)
text1 = text1.rstrip()
print(text1 + text2)
print(text1 + " " + text2)

#wyswietlanie łancucha znakow

#wszystkie wersje Pythona
text = "%s, Java i %s"%("PHP", "Python")
print(text)

#nowsze wersje Pythona 2.6 +
text = "{0}, Java i {1}".format("PHP", "Python")
print(text)

#help(text.replace)


new = text.replace("PHP", "C#")
print(new)

#wypisanie danych

rok = "2019"
miesiac = "marzec"
dzien = "23"

print("Data: ",end="")
print(dzien, miesiac, rok + "r")

print("Data: ",end="")
print(dzien, miesiac, rok + "r",sep="-")



print("\n")
