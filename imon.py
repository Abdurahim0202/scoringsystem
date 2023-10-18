import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st

from PIL import Image

# Основная функция
def main():
    
    age = st.number_input("Ваш возраст:", min_value=18, max_value=100)
    number = st.number_input("Sum:", min_value=0, max_value=100000000)
    Period = st.number_input("Period of the longest debt:", min_value=0, max_value=100000000)
    time = st.number_input("Time:", min_value=0, max_value=100000000)
    gender = st.selectbox("Ваш пол:", ["Мужской", "Женский"])
    customer = st.selectbox("Type of client:", ["New customer", "Old customer"])
    education = st.selectbox("Education level:", ["Среднее образование", "Высшее образование", "Сред.спец.образ-ние", "Непол Сред.образ", "Начал образование", "Аспирантура"])
    tp_bus = st.selectbox("Type of business:", ["Карзи истеъмоли/Потребительский кредит", "Хизматрасони/Услуги", "Савдо / Торговля", "Истехсолот/Производство", "Хочагии кишлок / Сельское хозяйство"])
    family = st.selectbox("Your family situation:", ["Married", "Single", 'Divorced' , 'Widow'])
    gen_code = 0 
    if(gender == "Мужской"):
        gen_code = 1 
    else:
        gen_code = 0
    
    cus_code = 0 
    if(customer == "New customer"):
        cus_code = 2 
    else:
        cus_code = 1
        
    fam_code = 0 
    if(family == "Married"):
        fam_code = 1 
    elif(family == 'Single'):
        fam_code = 2
    elif(family == 'Divorced'):
        fam_code = 3
    else:
        fam_code = 4
    
    bus_code = 0 
    if(tp_bus == "Карзи истеъмоли/Потребительский кредит"):
        bus_code = 1 
    elif(tp_bus == 'Хизматрасони/Услуги'):
        bus_code = 2
    elif(tp_bus == 'Савдо / Торговля'):
        bus_code = 3
    elif(tp_bus == 'Истехсолот/Производство'):
        bus_code = 4
    else:
        bus_code = 5
  
    
    edu_code = 0 
    if(education == "Среднее образование"):
        edu_code = 1 
    elif(education == 'Высшее образование'):
        edu_code = 2
    elif(education == 'Сред.спец.образ-ние'):
        edu_code = 3
    elif(education == 'Непол Сред.образ'):
        edu_code = 4
    elif(education == 'Начал образование'):
        edu_code = 5
    else:
        edu_code = 6
        
    # Выводим данные на экран
    st.write("Your age :", age)
    st.write("Your gender:", gen_code)
    st.write("Your family situation:", fam_code)
    st.write("Your type of business:", bus_code)
    st.write("Your education:", edu_code)
    st.write("Which type of client are you :", cus_code)
    st.write("Sum of debt:", number)
    
    pickle_in = open("Logreg_Imon.pkl","rb")
    classifier=pickle.load(pickle_in)
    prediction=classifier.predict([[number, time, age, gen_code, edu_code, fam_code, cus_code, bus_code]])
    
    print(prediction)
    return prediction

    result=""
    if st.button("Predict"):
        result=int(predict_note_authentication(number, time, age, gen_code, edu_code, fam_code, cus_code, bus_code))


    #st.success('The output is {}'.format(result))
    st.success('Predicted cost of the house is {}'.format(result)+" TJS")
    if st.button("About"):
        st.text("Lets LEarn")
        st.text("Built with Streamlit")
# Запускаем приложение

if __name__ == "__main__":
    main()