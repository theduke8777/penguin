import streamlit as st 
import pickle
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split


st.title('Penguin Classifier')
st.write('This app uses 6 inputs to predict the species of penguin using a model built on the Palmer Penguins dataset. Use the form below')



rf_pickle = open('./random_forget_penguin.pickle', 'rb')
map_pickle = open('./output_penguin.pickle', 'rb')
rfc = pickle.load(rf_pickle)
unique_penguin_mapping = pickle.load(map_pickle)
rf_pickle.close()
map_pickle.close()


island = st.selectbox('Penguinn Island', options=['Biscoe', 'Dream', 'Torgeson'])
sex = st.selectbox('Sex', options=['Female', 'Male'])
bill_length = st.number_input('Bill Length (mm)', min_value=0)
bill_depth = st.number_input('Bill Depth (mm)', min_value=0)
flipper_length = st.number_input('Flipper Length (mm)', min_value=0)
body_mass =st.number_input('Body Mass (g)', min_value=0)

island_biscoe, island_dream, island_torgenson = 0,0,0
if island == 'Biscoe':
    island_biscoe = 1
elif island == 'Dream':
    island_dream = 1
elif island == 'Torgenson':
    island_torgenson = 1

sex_female, sex_male = 0, 0
if sex == 'Female':
    sex_female = 1
elif sex == 'Male':
    sex_male = 1

x = [[bill_length, bill_depth, flipper_length, body_mass, island_biscoe, island_dream, island_torgenson, sex_female, sex_male]]
new_prediction = rfc.predict(x)
prediction_species = unique_penguin_mapping[new_prediction][0]
st.write(f'We predict your penguin is of the {prediction_species} species')    
