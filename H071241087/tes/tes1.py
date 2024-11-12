try:
    jarak = int(input("Masukkan jarak : "))
except ValueError:
    print("Jarak harus bertipe integer")
    jarak = int(input("Masukkan jarak : "))

if 1 <= jarak <= 10:
    biaya = 10000

    print(biaya)
elif 11 <= jarak <= 20:
    biaya = 10000
    jarak -= 10
    biaya += jarak * 2500

    print(biaya)
elif 21 <= jarak <= 35:
    biaya = 10000
    jarak -= 20
    biaya += 10 * 2500 + jarak * 1000

    print(biaya)
elif 36 <= jarak <= 40:
    biaya = 50000

    print(biaya)
elif jarak > 41:
    print("Diluar jangkauan")
else:
    print("Jarak tidak valid")