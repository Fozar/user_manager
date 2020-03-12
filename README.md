<h1>Welcome to User Manager Prototype</h1>
<p>
    Designed by Alexandr Timoshenko specifically for Digital Ecosystems as a test task for employment.
</p>
<h3>Frontend Technologies Stack</h3>
<ul>
    <li>JavaScript</li>
    <li>Vue.js</li>
    <li>Vue Router</li>
    <li>Bootstrap Vue</li>
    <li>FortAwesome/vue-fontawesome</li>
    <li>Vue-multiselect</li>
    <li>Vuelidate</li>
    <li>Axios</li>
</ul>
<h3>Backend Technologies Stack</h3>
<ul>
    <li>Python 3</li>
    <li>Postgresql 10</li>
    <li>virtualenv</li>
    <li>SQLAlchemy</li>
    <li>WTForms</li>
    <li>WTForms-Alchemy</li>
    <li>Flask</li>
    <li>Flask-CORS</li>
    <li>Flask-RESTful</li>
    <li>Flask-SQLAlchemy</li>
    <li>Flask-WTF</li>
    <li>Flask-Bcrypt</li>
</ul>

# client
```
cd client
```
## Project setup
```
npm install
```

### Compiles and hot-reloads for development
```
npm run serve
```

### Compiles and minifies for production
```
npm run build
```

### Lints and fixes files
```
npm run lint
```

### Customize configuration
See [Configuration Reference](https://cli.vuejs.org/config/).

# server
```
cd server
```

### Create venv
##### Windows:
```
python -m venv venv
cd venv/Scripts
activate.bat
cd ../../
```
##### Linux:
```
python3 -m venv venv
source venv/bin/activate
```

### Install requirements
##### Windows:
```
pip install -r requirements.txt
```
##### Linux:
```
pip3 install -r requirements.txt
```

### Customize configuration in config.py!

### Run server
##### Windows:
```
python app.py
```
##### Linux:
```
python3 app.py
```