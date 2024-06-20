import joblib
import pandas as pd
from sklearn.impute import SimpleImputer
import numpy as np
# preprocessing
def normalisasi(x):
    # import data test
    cols = ['BMI','Perokok Aktif','Peminum Alkohol','Kesehatan Fisik','Kesehatan Mental','DiffWalking','Penderita Diabetes','Aktivitas Fisik']
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('model/data_test_norm.csv')
    # data_test = data_test.drop(data_test.columns[0],axis=1)
    
    # memasukkan data kedalam data test
    data_test = data_test.append(other=df,ignore_index=True)
    # print(data_test)
    # return data_test yang sudah dinormalisasi
    return joblib.load('model/norm1.sav').fit_transform(data_test)

# normals
def normal(x):
    cols = ['BMI','Perokok Aktif','Peminum Alkohol','Kesehatan Fisik','Kesehatan Mental','DiffWalking','Penderita Diabetes','Aktivitas Fisik']
    df = pd.DataFrame([x],columns=cols)
    data_test = pd.read_csv('model/data_test_norm.csv')
    # data_test = data_test.drop(data_test.columns[0],axis=1)
    # memasukkan data kedalam data test
    data_test = data_test.append(other=df,ignore_index=True)
    # return data_test yang sudah dinormalisasi
    return (data_test)

# metode with normalization
def knn(x):
    return joblib.load('model/best_knn_model.pkl').predict(x)
    # print(x)
   
