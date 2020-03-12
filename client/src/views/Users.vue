<template>
    <div>
        <UsersNavbar @submit-create="submitCreate"/>
        <UsersTable v-bind:users="users" @delete-user="submitDelete" @edit-user="editUser" @manage-user="manageUser"
                    ref="usersTable"/>

        <b-modal id="edit-user" centered title="Edit User" @ok.prevent="submitEdit()" @hidden="resetUserForm">
            <form ref="editUserForm">
                <b-form-group label="Login" label-for="login-input"
                              invalid-feedback="Login is required">
                    <b-form-input id="login-input" v-model="user.login" :state="validateUserState('login')"
                                  required type="text" name="login"/>
                </b-form-group>

                <b-form-group label="First name" label-for="first-name-input"
                              invalid-feedback="First name is required">
                    <b-form-input id="first-name-input" v-model="user.first_name"
                                  :state="validateUserState('first_name')" required type="text" name="first_name"/>
                </b-form-group>

                <b-form-group label="Last name" label-for="last-name-input"
                              invalid-feedback="Last name is required">
                    <b-form-input id="last-name-input" v-model="user.last_name"
                                  :state="validateUserState('last_name')" required type="text" name="last_name"/>
                </b-form-group>

                <b-form-group label="Birthday" label-for="birthday-input"
                              invalid-feedback="Birthday is required">
                    <b-form-input id="birthday-input" v-model="user.birthday"
                                  :state="validateUserState('birthday')" required type="date" name="birthday"/>
                </b-form-group>

                <b-form-group label="E-mail" label-for="email-input">
                    <b-form-input id="email-input" v-model="user.email" type="email" name="email"
                                  :state="validateUserState('email')" />
                </b-form-group>
            </form>
        </b-modal>

        <b-modal id="manage-user" centered title="Manage User" @ok.prevent="submitManage()" @hidden="resetManageForm">
            <form ref="manageUserForm">
                <b-form-group label="Role" label-for="role-input">
                    <multiselect id="role-input" v-model="selectedRole" track-by="name" label="name"
                                 placeholder="Manage Role" :options="roles" />
                </b-form-group>
                <b-form-group label="Groups" label-for="groups-input">
                    <multiselect id="groups-input" v-model="selectedGroups" :options="groups" :multiple="true"
                                 :close-on-select="false" :clear-on-select="false" :preserve-search="true"
                                 placeholder="Manage Groups" label="name" track-by="name" :preselect-first="true"/>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    import UsersNavbar from "../components/UsersNavbar";
    import UsersTable from "../components/UsersTable";
    import {userApiMixin} from "../mixins/user-api";
    import {groupApiMixin} from "../mixins/group-api";
    import {roleApiMixin} from "../mixins/role-api";
    import {userValidationMixin} from "../mixins/user-validation";

    export default {
        name: "Users",
        mixins: [userApiMixin, groupApiMixin, roleApiMixin, userValidationMixin],
        data() {
            return {
                user: {},
                selectedGroups: [],
                selectedRole: null,
            }
        },
        components: {
            UsersNavbar, UsersTable
        },
        created() {
            document.title = "User Manager - Users";
            this.getUsers().then(response => {
                this.users = response.data;
            });
        },
        methods: {
            resetManageForm() {
                this.user = {}
            },
            editUser(user) {
                this.user = {...user};
                this.user.birthday = new Date(this.user.birthday).toISOString().slice(0, 10);
                this.user.created_at = new Date(this.user.created_at).toISOString().slice(0, 19);
                this.$bvModal.show("edit-user")
            },
            manageUser(user) {
                this.user = user;
                this.getUserMetadata(user.id).then(response => {
                    this.selectedGroups = response.data.groups;
                    this.selectedRole = response.data.role
                });
                this.getGroups().then(response => {
                    this.groups = response.data
                });
                this.getRoles().then(response => {
                    this.roles = response.data
                });
                this.$bvModal.show("manage-user")
            },
            submitDelete(user) {
                if (!confirm("Are you sure?"))
                    return;
                this.deleteUser(user.id).then(response => {
                    // Delete from table if success
                    if (response.status === 200) {
                        this.users = this.users.filter(_user => _user.id !== user.id);
                        // Show notification
                        this.$bvToast.toast(`User ${user.login} deleted`, {
                            title: 'User deleted',
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
            submitEdit() {
                this.$v.user.$touch();
                if (this.$v.user.$anyError) {
                    return;
                }
                this.updateUser(this.user).then(response => {
                    if (response.status === 200) {
                        this.user = {};
                        let userIndex = this.users.findIndex(user => user.id === response.data.id);
                        this.users[userIndex] = response.data;
                        this.$refs.usersTable.refreshTable();
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
            submitManage() {
                let groups = this.selectedGroups.map(group => group.id);
                let role = ((this.selectedRole instanceof Object) ? this.selectedRole.id : null);
                console.log(groups);
                console.log(role);
                this.updateUserMetadata(this.user.id, {"role": role, "groups": groups}).then(response => {
                    if (response.status === 200) {
                        this.$nextTick(() => {
                            this.$bvModal.hide('manage-user')
                        });
                        this.$bvToast.toast(`User ${this.user.login} updated`, {
                            title: 'User updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        });
                        this.user = {};
                    } else {
                        this.$bvToast.toast(`Something went wrong. Error code: ${response.status}`, {
                            title: 'Error',
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                })
            },
            submitCreate(user) {
                this.createUser(user).then(response => {
                    this.users.push(response.data);
                    // Show notification
                    this.$bvToast.toast(`User ${response.data.login} added`, {
                        title: 'User added',
                        autoHideDelay: 5000,
                        variant: "dark"
                    })
                });
            }
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"/>

<style scoped>
</style>