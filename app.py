from flask import Flask, render_template, request
import joblib
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords


app = Flask(
  __name__,
  template_folder="frontend/templates",
  static_folder="frontend/static",
)


model = joblib.load('./models/spam_classifier.pkl')
vectorizer = joblib.load('./models/vectorizer.pkl')


lemmatizer = WordNetLemmatizer()
stop_words = set(stopwords.words('english'))

def preprocess_text(text):
  text = re.sub('[^a-zA-Z]', ' ', text)
  text = text.lower()
  text = ' '.join([lemmatizer.lemmatize(word) for word in text.split() if word not in stop_words])
  return text


@app.route('/', methods=['GET', 'POST'])
def index():
  if request.method == 'POST':
    input = request.form['message']
    
    input_processed = preprocess_text(input)
    input_vectorized = vectorizer.transform([input_processed]) 
  
    prediction = model.predict(input_vectorized)
    result = 'Spam' if prediction[0] == 1 else 'Ham'
  
    return render_template('index.html', result=result, input=input)
  
  else:
    return render_template('index.html', result=None)


if __name__ == '__main__':
  app.run(debug=True)