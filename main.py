# import libary 
import streamlit as st
import time
import metode
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

tab1, tab2, tab3, tab4, tab5, tab6, tab7 = st.tabs(["Dataset", "Normalisasi", "Prepocesing", "model", "Accuracy", "About", "Prediksi"])
with tab1:
    st.write('Dataset')
    datas = pd.read_csv("heart_deases.csv")
    df = pd.DataFrame(datas)
    df
with tab2:
    class1 = '''
    st.write('Normalisasi')
    df = df.head(5000)
    df
    '''
    st.code(class1)
    st.write('Normalisasi')
    df = df.head(5000)
    df
    class2 = '''
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report, accuracy_score
    from sklearn.model_selection import GridSearchCV
    from sklearn.feature_selection import SelectKBest, chi2
    from imblearn.over_sampling import SMOTE
    from imblearn.under_sampling import RandomUnderSampler
    from imblearn.pipeline import Pipeline
    
    X = df.drop('Penyakit Jantung', axis=1)
    y = df['Penyakit Jantung']
    '''
    st.code(class2)
    import pandas as pd
    from sklearn.model_selection import train_test_split
    from sklearn.preprocessing import MinMaxScaler
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.metrics import classification_report, accuracy_score
    from sklearn.model_selection import GridSearchCV
    from sklearn.feature_selection import SelectKBest, chi2
    from imblearn.over_sampling import SMOTE
    from imblearn.under_sampling import RandomUnderSampler
    from imblearn.pipeline import Pipeline
    
    X = df.drop('Penyakit Jantung', axis=1)
    y = df['Penyakit Jantung']
    class3 ='''
    undersampler = RandomUnderSampler(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = undersampler.fit_resample(X, y)
    '''
    st.code(class3)
    undersampler = RandomUnderSampler(sampling_strategy='auto', random_state=42)
    X_resampled, y_resampled = undersampler.fit_resample(X, y)
    
    class4 = '''
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_resampled)
    nama_fitur = X.columns.copy()
    scaled_fitur = pd.DataFrame(X_scaled,columns=nama_fitur)
    scaled_fitur
    '''
    st.code(class4)
    scaler = MinMaxScaler()
    X_scaled = scaler.fit_transform(X_resampled)
    nama_fitur = X.columns.copy()
    scaled_fitur = pd.DataFrame(X_scaled,columns=nama_fitur)
    scaled_fitur

    
with tab3:
    st.write('Prepocesing')
    class5 = '''
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_resampled, test_size=0.2, random_state=1)
    X_train
    '''
    st.code(class5)
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y_resampled, test_size=0.2, random_state=1)
    X_train
    
with tab4:
    st.write('Model')
    class6 = '''
    from sklearn.model_selection import GridSearchCV
    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1, 31))}
    
    # Lakukan grid search dengan 5-fold cross-validation
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    
    # Fit model dengan data
    grid_search.fit(X_train, y_train)
    '''
    st.code(class6)
    from sklearn.model_selection import GridSearchCV
    knn = KNeighborsClassifier()
    param_grid = {'n_neighbors': list(range(1, 31))}
    
    # Lakukan grid search dengan 5-fold cross-validation
    grid_search = GridSearchCV(knn, param_grid, cv=5, scoring='accuracy')
    
    # Fit model dengan data
    grid_search.fit(X_train, y_train)
    "Best parameter (k):", grid_search.best_params_
    "Best cross-validation score:", grid_search.best_score_
with tab5:
    st.write('Accuracy')
    class7 ='''
    knn = KNeighborsClassifier(n_neighbors=21)
    knn.fit(X_train, y_train)
    '''
    st.code(class7)
    knn = KNeighborsClassifier(n_neighbors=21)
    knn.fit(X_train, y_train)
    
    class8 ='''
     y_pred = knn.predict(X_test)
    '''
    st.code(class8)
    y_pred = knn.predict(X_test)

    class9 ='''
    from sklearn.metrics import classification_report, confusion_matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    print("Confusion Matrix:\n", conf_matrix)
    '''
    st.code(class9)
    from sklearn.metrics import classification_report, confusion_matrix
    conf_matrix = confusion_matrix(y_test, y_pred)
    st.write("Confusion Matrix:")
    conf_matrix

    class10 ='''
    print("Accuracy:", accuracy_score(y_test, y_pred))
    print("Classification Report:\n", classification_report(y_test, y_pred))
    '''
    st.code(class10)
    st.write("Accuracy:") 
    acc = accuracy_score(y_test, y_pred)
    acc
    target_name = ["class 0", "class 1"]
    st.dataframe(
        pd.DataFrame(
            classification_report(y_test, y_pred, target_names=target_name, output_dict=True)
        ).transpose()
    )
    # "Classification Report:\n", classification_report(y_test, y_pred)
with tab6:
    st.write('About')
    st.markdown("<h2 style='text-align: center; color: white; margin:0 ; padding:0;'>Tentang Sistem ini</h2>", unsafe_allow_html=True)
    st.write('Sistem Prediksi Penyakit Jantung adalah sebuah sistem yang bertujuan untuk memprediksi penyakit jantung dini. Sistem ini dibuat menggunakan bahasa pemrograman python dan library streamlit.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Dataset</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Dataset yang digunakan pada sistem ini memiliki <b>9 fitur</b> termasuk kelas, Dataset yang digunakan dalam sistem ini menggunakan data real yang didapatkan disalah satu puskesmas di kecamatan arosbaya kota bangakalan . Dataset yang berjudul <i>Heart Disease</i>, dataset untuk mendeteksi apakah seseorang mengidap Penyakit Jantung atau tidak berdasarkan berbagai faktor seperti <i>BMI</i>,<i>Perokok Aktif</i>,<i>Peminum Alkohol</i>,<i>Kesehatan Fisik</i>,<i>Kesehatan Mental</i>,<i>DiffWalking</i>,<i>Penderita Diabetes</i>,<i>Aktivitas Fisik</i>,class (0/1), fitur yang disebutkan rata-rata string yang sudah diubah mencajadi kategorikal.</p>", unsafe_allow_html=True)
    st.write('Untuk Fitur kolestrol bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter. Untuk fitur blood pressure bisa didapatkan dengan cara mengecek ke dokter atau dengan cara mengukur sendiri dengan menggunakan alat yang disediakan oleh dokter.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Tahap preprosessing</h4>", unsafe_allow_html=True)
    st.write('Sistem ini menggunakan preprosessing data yaitu dengan normalisasi data. Metode normalisasi yang digunakan adalah MinMaxScaler.')
    st.markdown("<h4 style='text-align: center; color: white; margin:0 ; padding:0;'>Metode yang digunakan</h4>", unsafe_allow_html=True)
    st.markdown("<p  color: white;'>Pada sistem ini menggunakan model KNN ( <i>K-nearest neighbors algorithm</i> ) dengan parameter <b>K = 11</b> dengan akurasi 75% jika sebelumnya data dinormalisasi terlebih dahulu, namun jika tanpa normalisasi akurasi yang didapat sebesar 70% .</p>", unsafe_allow_html=True) 

with tab7:
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
                pa, peAlk, diffw, diabet, AktF = (0 if val == 'Iya' else 1 for val in [pa, peAlk, diffw, diabet, AktF])
                    # normalisasi data
                
                data = metode.normalisasi([bmi, pa, peAlk, kesfis, kesMen, diffw, diabet, AktF])
                    # prediksi data
                # print([bmi])
               
                prediksi = metode.knn(data)
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
                pa, peAlk, diffw, diabet, AktF = (0 if val == 'Iya' else 1 for val in [pa, peAlk, diffw, diabet, AktF])
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

# insialisasi web
# st.markdown("<p style='text-align: center; color: white; margin:0 ; padding:0;'>MENU</p>", unsafe_allow_html=True)
# kolom = st.columns((2, 2, 8, 8, 7, 8, 7, 8))
# home = kolom[1].button('Dataset')
# normalisasi = kolom[2].button('normalisasi')
# prepocesing = kolom[3].button('prepocesing')
# model = kolom[4].button('model')
# accuracy = kolom[5].button('a`ccuracy')
# about = kolom[6].button('About')
# prediksi = kolom[7].button('prediksi')

# home page
# if prediksi==False and about==False and home==True or prediksi==False and about==False and home==False :
#     st.write('Dataset')
#     datas = pd.read_csv("data_fix1.csv", sep=";")
#     df = pd.DataFrame(datas)
#     df
    
# if prediksi==False and about==False and home==False or prediksi==True and about==False and home==False :
#     st.markdown("<h1 style='text-align: center; color: white; margin:0 ; padding:0;'>Prediksi Penyakit Jantung</h1>", unsafe_allow_html=True)
#     # setting kolom
#     # with st.expander("Setting"):

#     preprosesing = st.radio('Preprocessing Data', options=['Normalization (Min-Max)', 'Normal'], index=0, horizontal=True)
#     col1, col2 = st.columns(2)
#     with col1:
#         nama = st.text_input("Masukkan Nama",placeholder='Nama')
#     with col2:
#         umur = st.number_input("Masukkan Umur",max_value=100)
#     jk = st.selectbox("Jenis Kelamin",('Laki-laki','Perempuan'))
#     col3,col4 = st.columns(2)
#     with col3:
#         bmi = st.number_input("BMI",min_value=0,max_value=10000)
#     with col4:
#         pa = st.selectbox("Perokok Aktif",('Iya','Tidak'))
#     col5,col6 = st.columns(2)
#     with col5:
#         peAlk = st.selectbox("Peminum Alkohol",('Iya','Tidak'))
#     with col6:
#         kesfis = st.number_input("Kesehatan Fisik",min_value=0,max_value=1000)
#     col7,col8 = st.columns(2)
#     with col7:
#         kesMen = st.number_input("Kesehatan Mental",min_value=0,max_value=1000)
#     with col8:
#         diffw = st.selectbox("Diffwalking",('Iya','Tidak'))
#     col9,col10 = st.columns(2)
#     with col9:
#         diabet = st.selectbox("Penderita diabetes",('Iya','Tidak'))
#     with col10:
#         AktF = st.selectbox("Aktivitas fisik",('Iya','Tidak'))
    
#     #    Centering Butoon 
#     columns = st.columns((2, 0.6, 2))
#     submit = columns[1].button("Submit")
#     # if sumbit == True:

#     if submit and nama != '' and diffw !='' and diabet !='' and AktF !=''  and jk != '' and pa !='' and peAlk!='' and kesfis !=0 and kesMen !=0 and umur !=0  and bmi !=0 :
#             if preprosesing == 'Normalization (Min-Max)':
#                 pa, peAlk, diffw, diabet, AktF = (0 if val == 'Iya' else 1 for val in [pa, peAlk, diffw, diabet, AktF])
#                     # normalisasi data
                
#                 data = metode.normalisasi([bmi, pa, peAlk, kesfis, kesMen, diffw, diabet, AktF])
#                     # prediksi data
#                 # print([bmi])
               
#                 prediksi = metode.knn(data)
#                 # print(prediksi)       
#                  # cek prediksi
#                 with st.spinner("Tunggu Sebentar Masih Proses..."):
#                     string_temp = (f'{nama} age is {umur} and jenis kelamin {jk}')
#                     if prediksi[-1] == 0:
#                         time.sleep(1)
                        
#                         st.success(string_temp+" tidak ada penyakit jantung")
#                     else:
#                         time.sleep(1)
#                         st.warning(string_temp+" Ada Penyakit Jantung")    
#             else:
#                 pa, peAlk, diffw, diabet, AktF = (0 if val == 'Iya' else 1 for val in [pa, peAlk, diffw, diabet, AktF])
#                     # normalisasi data
#                 data = metode.normal([bmi, pa, peAlk, kesfis, kesMen, diffw, diabet, AktF])
#                     # prediksi data
#                 # print([bmi])
#                 # print(pd.DataFrame(data))
#                 prediksi = metode.knn(data)
#                         # cek prediksi
#                 with st.spinner("Tunggu Sebentar Masih Proses..."):
#                     string_temp = (f'{nama} age is {umur} and jenis kelamin {jk}')
#                     if prediksi[-1] == 0:
#                         time.sleep(1)
#                         st.success(string_temp+" Tidak Ada Penyakit Jantung")
#                     else:
#                         time.sleep(1)
#                         st.warning(string_temp+" Ada Penyakit Jantung")    
#     else:
#         st.error("Harap Diisi Semua Kolom")

# about page
# if about==True and home==False and prediksi==False:
    
