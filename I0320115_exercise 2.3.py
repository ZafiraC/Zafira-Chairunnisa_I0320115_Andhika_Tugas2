import math

#menampilkan informasi program
print("luas dan keliling lingkaran")

#input nilai jari-jari
r = float(input("Masukkan niali jari-jari: "))

#menghitung luas lingkaran
luas_lingkaran = 3.14 * (r ** 2)

#menghitung keliling lingkaran
keliling_lingkaran = 2 * 3.14 * r

#menampilkan hasil perhitungan ke layar
print("luas lingkaran: ", luas_lingkaran)
print("keliling lingkaran: ", keliling_lingkaran)