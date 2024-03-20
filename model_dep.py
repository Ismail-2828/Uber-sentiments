import pickle
from flask import Flask, jsonify, request

# Load the saved model
with open(r'UBER MODEL.pkl', 'rb') as file:
    model = pickle.load(file)

# Create a Flask app
app = Flask(__name__)

# Define a route to accept and respond to requests
@app.route('/predict', methods=['POST'])
def predict():
    # Extract the data from the request
    data = request.get_json()

    # Use the loaded model to make predictions
    predictions = model.predict(data['input'])

    # Convert the predictions to a JSON object and return it
    return jsonify({'output': predictions.tolist()})

if __name__ == '__main__':
    # Start the Flask app
    app.run()