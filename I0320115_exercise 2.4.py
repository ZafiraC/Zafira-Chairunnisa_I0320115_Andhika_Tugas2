#menampilkan informasi program

print("Konversi suhu (Fahrenheit ke Celcius)")

#input suhu dalam fahrenheit
F = float(input("Masukkan suhu(fahrenheit): "))

#melakukan konversi suhu ke celcius
C = 5 * (F-32) / 9

#menampilkan hasil perhitungan ke layar
print("Fahrenheit: ", F)
print("Celcius: ", C)