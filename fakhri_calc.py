import streamlit as st

# Fungsi untuk menghitung hasil kalkulasi
def calculate_result(expression):
    try:
        return eval(expression)
    except:
        return "Error"

# Desain dan header aplikasi
st.set_page_config(page_title="Kalkulator Sederhana", page_icon="💻", layout="wide")
st.title("Kalkulator Sederhana")
st.subheader("Kalkulator interaktif dengan tampilan yang menarik!")

# Tampilan kalkulator interaktif
st.markdown(
    """
    <style>
    .calc-button {
        background-color: #4CAF50;
        border: none;
        color: white;
        padding: 20px;
        font-size: 18px;
        cursor: pointer;
        width: 60px;
        height: 60px;
        border-radius: 10px;
    }
    .calc-button:hover {
        background-color: #45a049;
    }
    .calc-display {
        font-size: 30px;
        background-color: #f4f4f4;
        border: none;
        padding: 10px;
        width: 100%;
        text-align: right;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True
)

# Variabel untuk menyimpan ekspresi kalkulator
if 'expression' not in st.session_state:
    st.session_state.expression = ""

# Input tampilan kalkulasi
input_display = st.text_input("Tampilan Kalkulasi", value=st.session_state.expression, disabled=True, key="display", label_visibility="collapsed")

# Fungsi untuk memperbarui ekspresi kalkulasi
def update_expression(value):
    st.session_state.expression += value

# Fungsi untuk menghapus ekspresi kalkulasi
def clear_expression():
    st.session_state.expression = ""

# Fungsi untuk menghitung hasil kalkulasi
def get_result():
    result = calculate_result(st.session_state.expression)
    return result

# Menambahkan tombol kalkulator
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("7", key="7"):
        update_expression("7")
with col2:
    if st.button("8", key="8"):
        update_expression("8")
with col3:
    if st.button("9", key="9"):
        update_expression("9")
        
with col1:
    if st.button("4", key="4"):
        update_expression("4")
with col2:
    if st.button("5", key="5"):
        update_expression("5")
with col3:
    if st.button("6", key="6"):
        update_expression("6")
        
with col1:
    if st.button("1", key="1"):
        update_expression("1")
with col2:
    if st.button("2", key="2"):
        update_expression("2")
with col3:
    if st.button("3", key="3"):
        update_expression("3")
        
with col1:
    if st.button("0", key="0"):
        update_expression("0")
with col2:
    if st.button("+", key="+"):
        update_expression("+")
with col3:
    if st.button("-", key="-"):
        update_expression("-")
        
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("*", key="*"):
        update_expression("*")
with col2:
    if st.button("/", key="/"):
        update_expression("/")
with col3:
    if st.button("C", key="clear"):
        clear_expression()

col1, col2, col3 = st.columns(3)

with col1:
    if st.button("(", key="("):
        update_expression("(")
with col2:
    if st.button(")", key=")"):
        update_expression(")")
with col3:
    if st.button("=", key="equal"):
        result = get_result()
        st.text(f"Hasil: {result}")

# Tampilan hasil kalkulasi
st.write(f"**Hasil: {get_result()}**")


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








