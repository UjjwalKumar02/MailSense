# MailSense

MailSense is a web application that classifies user-provided mail messages as **spam** or **ham** using a Machine learning model.

---

## Technologies Used

- Python
- Flask
- Natural Language Processing (NLP)
- scikit-learn
- Tailwind CSS

---

## Features

- Simple and Clean UI
- Real-time email classification
- Pre-trained ML model for spam detection

---

## Installation


  
Install the dependencies:

```
pip install -r requirements.txt
```

Configure Tailwind  
```
npm install -D tailwindcss@3 postcss autoprefixer  
npx tailwindcss init -p
```  

Update the tailwind.config.js  
```
module.exports = {
  content: ["./templates/**/*.html"],
  theme: {
    extend: {},
  },
  plugins: [],
}
```
Run the command in separate terminal
```
cd frontend
npx tailwindcss -i ./tailwind/input.css -o ./static/css/styles.css --watch
```  

Run the app in other terminal
```
python app.py
```
<!-- ---
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
``` -->
