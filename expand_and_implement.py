import csv
from joblib import dump, load
from sklearn.linear_model import LogisticRegression

inputs = []
labels = []

with open("tvt.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        predictor_marines = int(row[0])
        enemy_marines = int(row[1])
        score = int(row[2])

        inputs.append((predictor_marines, enemy_marines))
        labels.append(1 if score > 0 else 0)

logreg = LogisticRegression()
logreg.fit(inputs, labels)
dump(logreg, "tvt.joblib")
logreg = load("tvt.joblib")

print(logreg.predict([(3, 6)]))
