import streamlit as st
import pandas as pd
import joblib

# Modeli yükle
model = joblib.load('model.pkl')

st.title("🎓 EdTech: Öğrenci Başarı Tahminleyici")

# Veri seti sütunlarını oku (Modelin beklediği yapı için)
df = pd.read_csv('student_data.csv')
X = df.drop('G3', axis=1)

# Kullanıcıya bir form sun (Daha kolay yönetmek için)
with st.form("ogrenci_formu"):
    # Örnek olarak birkaç kritik sütunu alalım
    age = st.number_input("Yaş", 15, 22, 17)
    studytime = st.slider("Haftalık Çalışma Süresi", 1, 4, 2)
    absences = st.number_input("Devamsızlık", 0, 90, 5)
    g1 = st.number_input("1. Dönem Notu", 0, 20, 10)
    g2 = st.number_input("2. Dönem Notu", 0, 20, 10)
    
    submit = st.form_submit_button("Tahmin Et")

if submit:
    # Modelin beklediği tüm sütunları oluşturuyoruz (Sadece senin girdiklerini güncelle, gerisi 0 kalsın)
    # Bu, tüm verileri tek bir satırda gönderir
    data = pd.DataFrame(columns=X.columns) # X, yukarıda df.drop('G3') ile tanımladığın değişken
    data.loc[0] = 0 # Her şeyi sıfırla
    
    # Kendi girdiklerini yerleştir
    data['age'] = age
    data['studytime'] = studytime
    data['absences'] = absences
    data['G1'] = g1
    data['G2'] = g2
    
    # Şimdi tahmin et
    tahmin = model.predict(data)
    st.success(f"Tahmini Final Notu: {tahmin[0]:.2f}")
