<template>
    <div>
        <h1>
            <font-awesome-icon size="5x" icon="user"/>
            <br>Welcome to User Manager Prototype
        </h1>
        <p>
            Designed by Alexandr Timoshenko specifically for Digital Ecosystems as a test task for employment.
        </p>
        <p><strong>WARNING:<br>Don't forget to change the axios.defaults.baseURL in main.js to API url!</strong></p>
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
            <li>Flask-JWT-Extended</li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: 'HelloWorld',
    }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
    h3 {
        margin: 50px 0 0;
    }

    ul {
        list-style-type: none;
        padding: 0;
    }

    li {
        display: inline-block;
        margin: 0 10px;
    }

    a {
        color: #42b983;
    }
</style>
