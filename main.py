# import libary 
import streamlit as st
import metode
import time
import pandas as pd

# pige title
st.set_page_config(
    page_title="Prediksi Penyakit Jantung",
    page_icon="https://e7.pngegg.com/pngimages/594/747/png-clipart-heart-heart-cartoon-heart.png",
)

# hide menu
hide_streamlit_style = """



<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
</style>

"""
# insialisasi web
st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)
kolom = st.columns((2.2, 0.48, 2.7))
home = kolom[1].button('🏠')
about = kolom[2].button('About')

# home page
if home==False and about==False or home==True and about==False:
    st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
    # setting kolom
    # with st.expander("Setting"):

    preprosesing = st.radio('Preprocessing Data', options=['Normalization (Min-Max)', 'Normal'], index=0, horizontal=True)
    col1, col2 = st.columns(2)
    with col1:
        nama = st.text_input("Masukkan Nama",placeholder='Nama')
    with col2:
        umur = st.number_input("Masukkan Umur",max_value=100)
    jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
    col3,col4 = st.columns(2)
    with col3:
        bmi = st.number_input("BMI",min_value=0,max_value=10000)
    with col4:
        pa = st.selectbox("Perokok Aktif",('Iya','Tidak'))
    col5,col6 = st.columns(2)
    with col5:
        peAlk = st.selectbox("Peminum Alkohol",('Iya','Tidak'))
    with col6:
        kesfis = st.number_input("Kesehatan Fisik",min_value=0,max_value=1000)
    col7,col8 = st.columns(2)
    with col7:
        kesMen = st.number_input("Kesehatan Mental",min_value=0,max_value=1000)
    with col8:
        diffw = st.selectbox("Diffwalking",('Iya','Tidak'))
    col9,col10 = st.columns(2)
    with col9:
        diabet = st.selectbox("Penderita diabetes",('Iya','Tidak'))
    with col10:
        AktF = st.selectbox("Aktivitas fisik",('Iya','Tidak'))

    
    
    
    #    Centering Butoon 
    columns = st.columns((2, 0.6, 2))
    submit = columns[1].button("Submit")
    # if sumbit == True:

    if submit and nama != '' and diffw !='' and diabet !='' and AktF !=''  and jk != '' and pa !='' and peAlk!='' and kesfis !=0 and kesMen !=0 and umur !=0  and bmi !=0 :
            if preprosesing == 'Normalization (Min-Max)':
                if pa == 'Iya' and peAlk == 'Iya' and diffw == 'Iya' and diabet == 'Iya' and AktF == 'Iya':
                    pa, peAlk, diffw, diabet, AktF= 0, 0, 0, 0, 0
                else:
                    pa, peAlk, diffw, diabet, AktF = 1, 1, 1, 1, 1
                    # normalisasi data
                
                datanorm = metode.normalisasi([bmi, pa, peAlk, kesfis, kesMen, diffw, diabet, AktF])
                    # prediksi data
                # print([bmi])
               
                prediksi = metode.knn(datanorm)
                # print(prediksi)       
                 # cek prediksi
                with st.spinner("Tunggu Sebentar Masih Proses..."):
                    string_temp = (f'{nama} age is {umur} and jenis kelamin {jk}')
                    if prediksi[-1] == 0:
                        time.sleep(1)
                        
                        st.success(string_temp+" tidak ada penyakit jantung")
                    else:
                        time.sleep(1)
                        st.warning(string_temp+" Ada Penyakit Jantung")    
            else:
                if pa == 'Iya' and peAlk == 'Iya' and diffw == 'Iya' and diabet == 'Iya' and AktF == 'Iya':
                    pa, peAlk, diffw, diabet, AktF = 0, 0, 0, 0, 0
                else:
                    pa, peAlk, diffw, diabet, AktF = 1, 1, 1, 1, 1
                    # normalisasi data
                data = metode.normal([bmi, pa, peAlk, kesfis, kesMen, diffw, diabet, AktF])
                    # prediksi data
                # print([bmi])
                # print(pd.DataFrame(data))
                prediksi = metode.knn(data)
                        # cek prediksi
                with st.spinner("Tunggu Sebentar Masih Proses..."):
                    string_temp = (f'{nama} age is {umur} and jenis kelamin {jk}')
                    if prediksi[-1] == 0:
                        time.sleep(1)
                        st.success(string_temp+" Tidak Ada Penyakit Jantung")
                    else:
                        time.sleep(1)
                        st.warning(string_temp+" Ada Penyakit Jantung")    
    else:
        st.error("Harap Diisi Semua Kolom")

# about page
if about==True and home==False:
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem Prediksi Penyakit Jantung adalah sebuah sistem yang bertujuan untuk memprediksi penyakit jantung dini. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Dataset</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Dataset yang digunakan pada sistem ini memiliki <b>9 fitur</b> termasuk kelas, Dataset yang digunakan dalam sistem ini menggunakan data real yang didapatkan disalah satu puskesmas di kecamatan arosbaya kota bangakalan . Dataset yang berjudul <i>Heart Disease</i>, dataset untuk mendeteksi apakah seseorang mengidap Penyakit Jantung atau tidak berdasarkan berbagai faktor seperti <i>BMI</i>,<i>Perokok Aktif</i>,<i>Peminum Alkohol</i>,<i>Kesehatan Fisik</i>,<i>Kesehatan Mental</i>,<i>DiffWalking</i>,<i>Penderita Diabetes</i>,<i>Aktivitas Fisik</i>,class (0/1), fitur yang disebutkan rata-rata string yang sudah diubah mencajadi kategorikal.</p>", unsafe_allow_html=True)
    st.write('Untuk Fitur kolestrol bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter. Untuk fitur blood pressure bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tahap preprosessing</h4>", unsafe_allow_html=True)
    st.write('Sistem ini menggunakan preprosessing data yaitu dengan normalisasi data. Metode normalisasi yang digunakan adalah MinMaxScaler.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Metode yang digunakan</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 11</b> dengan akurasi 75% jika sebelumnya data dinormalisasi terlebih dahulu, namun jika tanpa normalisasi akurasi yang didapat sebesar 70% .</p>", unsafe_allow_html=True) 
