
# Napisz kod, który pyta użytkownika o ocenę z testu (od 1 do 6) i sprawdza, czy jest ona powyżej lub równa 4.
# Jeśli tak, to program powinien wyświetlić "Gratulacje, zdałeś!", w przeciwnym razie "Niestety, nie zdałeś.".
# (Pamiętaj, żeby ocenę pobierać jako liczbę)

ocena = int(input("Wpisz ocenę z testu: "))

if ocena >= 4:
        print("Gratulację zdałeś!")
else:
    if ocena <= 4:
        print("niestety nie tym razem")
