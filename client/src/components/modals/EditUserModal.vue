<template>
    <b-modal @hidden="resetUserForm" @ok.prevent="submitEdit()" centered id="edit-user" title="Edit User">
        <form>
            <b-form-group invalid-feedback="Login is required" label="Login"
                          label-for="login-input">
                <b-form-input :state="validateUserState('login')" id="login-input" name="login"
                              required type="text" v-model="user.login"/>
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
                <b-form-input :state="validateUserState('first_name')" id="first-name-input"
                              name="first_name" required type="text" v-model="user.first_name"/>
            </b-form-group>

            <b-form-group invalid-feedback="Last name is required" label="Last name"
                          label-for="last-name-input">
                <b-form-input :state="validateUserState('last_name')" id="last-name-input"
                              name="last_name" required type="text" v-model="user.last_name"/>
            </b-form-group>

            <b-form-group invalid-feedback="Birthday is required" label="Birthday"
                          label-for="birthday-input">
                <b-form-input :state="validateUserState('birthday')" id="birthday-input"
                              name="birthday" required type="date" v-model="user.birthday"/>
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
        name: "EditUserModal",
        mixins: [userValidationMixin, userApiMixin],
        data() {
            return {
                user: {}
            }
        },
        methods: {
            editUser(user) {
                this.user = {...user};
                this.user.birthday = new Date(this.user.birthday).toISOString().slice(0, 10);
                this.user.created_at = new Date(this.user.created_at).toISOString().slice(0, 19);
                this.$bvModal.show("edit-user")
            },
            submitEdit() {
                this.$v.user.$touch();
                if (this.$v.user.$anyError) {
                    return;
                }
                this.updateUser(this.user).then(response => {
                    if (response.status === 200) {
                        this.$emit('update-user-in-table', response.data);
                        this.$nextTick(() => {
                            this.$bvModal.hide('edit-user')
                        });
                        this.$bvToast.toast(`User ${response.data.login} updated`, {
                            title: 'User updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        })
                    } else {
                        this.$bvToast.toast(`Something went wrong. Error code: ${response.status}`, {
                            title: 'Error',
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>