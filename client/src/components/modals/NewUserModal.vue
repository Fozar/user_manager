<template>
    <b-modal @hidden="resetUserForm" @ok.prevent="submitCreate" centered id="new-user"
             title="New User">
        <form>
            <b-form-group invalid-feedback="Login is required" label="Login" label-for="login-input">
                <b-form-input :state="validateUserState('login')" id="login-input" name="login" required type="text"
                              v-model="user.login"/>
            </b-form-group>

            <b-form-group invalid-feedback="Password is required" label="Password" label-for="password-input">
                <b-form-input :state="validateUserState('password')" id="password-input" required type="password"
                              v-model="user.password"/>
            </b-form-group>

            <b-form-group invalid-feedback="Passwords must be identical" label="Repeat password"
                          label-for="repeat-password-input">
                <b-form-input :state="validateUserState('repeatPassword')" id="repeat-password-input" required
                              type="password"
                              v-model="user.repeatPassword"/>
            </b-form-group>

            <b-form-group invalid-feedback="First name is required" label="First name"
                          label-for="first-name-input">
                <b-form-input :state="validateUserState('first_name')" id="first-name-input" name="first_name" required
                              type="text" v-model="user.first_name"/>
            </b-form-group>

            <b-form-group invalid-feedback="Last name is required" label="Last name" label-for="last-name-input">
                <b-form-input :state="validateUserState('last_name')" id="last-name-input" name="last_name" required
                              type="text"
                              v-model="user.last_name"/>
            </b-form-group>

            <b-form-group invalid-feedback="Birthday is required" label="Birthday" label-for="birthday-input">
                <b-form-input :state="validateUserState('birthday')" id="birthday-input" name="birthday" required
                              type="date"
                              v-model="user.birthday"/>
            </b-form-group>

            <b-form-group label="E-mail" label-for="email-input">
                <b-form-input :state="validateUserState('email')" id="email-input" name="email" type="email"
                              v-model="user.email"/>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import {userValidationMixin} from "../../mixins/validation/user-validation";
    import {userApiMixin} from "../../mixins/api/user-api";

    export default {
        name: "NewUserModal",
        mixins: [userValidationMixin, userApiMixin],
        data() {
            return {
                user: {
                    login: null,
                    password: null,
                    repeatPassword: null,
                    first_name: null,
                    last_name: null,
                    birthday: null,
                    email: null
                },
            }
        },
        methods: {
            submitCreate() {
                this.$v.user.$touch();
                if (this.$v.user.$anyError) {
                    return;
                }
                delete this.user.repeatPassword;
                this.createUser(this.user).then(response => {
                    this.$emit('add-user-to-table', response.data);
                    // Show notification
                    this.$bvToast.toast(`User ${response.data.login} created`, {
                        title: 'User created',
                        autoHideDelay: 5000,
                        variant: "dark"
                    });
                    this.$nextTick(() => {
                        this.$bvModal.hide('new-user')
                    })
                }).catch(err => {
                    if (err.response.status === 400) {
                        let errors = "";
                        for (let [field, error] of Object.entries(err.response.data)) {
                            field = field[0].toUpperCase() + field.slice(1);
                            errors += `${field}: ${error} `
                        }
                        this.$bvToast.toast(`Something went wrong. ${errors}`, {
                            title: `Error code: ${err.response.status}`,
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                    console.log(err)
                });
            }
        }
    }
</script>

<style scoped>

</style>