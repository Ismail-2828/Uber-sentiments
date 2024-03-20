from flask import Flask, request, jsonify
import joblib

app = Flask(__name__)

# Load the pre-trained model (ensure you've saved it using joblib)
model = joblib.load('Sentiment_model.pkl')
vectorizer = joblib.load('Sentiment_vectorizer.pkl')

def text_preprocess(doc):
    doc = doc.lower()
    doc = doc.replace('.',". ")
    doc = doc.replace(',',", ")
    doc = doc.replace('!',"! ")
    doc = re.sub(r"[^a-z\s]","",doc)
    doc = [d for d in doc.split() if d not in stopwords]
    doc = " ".join(doc)
    return doc 

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    review = data['review']
    
    # Preprocess and vectorize the review
    preprocessed_review = text_preprocess(review)
    vectorized_review = vectorizer.transform([preprocessed_review])

    # Predict sentiment
    prediction = model.predict(vectorized_review)[0]
    
    return jsonify({'prediction': int(prediction)})

if __name__ == '__main__':
    app.run(debug=False)