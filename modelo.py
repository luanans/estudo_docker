from sklearn import datasets
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from pymongo import MongoClient
import json

iris = datasets.load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.3, random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train, y_train)

predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)

client = MongoClient('mongodb://luana:luana@mongodb:27017/')
db = client['iris_dataset']
collection = db['model_accuracy']

result = {
    'accuracy': accuracy,
    'model': 'Logistic Regression'
}
collection.insert_one(result)

print("Resultados salvos no MongoDB.")