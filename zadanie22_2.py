# Napisz kod, który pyta użytkownika o wiek i sprawdza, czy jest on pełnoletni.
# Jeśli tak, to program powinien wyświetlić "Jesteś pełnoletni!", w przeciwnym razie "Nie jesteś jeszcze pełnoletni.".
# (Pamiętaj, żeby wiek pobierać jako liczbę).


wiek = int(input("Podaj swój wiek: "))

if wiek <= 18:
    print("Nie jesteś jeszcze pełnoletni.")
else:
    if wiek >= 18:
        print("Jesteś pełnoletni!")