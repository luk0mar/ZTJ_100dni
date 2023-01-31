# string to ciąg tekstowy stąd łączy dwa teksty zawarte w ""
print(12 + 12)
print("12" + "12")

# sprawdzamy dlugosc znakow - len()
x = "Python jest super"
print(len(x))

# wyciągamy dany ciąg tekstowy z X
x = "Python jest super"
print(x[2:5])

# \n powoduje przejscie do nowej lini
print("Zero\nTo\nJunior")

# wydruk pustej linii
print()

# nowa linia i tab (wciecie)
print("Zero\nTo\n Junior\t i tabulacja")

# \ powoduje ze znak zostanie wydrukowany - nie bedzie interpretowany
print('"Zero" to "Junior"')

# przecinki są potraktowane jako spacje
print("Zero", "to", "Junior", 10000)

# przejście do nowych linii
print(
    """
Hej
co
tam
w Zero to Junior?
"""
)
