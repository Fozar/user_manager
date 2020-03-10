<template>
    <div>
        <RolesNavbar @submit-create="submitCreate"/>
        <RolesTable v-bind:roles="roles" @delete-role="submitDelete" @edit-role="editRole"
                    @manage-role="manageRole" ref="rolesTable"/>

        <b-modal id="edit-role" centered title="Edit Role" @ok.prevent="submitEdit()" @show="resetRoleForm">
            <form ref="editRoleForm">
                <b-form-group :state="nameState" label="Name" label-for="name-input"
                              invalid-feedback="Name is required">
                    <b-form-input id="name-input" v-model="roleToEdit.name" :state="nameState"
                                  required type="text" name="name"/>
                </b-form-group>
            </form>
        </b-modal>

        <b-modal id="manage-role" centered title="Manage Role" @ok.prevent="submitManage()" @hidden="resetManageForm">
            <form ref="manageRoleForm">
                <b-form-group label="Groups" label-for="groups-input">
                    <multiselect id="groups-input" v-model="selectedGroups" :options="groups" :multiple="true"
                                 :close-on-select="false" :clear-on-select="false" :preserve-search="true"
                                 placeholder="Manage Groups" label="name" track-by="name" :preselect-first="true">
                        <template slot="selection" slot-scope="{ values, search, isOpen }">
                            <span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">
                                {{ values.length }} groups selected
                            </span>
                        </template>
                    </multiselect>
                </b-form-group>
                <b-form-group label="Users" label-for="users-input">
                    <multiselect id="users-input" v-model="selectedUsers" :options="users" :multiple="true"
                                 :close-on-select="false" :clear-on-select="false" :preserve-search="true"
                                 placeholder="Manage Users" label="login" track-by="login" :preselect-first="true">
                        <template slot="selection" slot-scope="{ values, search, isOpen }">
                            <span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">
                                {{ values.length }} users selected
                            </span>
                        </template>
                    </multiselect>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    import {roleApiMixin} from "../mixins/role-api";
    import RolesNavbar from "../components/RolesNavbar";
    import RolesTable from "../components/RolesTable";
    import {groupApiMixin} from "../mixins/group-api";
    import {userApiMixin} from "../mixins/user-api";

    export default {
        name: "Roles",
        mixins: [roleApiMixin, groupApiMixin, userApiMixin],
        data() {
            return {
                roleToEdit: {},
                selectedGroups: [],
                selectedUsers: [],
                nameState: null,
            }
        },
        components: {
            RolesNavbar, RolesTable
        },
        created() {
            document.title = "User Manager - Roles";
            this.getRoles().then(response => {
                this.roles = response.data
            });
        },
        methods: {
            checkFormValidity() {
                const valid = this.$refs.editRoleForm.checkValidity();
                this.nameState = valid;
                return valid
            },
            resetRoleForm() {
                this.nameState = null;
            },
            resetManageForm() {
                this.roleToEdit = {}
            },
            editRole(role) {
                this.roleToEdit = {...role};
                this.$bvModal.show("edit-role")
            },
            manageRole(role) {
                this.roleToEdit = role;
                this.getRoleMetadata(role.id).then(response => {
                    this.selectedUsers = response.data.users;
                    this.selectedGroups = response.data.groups
                });
                this.getUsers().then(response => {
                    this.users = response.data
                });
                this.getGroups().then(response => {
                    this.groups = response.data
                });
                this.$bvModal.show("manage-role")
            },
            submitDelete(role) {
                if (!confirm("Are you sure?"))
                    return;
                this.deleteRole(role.id).then(response => {
                    // Delete from table if success
                    if (response.status === 200) {
                        this.roles = this.roles.filter(_role => _role.id !== role.id);
                        // Show notification
                        this.$bvToast.toast(`Role ${role.name} deleted`, {
                            title: 'Role deleted',
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
                if (!this.checkFormValidity())
                    return;
                this.updateRole(this.roleToEdit).then(response => {
                    if (response.status === 200) {
                        this.roleToEdit = {};
                        let roleIndex = this.roles.findIndex(role => role.id === response.data.id);
                        this.roles[roleIndex] = response.data;
                        this.$refs.rolesTable.refreshTable();
                        this.$nextTick(() => {
                            this.$bvModal.hide('edit-role')
                        });
                        this.$bvToast.toast(`Role ${response.data.name} updated`, {
                            title: 'Role updated',
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
                let users = this.selectedUsers.map(user => user.id);
                let groups = this.selectedGroups.map(group => group.id);
                this.updateRoleMetadata(this.roleToEdit.id, {"groups": groups, "users": users}).then(response => {
                    if (response.status === 200) {
                        this.$nextTick(() => {
                            this.$bvModal.hide('manage-role')
                        });
                        this.$bvToast.toast(`Role ${this.roleToEdit.name} updated`, {
                            title: 'Role updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        });
                        this.roleToEdit = {};
                    } else {
                        this.$bvToast.toast(`Something went wrong. Error code: ${response.status}`, {
                            title: 'Error',
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                })
            },
            submitCreate(role) {
                this.createRole(role).then(response => {
                    // Push to roles array
                    this.roles.push(response.data);
                    // Show notification
                    this.$bvToast.toast(`Role ${response.data.name} added`, {
                        title: 'Role added',
                        autoHideDelay: 5000,
                        variant: "dark"
                    })
                });
            }
        }
    }
</script>

<style scoped>
</style>