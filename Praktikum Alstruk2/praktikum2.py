
print("====================================")
print("          TOKO ALFAMART")
print("====================================")

harga = 12500
jumlah = 4

total = harga * jumlah
sisa = total % 2000
diskon = 5000
harga_diskon = total - diskon

print(f"Harga per buku      : Rp {harga:,}")
print(f"Jumlah buku dibeli  : {jumlah} buah")
print("------------------------------------")
print(f"Total Harga         : Rp {total:,}")
print(f"Sisa Pembagian % 2000: Rp {sisa:,}")
print(f"Harga Setelah Diskon: Rp {harga_diskon:,}")
print("====================================")
