import streamlit as st
import numpy as np
from scipy.stats import linregress

# Fungsi untuk menghitung % inhibisi
def calculate_inhibition(abs_sample, abs_blank):
    return ((abs_blank - abs_sample) / abs_blank) * 100

# Fungsi untuk menghitung IC50
def calculate_ic50(concentrations, inhibitions):
    slope, intercept, _, _, _ = linregress(concentrations, inhibitions)
    ic50 = -intercept / slope
    return slope, intercept, ic50

# Header aplikasi
st.title("DPPH Bioassay untuk Aktivitas Antioksidan")
st.write("Aplikasi ini membantu menghitung aktivitas antioksidan berdasarkan data absorbansi dan menghitung IC50.")

# Input data sampel
st.header("Input Data Sampel")
num_samples = st.number_input("Masukkan jumlah sampel yang diuji:", min_value=1, step=1)

# Nama ekstrak
extract_names = []
for i in range(num_samples):
    name = st.text_input(f"Masukkan nama ekstrak untuk sampel {i+1}:", key=f"name_{i}")
    extract_names.append(name)

# Data absorbansi blanko
abs_blank = st.number_input("Masukkan absorbansi blanko:", min_value=0.0, format="%.4f")

# Input data konsentrasi dan absorbansi
st.header("Data Konsentrasi dan Absorbansi")
concentration_inputs = {}
absorbance_inputs = {}

for name in extract_names:
    st.subheader(f"Sampel: {name}")
    num_points = st.number_input(
        f"Jumlah titik data untuk sampel {name}:", min_value=1, step=1, key=f"points_{name}"
    )
    concentrations = []
    absorbances = []
    for i in range(num_points):
        conc = st.number_input(
            f"Konsentrasi (ppm) titik {i+1} untuk {name}:", min_value=0.0, format="%.4f", key=f"conc_{name}_{i}"
        )
        abs_val = st.number_input(
            f"Absorbansi titik {i+1} untuk {name}:", min_value=0.0, format="%.4f", key=f"abs_{name}_{i}"
        )
        concentrations.append(conc)
        absorbances.append(abs_val)
    concentration_inputs[name] = concentrations
    absorbance_inputs[name] = absorbances

# Hitung dan tampilkan hasil
if st.button("Hitung Aktivitas Antioksidan"):
    for name in extract_names:
        concentrations = np.array(concentration_inputs[name])
        absorbances = np.array(absorbance_inputs[name])

        # Hitung % inhibisi
        inhibitions = calculate_inhibition(absorbances, abs_blank)

        # Hitung regresi dan IC50
        slope, intercept, ic50 = calculate_ic50(concentrations, inhibitions)

        # Tampilkan hasil
        st.subheader(f"Hasil untuk {name}")
        st.write(f"Persamaan regresi: y = {slope:.4f}x + {intercept:.4f}")
        st.write(f"IC50: {ic50:.4f} ppm")


# import streamlit as st
# import math

# def calculate_ph(mass=None, molarity=None, volume=None, dilution=None, substance_type="acid"):
#     """
#     Fungsi untuk menghitung pH larutan berdasarkan parameter yang diberikan.
#     - mass: massa zat (gram)
#     - molarity: molaritas larutan (M)
#     - volume: volume awal (liter)
#     - dilution: volume setelah pengenceran (liter)
#     - substance_type: jenis zat ("acid" atau "base")
#     """
#     # Konstanta molar massa HCl dan NaOH untuk contoh (ubah sesuai zat yang digunakan)
#     molar_mass = 36.46 if substance_type == "acid" else 40.00
    
#     # Hitung molaritas awal jika massa dan volume diketahui
#     if mass and volume:
#         molarity = mass / (molar_mass * volume)
    
#     # Hitung molaritas setelah pengenceran
#     if molarity and dilution:
#         molarity /= dilution
    
#     # Hitung pH atau pOH
#     if molarity:
#         if substance_type == "acid":
#             ph = -math.log10(molarity)
#         else:  # Untuk basa, hitung pOH dan konversi ke pH
#             poh = -math.log10(molarity)
#             ph = 14 - poh
#         return round(ph, 2)
#     return None

# # Streamlit app
# st.title("pH Meter WebApp")

# st.sidebar.header("Input Parameters")
# substance_type = st.sidebar.radio("Select Substance Type", ["acid", "base"])

# mass = st.sidebar.number_input("Mass (grams)", min_value=0.0, value=0.0, step=0.1)
# volume = st.sidebar.number_input("Initial Volume (liters)", min_value=0.0, value=0.0, step=0.1)
# dilution = st.sidebar.number_input("Diluted Volume (liters)", min_value=0.0, value=0.0, step=0.1)

# if st.sidebar.button("Calculate pH"):
#     ph_result = calculate_ph(mass=mass, volume=volume, dilution=dilution, substance_type=substance_type)
#     if ph_result is not None:
#         st.success(f"The calculated pH of the solution is: {ph_result}")
#     else:
#         st.error("Unable to calculate pH. Please check your input values.")

# st.write("Enter the parameters in the sidebar to calculate the pH of a solution.")


# import streamlit as st

# def main():
#         # Menggunakan CSS untuk mengganti background dengan warna
#     st.markdown("""
#         <style>
#             body {
#                 background-color: #FFFF;
#             }
#         </style>
#     """, unsafe_allow_html=True)
#     st.title("Kalkulator Punya Fakhri Yang Sayang Sama Ara :kissing_heart:")
#     st.write("Aplikasi ini menghitung operasi dasar matematika seperti penjumlahan (+), pengurangan (-), perkalian (x), dan pembagian (/).")
    
#     # Input angka pertama
#     num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

#     # Input angka kedua
#     num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)
    
#     # Pilihan operasi
#     operation = st.selectbox(
#         "Pilih operasi matematika:",
#         ("+", "-", "x", "/")
#     )
    
#     # Tombol untuk menghitung
#     if st.button("Hitung"):
#         if operation == "+":
#             result = num1 + num2
#             st.success(f"Hasil Penjumlahan: {result}")
#         elif operation == "-":
#             result = num1 - num2
#             st.success(f"Hasil Pengurangan: {result}")
#         elif operation == "x":
#             result = num1 * num2
#             st.success(f"Hasil Perkalian: {result}")
#         elif operation == "/":
#             if num2 != 0:
#                 result = num1 / num2
#                 st.success(f"Hasil Pembagian: {result}")
#             else:
#                 st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
    
# if __name__ == "__main__":
#     main()

# st.write("IDENTITAS DEVELOPER: ")
# st.write("Nama Saya Muhammad Fakhri Al-Fathi")
# st.write("Berkuliah Politeknik AKA Bogor")
# st.write("Saya Suka Makan Mie Sarimi Isi 2 Ayam Kremes #ga10gaasik")








