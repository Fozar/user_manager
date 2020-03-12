<template>
    <b-modal @hidden="resetManageForm" @ok.prevent="submitManage()" centered id="manage-group" title="Manage Group">
        <form>
            <b-form-group label="Role" label-for="role-input">
                <multiselect :options="roles" id="role-input" label="name" placeholder="Manage Role"
                             track-by="name" v-model="selectedRole"/>
            </b-form-group>
            <b-form-group label="Users" label-for="users-input">
                <multiselect :clear-on-select="false" :close-on-select="false" :multiple="true" :options="users"
                             :preselect-first="true" :preserve-search="true" id="users-input"
                             label="login" placeholder="Manage Users" track-by="id" v-model="selectedUsers">
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
    import {userApiMixin} from "../../mixins/api/user-api";
    import {roleApiMixin} from "../../mixins/api/role-api";
    import {groupApiMixin} from "../../mixins/api/group-api";

    export default {
        name: "ManageGroupModal",
        mixins: [groupApiMixin, userApiMixin, roleApiMixin],
        data() {
            return {
                group: {},
                roles: [],
                users: [],
                selectedUsers: [],
                selectedRole: {}
            }
        },
        methods: {
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
            resetManageForm() {
                this.group = {}
            },
            submitManage() {
                let users = this.selectedUsers.map(user => user.id);
                let role = ((this.selectedRole instanceof Object) ? this.selectedRole.id : null);
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