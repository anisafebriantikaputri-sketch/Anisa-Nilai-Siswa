print("=== Masukkan Data Siswa ===")
nama = input("Nama Lengkap : ")
print(nama)
kelas = input("Kelas : ")
print(kelas)

nilai_ujian = int(input(f"Nilai Ujian {nama} : "))
print(nilai_ujian)
kehadiran = int(input(f"Persentase Kehadiran {nama} (%) : "))
print(kehadiran)

a = nilai_ujian >= 75
b = kehadiran >= 80
status_lulus = a and b

print("\n=== Data Siswa ===")
print(f"Nama Lengkap : {nama}")
print(f"Kelas : {kelas}")
print(f"Nilai : {nilai_ujian}")
print(f"Kehadiran : {kehadiran}%")

if status_lulus:
  print("Status : Selamat, anda DINYATAKAN LULUS!!")
else:
  print("Status : Maaf, anda DINYATAKAN TIDAK LULUS.")
