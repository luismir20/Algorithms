import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

data = pd.DataFrame({
    'Age': [22, 25, 30, 35, 40, 45, 50, 55],
    'Income': [25000, 35000, 40000, 50000, 60000, 70000, 80000, 90000],
    'Credit Score': [600, 650, 700, 750, 800, 850, 900, 950],
    'Bought a Car': ['No', 'Yes', 'Yes', 'Yes', 'Yes', 'No', 'No', 'No']
})

# Spliting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    data[['Age', 'Income', 'Credit Score']],
    data['Bought a Car'],
    test_size=0.2,
    random_state=0
)

print("Instances in the testing set:")
print(X_test)

clf = DecisionTreeClassifier()

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print("Predictions:", y_pred)

accuracy = clf.score(X_test, y_test)
print('Accuracy:', accuracy)
