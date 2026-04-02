total_hari=int(input("Masukan Jumlah Hari Proyek (x) :"))
tahun= total_hari // 365
sisa_setelah_tahun= total_hari % 365
bulan= sisa_setelah_tahun // 30
hari= sisa_setelah_tahun %30

print("_" * 30)
print(f"Hasil Konversi untuk {total_hari} hari :")
print(f"tahun : {tahun}")
print(f"bulan : {bulan}")
print(f"hari : {hari}")
print("_" * 30)