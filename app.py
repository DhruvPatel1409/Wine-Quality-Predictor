import numpy as np
import pickle
import streamlit as st
import pandas as pd

loaded_model = pickle.load(open('C:/Users/ADMIN/Desktop/python jupyter/wine quality prediction/wine_model.sav','rb'))

nav = st.sidebar.radio("Navigation",["About","Predict"])
df = pd.read_csv('winequality-red.csv')

if nav=="About":
    st.title("Wine Quality Prediction App")
    st.text("")
    st.text("")
    st.image('wb.jpg',width=600)

if nav=="Predict":
    def wine_prediction(input_data):

        data_numeric = np.array(input_data).astype(float)
        input_data_as_numpy_array = np.asarray(input_data)
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
        prediction = loaded_model.predict(input_data_reshaped)
        print(prediction)

        if(prediction[0] == 0):
            return "BAD QUALITY WINE"
        else:
            return "GOOD QUALITY WINE"

    def main():

        st.title('Wine Quality Prediction App')

        fixed_acidity = st.number_input('Level of fixed acidity : ')
        volatile_acidity = st.number_input('Level of volatile acidity : ')
        citric_acid = st.number_input('Level of citric acid : ')
        residual_sugar = st.number_input('Level of residual sugar : ')
        chlorides = st.number_input('Level of chlorides : ')
        free_sulfur_dioxide	 = st.number_input('Level of free sulfur dioxide : ')
        total_sulfur_dioxide = st.number_input('Level of total sulfur dioxide : ')
        density = st.number_input('Level of density : ')
        pH = st.number_input('Level of pH : ')
        sulphates = st.number_input('Level of sulphates : ')
        alcohol = st.number_input('Level of alcohol : ')

    # code for prediction

        quality = ' '

        if st.button('PREDICT'):
            quality = wine_prediction([fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol])
    
        st.success(quality)

    if __name__ == '__main__':
        main()
    