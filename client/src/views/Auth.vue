<template>
    <b-container class="mt-5 p-5 w-25 text-center border border-dark rounded-bottom rounded-lg">
        <h1>
            <font-awesome-icon icon="user" size="5x"/>
        </h1>
        <h3>Sign In</h3>
        <b-form @submit.prevent="onSubmit" novalidate>
            <b-form-group class="text-left" invalid-feedback="Login is required" label="Login" label-for="login-input">
                <b-form-input :state="validateAuthState('login')" id="name-input" required type="text"
                              v-model="credentials.login"/>
            </b-form-group>
            <b-form-group class="text-left" invalid-feedback="Password is required" label="Password"
                          label-for="login-input">
                <b-form-input :state="validateAuthState('password')" id="name-input" required type="password"
                              v-model="credentials.password"/>
            </b-form-group>
            <b-button type="submit" variant="primary">Submit</b-button>
        </b-form>
    </b-container>
</template>

<script>
    import {authApiMixin} from "../mixins/api/auth-api";
    import {authValidationMixin} from "../mixins/validation/login-validation";

    export default {
        name: "Auth",
        mixins: [authApiMixin, authValidationMixin],
        data() {
            return {
                credentials: {
                    login: "admin",
                    password: "admin"
                }
            }
        },
        methods: {
            onSubmit() {
                this.$v.credentials.$touch();
                if (this.$v.credentials.$anyError) {
                    return;
                }
                this.login(this.credentials).then(response => {
                        localStorage.setItem('user', JSON.stringify(response.data.user));
                        localStorage.setItem('jwt', response.data.token);
                        if (localStorage.getItem('jwt') != null) {
                            if (this.$route.params.nextUrl != null) {
                                this.$router.push(this.$route.params.nextUrl)
                            } else {
                                this.$router.push('users')
                            }
                            location.reload();
                        }
                    }
                )
            }
        }
    }
</script>

<style scoped>

</style>