<template>
    <div id="navbar-wrapper">
        <b-navbar id="navbar" type="white" variant="white">
            <b-nav-form>
                <b-button pill v-b-modal.new-user variant="success">
                    <font-awesome-icon icon="plus"/>
                    New User
                </b-button>
            </b-nav-form>
        </b-navbar>

        <b-modal id="new-user" centered title="New User" @show="resetUserForm"
                 @ok.prevent="submitCreate">
            <form ref="newUserForm">
                <b-form-group :state="loginState" label="Login" label-for="login-input"
                              invalid-feedback="Login is required">
                    <b-form-input id="login-input" v-model="user.login" :state="loginState"
                                  required type="text" name="login"/>
                </b-form-group>

                <b-form-group :state="firstNameState" label="First name" label-for="first-name-input"
                              invalid-feedback="First name is required">
                    <b-form-input id="first-name-input" v-model="user.first_name"
                                  :state="firstNameState" required type="text" name="first_name"/>
                </b-form-group>

                <b-form-group :state="lastNameState" label="Last name" label-for="last-name-input"
                              invalid-feedback="Last name is required">
                    <b-form-input id="last-name-input" v-model="user.last_name"
                                  :state="lastNameState" required type="text" name="last_name"/>
                </b-form-group>

                <b-form-group :state="birthdayState" label="Birthday" label-for="birthday-input"
                              invalid-feedback="Birthday is required">
                    <b-form-input id="birthday-input" v-model="user.birthday"
                                  :state="birthdayState" required type="date" name="birthday"/>
                </b-form-group>

                <b-form-group label="E-mail" label-for="email-input">
                    <b-form-input id="email-input" v-model="user.email" type="email" name="email"/>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: "UsersNavbar",
        data() {
            return {
                user: {
                    login: "",
                    first_name: "",
                    last_name: "",
                    birthday: "",
                    email: ""
                },
                loginState: null,
                firstNameState: null,
                lastNameState: null,
                birthdayState: null
            }
        },
        methods: {
            checkFormValidity() {
                const valid = this.$refs.newUserForm.checkValidity();
                this.loginState = valid;
                this.firstNameState = valid;
                this.lastNameState = valid;
                this.birthdayState = valid;
                return valid
            },
            resetUserForm() {
                this.user.login = "";
                this.user.first_name = "";
                this.user.last_name = "";
                this.user.birthday = "";
                this.user.email = "";
                this.loginState = null;
                this.firstNameState = null;
                this.lastNameState = null;
                this.birthdayState = null
            },
            submitCreate() {
                if (!this.checkFormValidity())
                    return;
                this.$emit("submit-create", this.user);
                this.$nextTick(() => {
                    this.$bvModal.hide('new-user')
                });
            }
        }
    }
</script>

<style scoped>
    #navbar-wrapper {
        height: 6vh;
    }

    #navbar {
        height: 100%;
    }
</style>