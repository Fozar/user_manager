<template>
    <div>
        <GroupsNavbar @submit-create="submitCreate"/>
        <GroupsTable v-bind:groups="groups" @delete-group="submitDelete" @edit-group="editGroup"
                     @manage-group="manageGroup" ref="groupsTable"/>

        <b-modal id="edit-group" centered title="Edit Group" @ok.prevent="submitEdit()" @hidden="resetGroupForm">
            <form ref="editGroupForm">
                <b-form-group label="Name" label-for="name-input" invalid-feedback="Name is required">
                    <b-form-input id="name-input" v-model="group.name" :state="validateGroupState('name')"
                                  required type="text" name="name"/>
                </b-form-group>
            </form>
        </b-modal>

        <b-modal id="manage-group" centered title="Manage Group" @ok.prevent="submitManage()" @hidden="resetManageForm">
            <form ref="manageGroupForm">
                <b-form-group label="Role" label-for="role-input">
                    <multiselect id="role-input" v-model="selectedRole" track-by="name" label="name"
                                 placeholder="Manage Role" :options="roles"/>
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
    import GroupsNavbar from "../components/GroupsNavbar";
    import GroupsTable from "../components/GroupsTable";
    import {groupApiMixin} from "../mixins/group-api";
    import {userApiMixin} from "../mixins/user-api";
    import {roleApiMixin} from "../mixins/role-api";
    import {groupValidationMixin} from "../mixins/group-validation";

    export default {
        name: "Groups",
        mixins: [groupApiMixin, userApiMixin, roleApiMixin, groupValidationMixin],
        data() {
            return {
                group: {},
                selectedUsers: [],
                selectedRole: null,
            }
        },
        components: {
            GroupsNavbar, GroupsTable
        },
        created() {
            document.title = "User Manager - Groups";
            this.getGroups().then(response => {
                this.groups = response.data
            });
        },
        methods: {
            resetManageForm() {
                this.group = {}
            },
            editGroup(group) {
                this.group = {...group};
                this.$bvModal.show("edit-group")
            },
            manageGroup(group) {
                this.group = group;
                this.getGroupMetadata(group.id).then(response => {
                    this.selectedUsers = response.data.users;
                    this.selectedRole = response.data.role
                });
                this.getUsers().then(response => {
                    this.users = response.data
                });
                this.getRoles().then(response => {
                    this.roles = response.data
                });
                this.$bvModal.show("manage-group")
            },
            submitDelete(group) {
                if (!confirm("Are you sure?"))
                    return;
                this.deleteGroup(group.id).then(response => {
                    // Delete from table if success
                    if (response.status === 200) {
                        this.groups = this.groups.filter(_group => _group.id !== group.id);
                        // Show notification
                        this.$bvToast.toast(`Group ${group.name} deleted`, {
                            title: 'Group deleted',
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
                this.$v.group.$touch();
                if (this.$v.group.$anyError) {
                    return;
                }
                this.updateGroup(this.group).then(response => {
                    if (response.status === 200) {
                        this.group = {};
                        let groupIndex = this.groups.findIndex(group => group.id === response.data.id);
                        this.groups[groupIndex] = response.data;
                        this.$refs.groupsTable.refreshTable();
                        this.$nextTick(() => {
                            this.$bvModal.hide('edit-group')
                        });
                        this.$bvToast.toast(`Group ${response.data.name} updated`, {
                            title: 'Group updated',
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
                let role = ((this.selectedRole instanceof Object) ? this.selectedRole.id : null);
                console.log(users);
                console.log(role);
                this.updateGroupMetadata(this.group.id, {"role": role, "users": users}).then(response => {
                    if (response.status === 200) {
                        this.$nextTick(() => {
                            this.$bvModal.hide('manage-group')
                        });
                        this.$bvToast.toast(`Group ${this.group.name} updated`, {
                            title: 'Group updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        });
                        this.group = {};
                    } else {
                        this.$bvToast.toast(`Something went wrong. Error code: ${response.status}`, {
                            title: 'Error',
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                })
            },
            submitCreate(group) {
                this.createGroup(group).then(response => {
                    // Push to groups array
                    this.groups.push(response.data);
                    // Show notification
                    this.$bvToast.toast(`Group ${response.data.name} added`, {
                        title: 'Group added',
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