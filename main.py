from flask import Flask, request, jsonify
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import pandas as pd


app = Flask(__name__)
data = None
model = None

#uploading data
@app.route('/upload', methods=['POST'])
def upload_data():
    global data
    file = request.files.get('file')
    if not file:
        return jsonify({"error": "No file uploaded"}), 400

    data = pd.read_csv(file)
    return jsonify({"message": "Data uploaded successfully", "columns": list(data.columns)})

#Training endpoint
@app.route('/train', methods=['POST'])
def train_model():
    global data, model
    if data is None:
        return jsonify({"error": "No data uploaded"}), 400

    X = data[['Temperature', 'Run_Time']] #dependent variables
    y = data['Downtime_Flag'] #target variable
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = DecisionTreeClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    clf_report = classification_report(y_test, y_pred, output_dict=True)
    conf_matrix = confusion_matrix(y_test, y_pred).tolist()

    return jsonify({
        "message": "Model trained successfully",
        "accuracy": accuracy,
        "classification_report": clf_report,
        "confusion_matrix": conf_matrix
    })

#Predict endpoint
@app.route('/predict', methods=['POST'])
def predict():
    global model
    if model is None:
        return jsonify({"error": "Model not trained"}), 400

    input_data = request.get_json()
    if not input_data or not all(k in input_data for k in ['Temperature', 'Run_Time']):
        return jsonify({"error": "Invalid input format"}), 400 #input values

    features = [[input_data['Temperature'], input_data['Run_Time']]]
    prediction = model.predict(features)[0]
    confidence = max(model.predict_proba(features)[0])

    return jsonify({"Downtime": "Yes" if prediction == 1 else "No", "Confidence": round(confidence, 2)})


#To run the app locally
if __name__ == '__main__':
    app.run(debug=True, port=5007)
