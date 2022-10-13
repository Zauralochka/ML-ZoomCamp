import pickle

model_file = 'model1.bin'
vectorizer_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(vectorizer_file, 'rb') as vect:
    vectorizer = pickle.load(vect)

client = {"reports": 0, "share": 0.001694, "expenditure": 0.12, "owner": "yes"}

X = vectorizer.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print('input', client)
print('prediction of getting credit card', y_pred)