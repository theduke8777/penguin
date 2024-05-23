import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
 
penguin_df = pd.read_csv('penguins.csv')
penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']]
features = pd.get_dummies(features)

#convert into numercail Adeli is 0, Gentoo is 1 and so on
output, unique = pd.factorize(output)

x_train, x_test, y_train, y_test = train_test_split(features, output, test_size=.8)
# Train the model
rfc = RandomForestClassifier(random_state=15)
rfc.fit(x_train.values, y_train)

y_pred = rfc.predict(x_test)
score = accuracy_score(y_pred, y_test)
print(f'Our accuracy : {score}')


# When creating a picker files: 1. Model and the 2. output
# Generate pickle files for model(rfc) and  output which is unique(from pd.factorize)
rf_pickle = open('random_forget_penguin.pickle', 'wb')
pickle.dump(rfc, rf_pickle)
rf_pickle.close()

output_pickle = open('output_penguin.pickle', 'wb')
pickle.dump(unique, output_pickle)
output_pickle.close()

