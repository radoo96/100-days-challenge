godziny = int(input("Ile godzin tygodniowo? "))

if godziny >= 15:
    print("MEGA!!!!")
elif godziny >= 7:
    print("Bardzo dobrze! Tak się buduje nawyk")
else:
    print("Za mało, popraw")

ocena = int(input("Ile dostałem z egzaminu (0 - 100)? "))
if ocena >= 90:
    print("Świętnie!!!")
elif ocena >= 50 < 90:
    print("Tak trzymaj")
else:
    print("Do poprawki")