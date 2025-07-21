# <center>MailSense</center>

A web application that classifies user-provided emails as **spam** or **ham** using a machine learning spam classifier model built with NLP techniques.

<br/>

## 🚀 Features

- Simple and intuitive web interface
- Real-time email classification
- Pre-trained machine learning model for spam detection
- Built with Flask and Python

<br/>

## 🛠️ Technologies Used

- Python 3
- Flask
- Natural Language Processing (NLP)
- scikit-learn
- pandas

<br/>

## Tailwind Integration

Terminal  
```bash
npm install -D tailwindcss@3 postcss autoprefixer  
npx tailwindcss init -p
```  
tailwind.config.js  

```bash
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```  

Create tailwind/input.css
```bash
@tailwind base;
@tailwind components;
@tailwind utilities;
```  

Terminal  
```bash
npx tailwindcss -i ./tailwind/input.css -o ./static/css/styles.css --watch
```  

templates/index.html
```bash
<link rel="stylesheet" href="{{ url_for('static', filename='static\css\styles.css') }}">
```


<br/>

## Run in local

``` 
python app.py
```
