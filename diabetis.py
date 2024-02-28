import numpy as np
import pickle
import sklearn
import streamlit as st
#
# # LOADING THE SAVED MODEL
loaded_model = pickle.load(open('C:/Users\ANKUSH\Desktop/AI ML/ML/Feature Engineering/train_model.sav','rb'))
#
#
# input = (0,108,68,20,0,27.3,1.171133,-0.236812)
# #input_data to numpy array
# input_data_as_numpy_array = np.array(input)
#
# input_data_reshape = input_data_as_numpy_array.reshape(1,-1)
#
# prediction = loaded_model.predict(input_data_reshape)
# print(prediction)
#
# if (prediction[0] == 1):
#     print('Person is diabetic')
# else:
#     print('person is not diabetic')


#creating function for prediction
def diabetis_pred(input):
    input = (0,108,68,20,0,27.3,1.171133,-0.236812)
     #input_data to numpy array
    input_data_as_numpy_array = np.array(input)

    input_data_reshape = input_data_as_numpy_array.reshape(1,-1)

    prediction = loaded_model.predict(input_data_reshape)
    print(prediction)

    if (prediction[0] == 1):
        return 'Person is diabetic'
    else:
        return 'person is not diabetic'

def main():

    # GIVING TITLE
    st.title('Diabetis Prediction Web App')

    # GETTING INPUT DATA
    Pregnancies = st.text_input('Number of pregnancies')
    Glucose = st.text_input('Glucose level')
    BloodPressure = st.text_input('Blood Pressure Value')
    SkinThickness = st.text_input('Skin Thickness values')
    Insulin = st.text_input('Insulin value')
    BMI = st.text_input('BMI')
    Age_boxcox = st.text_input('Age')
    dpf_boxcox = st.text_input('dpf')

    #CODE FOR PREDICTION
    diagnosis = ''

    # CREATING A BUTTON FOR PREDICTION
    if st.button('Diabetes Test Result'):
        diagnosis = diabetis_pred([Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,Age_boxcox,dpf_boxcox])

    st.success(diagnosis)

if __name__ == '__main__':
    main()

















