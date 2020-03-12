<template>
    <div>
        <UsersNavbar/>
        <UsersTable v-bind:users="users" @delete-user="submitDelete" @edit-user="editUser" @manage-user="manageUser"
                    ref="usersTable"/>

        <NewUserModal @add-user-to-table="addUserToTable" ref="newUserModal"/>
        <EditUserModal @update-user-in-table="updateUserInTable" ref="editUserModal"/>
        <ManageUserModal ref="manageUserModal"/>

    </div>
</template>

<script>
    import UsersNavbar from "../components/navbars/UsersNavbar";
    import UsersTable from "../components/tables/UsersTable";
    import {userApiMixin} from "../mixins/api/user-api";
    import NewUserModal from "../components/modals/NewUserModal";
    import EditUserModal from "../components/modals/EditUserModal";
    import ManageUserModal from "../components/modals/ManageUserModal";

    export default {
        name: "Users",
        mixins: [userApiMixin],
        components: {
            UsersNavbar, UsersTable, NewUserModal, EditUserModal, ManageUserModal
        },
        created() {
            document.title = "User Manager - Users";
            this.getUsers().then(response => {
                this.users = response.data;
            });
        },
        methods: {
            editUser(user) {
                this.$refs.editUserModal.editUser(user)
            },
            manageUser(user) {
                this.$refs.manageUserModal.manageUser(user)
            },
            submitDelete(user) {
                if (!confirm("Are you sure?"))
                    return;
                this.deleteUser(user.id).then(response => {
                    if (response.status === 200) {
                        this.users = this.users.filter(_user => _user.id !== user.id);
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
            addUserToTable(user) {
                this.users.push(user)
            },
            updateUserInTable(user) {
                let userIndex = this.users.findIndex(_user => _user.id === user.id);
                this.users[userIndex] = user;
                this.$refs.usersTable.refreshTable();
            }
        }
    }
</script>

<style src="vue-multiselect/dist/vue-multiselect.min.css"/>

<style scoped>
</style>