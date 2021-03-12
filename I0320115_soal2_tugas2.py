print("-------------------")
print(" Identitas Pribadi ")
print("-------------------")

nama = "Zafira Chairunnisa"
tempat_lahir = "Surakarta"
tanggal_kelahiran = "11 Mei 2002"
anak_ke = "2"
saudara = "3"
alamat = "Jl. Jetis Permai Gang 5, Gentan, Baki, Sukoharjo"
sekolah = "Universitas Sebelas Maret"
fakultas = "Teknik"
program_studi = "Teknik Industri"
tinggi_badan = "165 cm"
berat_badan = "65.5 kg"
ukuran_sepatu = "39 cm"

#kelahiran
tanggal_lahir = 11
bulan_lahir = 5
tahun_lahir = 2002

#usia
tanggal_sekarang = 12
bulan_sekarang = 3
tahun_sekarang = 2021

usia = (tanggal_sekarang - tanggal_lahir) + ((bulan_sekarang - bulan_lahir)*30) + ((tahun_sekarang - tahun_lahir)*365)
hari = int(((usia)%365)/30)
bulan = int(((usia)%365)/30)
tahun = int((usia)/365)

print("Perkenalkan nama saya", nama, "Saya lahir di", tempat_lahir, "pada tanggal", tanggal_kelahiran, "Umur saya sekarang adalah", tahun, "tahun,", bulan, "bulan,", hari, "hari.")
print("Saya anak ke", anak_ke, "dari", saudara, "bersaudara.", "Saya beserta keluarga tinggal di", alamat)
print("Saya sekolah di", sekolah, "Fakultas", fakultas, "Program Studi", program_studi, "Angkatan 2020")
print("Saya termasuk anak yang memiliki tinggi badan yang tinggi yaitu", tinggi_badan, "dengan berat badan", berat_badan, "dan ukuran sepatu saya adalah", ukuran_sepatu)



