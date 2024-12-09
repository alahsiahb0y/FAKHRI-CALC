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
#     st.title("=== KALKULATOR SEDEHANA ===")
#     st.write("Kemampuan kalkulator terbatas pada : penjumlahan (+), pengurangan (-), perkalian (x), dan pembagian (/).")
    
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

# st.write("created by: Muhammad Fakhri Al-Fathi")
# st.write("Kampus: Politeknik AKA Bogor")
# st.write("Notes: Saya Suka Makan Mie Sarimi Isi 2 Ayam Kremes #ga10gaasik")

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt # type: ignore
from sklearn.linear_model import LinearRegression # type: ignore
from streamlit_option_menu import option_menu # type: ignore

# Fungsi untuk menghitung % inhibisi
def calculate_inhibition(abs_blank, abs_sample):
    return ((abs_blank - abs_sample) / abs_blank) * 100

# Fungsi untuk menghitung IC50 dari regresi linier
def calculate_ic50(concentrations, inhibitions):
    # Konversi ke array numpy
    x = np.array(concentrations).reshape(-1, 1)
    y = np.array(inhibitions)
    
    # Model regresi linier
    model = LinearRegression()
    model.fit(x, y)
    
    # IC50 adalah konsentrasi saat inhibisi 50%
    ic50 = (50 - model.intercept_) / model.coef_[0]
    return ic50, model

# Tema dan desain Streamlit
st.set_page_config(page_title="DPPH Bioassay", layout="wide", page_icon="🌿")
st.markdown(
    """
    <style>
    .main {
        background-color: #f7f7f7;
    }
    .sidebar .sidebar-content {
        background-color: #e0f7fa;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Header aplikasi
st.title("🌿 **Bioassay DPPH Antioxidant Activity**")
st.markdown("Sebuah aplikasi interaktif untuk menghitung aktivitas antioksidan berdasarkan metode DPPH.")
st.markdown("---")

# Sidebar untuk input data
with st.sidebar:
    st.header("📋 Input Data")
    extract_name = st.text_input("Nama ekstrak:", placeholder="Masukkan nama ekstrak...")
    amount_extracted = st.number_input("Massa ekstrak (mg):", min_value=0.0, step=0.1)
    solvent_volume = st.number_input("Volume pelarut (mL):", min_value=0.0, step=0.1)
    num_dilutions = st.number_input("Jumlah pengenceran:", min_value=1, step=1, value=5)
    dilution_factors = st.text_area(
        "Faktor pengenceran (pisahkan dengan koma):",
        placeholder="Contoh: 1, 2, 4, 8, 16",
    )
    abs_blank = st.number_input("Absorbansi blanko (DPPH):", min_value=0.0, step=0.01)
    abs_samples = st.text_area(
        "Absorbansi sampel (pisahkan dengan koma):",
        placeholder="Contoh: 0.7, 0.5, 0.3...",
    )

# Perhitungan konsentrasi larutan induk
if solvent_volume > 0:
    stock_concentration = amount_extracted / solvent_volume  # mg/mL
    st.sidebar.write(f"📌 Konsentrasi larutan induk: **{stock_concentration:.2f} mg/mL**")

# Proses data pengenceran
if dilution_factors and abs_samples:
    dilution_factors = list(map(float, dilution_factors.split(',')))
    abs_samples = list(map(float, abs_samples.split(',')))
    concentrations = [stock_concentration / factor for factor in dilution_factors]
    inhibitions = [calculate_inhibition(abs_blank, abs_sample) for abs_sample in abs_samples]
    
    # Menampilkan data
    data = pd.DataFrame({
        "Konsentrasi (ppm)": concentrations,
        "% Inhibisi": inhibitions
    })
    st.markdown("### 📊 Data Aktivitas Antioksidan")
    st.dataframe(data, use_container_width=True)

    # Hitung IC50 dan regresi
    ic50, model = calculate_ic50(concentrations, inhibitions)
    st.success(f"**IC50: {ic50:.2f} ppm**")

    # Plot grafik interaktif
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(concentrations, inhibitions, label="Data", color="#00796b", s=100)
    x_vals = np.linspace(min(concentrations), max(concentrations), 100)
    y_vals = model.predict(x_vals.reshape(-1, 1))
    ax.plot(x_vals, y_vals, label="Regresi Linier", color="#d32f2f", linewidth=2)
    ax.set_xlabel("Konsentrasi (ppm)", fontsize=12)
    ax.set_ylabel("% Inhibisi", fontsize=12)
    ax.set_title(f"Regresi Aktivitas Antioksidan: {extract_name}", fontsize=14)
    ax.legend()
    ax.grid(alpha=0.3)
    st.pyplot(fig)

# Footer
st.markdown("---")
st.markdown("💡 **Tips**: Pastikan data pengenceran dan absorbansi diisi dengan benar untuk hasil yang akurat.")
st.markdown("🛠️ Dibuat oleh: **[Nama Anda]**")







