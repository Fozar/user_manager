<template>
    <b-modal @hidden="resetManageForm" @ok.prevent="submitManage()" centered id="manage-role" title="Manage Role">
        <form ref="manageRoleForm">
            <b-form-group label="Groups" label-for="groups-input">
                <multiselect :clear-on-select="false" :close-on-select="false" :multiple="true" :options="groups"
                             :preselect-first="true" :preserve-search="true" id="groups-input"
                             label="name" placeholder="Manage Groups" track-by="name" v-model="selectedGroups">
                    <template slot="selection" slot-scope="{ values, search, isOpen }">
                            <span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">
                                {{ values.length }} groups selected
                            </span>
                    </template>
                </multiselect>
            </b-form-group>
            <b-form-group label="Users" label-for="users-input">
                <multiselect :clear-on-select="false" :close-on-select="false" :multiple="true" :options="users"
                             :preselect-first="true" :preserve-search="true" id="users-input"
                             label="login" placeholder="Manage Users" track-by="login" v-model="selectedUsers">
                    <template slot="selection" slot-scope="{ values, search, isOpen }">
                            <span class="multiselect__single" v-if="values.length &amp;&amp; !isOpen">
                                {{ values.length }} users selected
                            </span>
                    </template>
                </multiselect>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import {groupApiMixin} from "../../mixins/api/group-api";
    import {userApiMixin} from "../../mixins/api/user-api";
    import {roleApiMixin} from "../../mixins/api/role-api";

    export default {
        name: "ManageRoleModal",
        mixins: [groupApiMixin, userApiMixin, roleApiMixin],
        data() {
            return {
                role: {},
                users: [],
                groups: [],
                selectedUsers: [],
                selectedGroups: []
            }
        },
        methods: {
            manageRole(role) {
                this.role = role;
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
            resetManageForm() {
                this.role = {}
            },
            submitManage() {
                let users = this.selectedUsers.map(user => user.id);
                let groups = this.selectedGroups.map(group => group.id);
                this.updateRoleMetadata(this.role.id, {"groups": groups, "users": users}).then(response => {
                    if (response.status === 200) {
                        this.$nextTick(() => {
                            this.$bvModal.hide('manage-role')
                        });
                        this.$bvToast.toast(`Role ${this.role.name} updated`, {
                            title: 'Role updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        });
                        this.role = {};
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