<template>
    <b-modal @hidden="resetManageForm" @ok.prevent="submitManage()" centered id="manage-user" title="Manage User">
        <form>
            <b-form-group label="Role" label-for="role-input">
                <multiselect :options="roles" id="role-input" label="name" placeholder="Manage Role"
                             track-by="name" v-model="selectedRole"/>
            </b-form-group>
            <b-form-group label="Groups" label-for="groups-input">
                <multiselect :clear-on-select="false" :close-on-select="false" :multiple="true" :options="groups"
                             :preselect-first="true" :preserve-search="true" id="groups-input"
                             label="name" placeholder="Manage Groups" track-by="id" v-model="selectedGroups"/>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import {userApiMixin} from "../../mixins/api/user-api";
    import {groupApiMixin} from "../../mixins/api/group-api";
    import {roleApiMixin} from "../../mixins/api/role-api";

    export default {
        name: "ManageUserModal",
        mixins: [userApiMixin, groupApiMixin, roleApiMixin],
        data() {
            return {
                user: {},
                roles: [],
                groups: [],
                selectedGroups: [],
                selectedRole: {}
            }
        },
        methods: {
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
            resetManageForm() {
                this.user = {}
            },
            submitManage() {
                let groups = this.selectedGroups.map(group => group.id);
                let role = ((this.selectedRole instanceof Object) ? this.selectedRole.id : null);
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