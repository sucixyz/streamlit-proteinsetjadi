import streamlit as st
def hitung_kebutuhan_protein(umur, tinggi_cm, berat_kg, jenis_kelamin):
    """
    Menghitung kebutuhan protein harian (gram per hari) berdasarkan:
    - Umur (tahun)
    - Tinggi (cm)
    - Berat badan (kg)
    - Jenis kelamin ("L" atau "P")

    Rumus umum (perkiraan berdasarkan berat badan dan jenis kelamin):
    - Laki-laki: 0.9 gram protein per kg berat badan
    - Perempuan: 0.8 gram protein per kg berat badan
    - Anak-anak: > 1 gram/kg tergantung usia

    Return: kebutuhan protein per hari dalam gram
    """

    if umur <= 3:
        kebutuhan_protein = berat_kg * 1.05
    elif umur <= 8:
        kebutuhan_protein = berat_kg * 0.95
    elif umur <= 18:
        kebutuhan_protein = berat_kg * 0.85
    else:
        if jenis_kelamin.upper() == "L":
            kebutuhan_protein = berat_kg * 0.9
        elif jenis_kelamin.upper() == "P":
            kebutuhan_protein = berat_kg * 0.8
        else:
            return "Jenis kelamin tidak valid. Gunakan 'L' atau 'P'."

    return round(kebutuhan_protein, 2)


# Contoh penggunaan program
umur = int(input("Masukkan umur (tahun): "))
tinggi = float(input("Masukkan tinggi badan (cm): "))
berat = float(input("Masukkan berat badan (kg): "))
jenis_kelamin = input("Masukkan jenis kelamin (L/P): ")

hasil = hitung_kebutuhan_protein(umur, tinggi, berat, jenis_kelamin)

print(f"Kebutuhan protein harian Anda diperkirakan: {hasil} gram")