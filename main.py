import random


karakterler = "+-/*!&$#?=@abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

parola_uzunlugu = int(input("Parolanızın uzunluğunu girin: "))


parola = ""

for _ in range(parola_uzunlugu):
    parola += random.choice(karakterler)

print("Oluşturulan Parola: ", parola)
