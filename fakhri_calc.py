import streamlit as st

def main():
    st.title("Kalkulator Punya Fakhri")
    st.write("Aplikasi ini menghitung operasi dasar matematika seperti penjumlahan (+), pengurangan (-), perkalian (x), dan pembagian (/).")
    
    # Input angka pertama
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

    # Input angka kedua
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)
    
    # Pilihan operasi
    operation = st.selectbox(
        "Pilih operasi matematika:",
        ("+", "-", "x", "/")
    )
    
    # Tombol untuk menghitung
    if st.button("Hitung"):
        if operation == "+":
            result = num1 + num2
            st.success(f"Hasil Penjumlahan: {result}")
        elif operation == "-":
            result = num1 - num2
            st.success(f"Hasil Pengurangan: {result}")
        elif operation == "x":
            result = num1 * num2
            st.success(f"Hasil Perkalian: {result}")
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Hasil Pembagian: {result}")
            else:
                st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
    
if __name__ == "__main__":
    main()

st.write("NAMA SAYA FAKHRI BERKULIAH DI AKA:sunglasses:")







