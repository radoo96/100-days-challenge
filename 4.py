# wypisuje od 0 
# gdybym chciał od 1 wpisuje (1, 5)

for i in range(5):
    print(i)

#Źle - ta sama zmienna 

cel = int(input("Ile dni zostało do twojego nawiększego celu? "))

for cel in range(1,7):
    print(f"Dzień {cel} - do dzieła")

#Dobrze

dni = int(input("Ile dni zostało do twojego największego celu? "))

for dzien in range(1, dni + 1):
    print(f"Dzień {dzien} - do dzieła")