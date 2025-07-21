from flask import Flask, render_template, request
import joblib
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk


def download_nltk_resources():
  try:
    nltk.data.find('corpora/stopwords')
  except LookupError:
    nltk.download('stopwords')

download_nltk_resources()


app = Flask(
  __name__,
  template_folder="frontend/templates",
  static_folder="frontend/static",
)


model = joblib.load('./models/spamClassifier.pkl')
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
    result=""
    
    if not input:
      return render_template('index.html', result="Please enter a message to classify.", input="")
          
    input_processed = preprocess_text(input)
    input_vectorized = vectorizer.transform([input_processed]) 
  
    prediction = model.predict(input_vectorized)
    result = 'Spam' if prediction[0] == 1 else 'Ham'
    message = str(input)
    
    return render_template('index.html', result=result, input="", message=message)
  
  else:
    return render_template('index.html', result=None, input="")


if __name__ == '__main__':
  app.run(debug=True)