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

        <b-modal id="new-user" centered title="New User" @hidden="resetUserForm"
                 @ok.prevent="submitCreate">
            <form ref="newUserForm">
                <b-form-group label="Login" label-for="login-input" invalid-feedback="Login is required">
                    <b-form-input id="login-input" v-model="user.login" required type="text" name="login"
                                  :state="validateUserState('login')" />
                </b-form-group>

                <b-form-group label="First name" label-for="first-name-input"
                              invalid-feedback="First name is required">
                    <b-form-input id="first-name-input" v-model="user.first_name" required type="text"
                                  name="first_name" :state="validateUserState('first_name')" />
                </b-form-group>

                <b-form-group label="Last name" label-for="last-name-input" invalid-feedback="Last name is required">
                    <b-form-input id="last-name-input" v-model="user.last_name" required type="text" name="last_name"
                                  :state="validateUserState('last_name')" />
                </b-form-group>

                <b-form-group label="Birthday" label-for="birthday-input" invalid-feedback="Birthday is required">
                    <b-form-input id="birthday-input" v-model="user.birthday" required type="date" name="birthday"
                                  :state="validateUserState('birthday')"/>
                </b-form-group>

                <b-form-group label="E-mail" label-for="email-input">
                    <b-form-input id="email-input" v-model="user.email" type="email" name="email"
                                  :state="validateUserState('email')" />
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    import {userValidationMixin} from "../mixins/user-validation";

    export default {
        name: "UsersNavbar",
        mixins: [userValidationMixin],
        data() {
            return {
                user: {
                    login: null,
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