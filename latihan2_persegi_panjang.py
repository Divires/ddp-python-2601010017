# latihan2_persegi_panjang.py

panjang = float(input("Masukkan panjang: "))
lebar = float(input("Masukkan lebar: "))

luas = panjang * lebar
keliling = 2 * (panjang + lebar)

print(f"Luas : {luas} m2")
print(f"Keliling : {keliling} m")

# --- TRACE TABLE ---
# Langkah | panjang | lebar | luas | keliling | Output / Aksi
# -------------------------------------------------------------
# 1       | -       | -     | -    | -        | Meminta input panjang & lebar
# 2       | 8       | 5     | -    | -        | Menyimpan nilai input
# 3       | 8       | 5     | 40.0 | -        | Menghitung luas (8 * 5)
# 4       | 8       | 5     | 40.0 | 26.0     | Menghitung keliling (2 * (8 + 5))
# 5       | 8       | 5     | 40.0 | 26.0     | Mencetak hasil ke layar