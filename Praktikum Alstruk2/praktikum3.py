
nilai = 82
kehadiran = 90

print("--- Hasil Data Awal (Nilai=82, Kehadiran=90) ---")
print("Syarat Nilai (>= 75)     :", nilai >= 75)
print("Syarat Kehadiran (>= 80) :", kehadiran >= 80)
print("Status Kelulusan (AND)   :", nilai >= 75 and kehadiran >= 80)

nilai = 70

print("\n--- Hasil Setelah Nilai Diubah menjadi 70 ---")
print("Syarat Nilai (>= 75)     :", nilai >= 75)
print("Syarat Kehadiran (>= 80) :", kehadiran >= 80)
print("Status Kelulusan (AND)   :", nilai >= 75 and kehadiran >= 80)
print("Status Kelulusan (OR)    :", nilai >= 75 or kehadiran >= 80)
