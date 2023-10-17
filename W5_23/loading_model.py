import pickle

model_file = 'model1.bin'
vectorizer_file = 'dv.bin'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(vectorizer_file, 'rb') as vect:
    vectorizer = pickle.load(vect)

client = {"job": "retired", "duration": 445, "poutcome": "success"}

X = vectorizer.transform([client])
y_pred = model.predict_proba(X)[0, 1]

print('input', client)
print('prediction of getting credit', y_pred)