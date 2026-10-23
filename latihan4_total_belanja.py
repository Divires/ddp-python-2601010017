# latihan4_total_belanja.py

nama_barang = input("Masukkan nama barang: ")
harga_satuan = float(input("Masukkan harga satuan: "))
jumlah_barang = int(input("Masukkan jumlah barang: "))

subtotal = harga_satuan * jumlah_barang
ppn = 0.11 * subtotal
total_bayar = subtotal + ppn

print(f"Subtotal {subtotal}, PPN {ppn}, Total {total_bayar}")