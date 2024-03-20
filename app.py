from flask import Flask, render_template, request
import re 
import joblib
import nltk
app = Flask(__name__)

# Load the pre-trained model and vectorizer
model = joblib.load('Sentiment_model.pkl')
vectorizer = joblib.load('Sentiment_vectorizer.pkl')
stopwords = nltk.corpus.stopwords.words("English")

def text_preprocess(doc):
    doc = doc.lower()
    doc = doc.replace('.',". ")
    doc = doc.replace(',',", ")
    doc = doc.replace('!',"! ")
    doc = re.sub(r"[^a-z\s]","",doc)
    doc = [d for d in doc.split() if d not in stopwords]
    doc = " ".join(doc)
    return doc 

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    prediction = ""  # Default value for prediction
    review = ""
    if request.method == 'POST':
        review = request.form['review']
        
        # Preprocess and vectorize the review
        preprocessed_review = text_preprocess(review)
        vectorized_review = vectorizer.transform([preprocessed_review])

        # Get prediction
        pred_value = model.predict(vectorized_review)[0]
        prediction = "Positive" if pred_value == 1 else "Negative"
    
    # Render the template with the prediction value
    return render_template("index.html", prediction=prediction,review_text=review)

if __name__ == '__main__':
    app.run(debug=True)
