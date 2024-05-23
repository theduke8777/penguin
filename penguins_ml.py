import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

penguin_df = pd.read_csv('penguins.csv')
penguin_df.dropna(inplace=True)
output = penguin_df['species']
features = penguin_df[['island', 'bill_length_mm', 'bill_depth_mm','flipper_length_mm', 'body_mass_g', 'sex']]
# Find the columns that will coverted to false or true. island has tree: for example: Torgerson will be island_Torgenson(true or false)
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