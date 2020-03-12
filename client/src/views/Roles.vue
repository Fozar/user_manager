<template>
    <div>
        <RolesNavbar/>
        <RolesTable v-bind:roles="roles" @delete-role="submitDelete" @edit-role="editRole"
                    @manage-role="manageRole" ref="rolesTable"/>

        <NewRoleModal @add-role-to-table="addRoleToTable" ref="newRoleModal"/>
        <EditRoleModal @update-role-in-table="updateRoleInTable" ref="editRoleModal"/>
        <ManageRoleModal ref="manageRoleModal"/>
    </div>
</template>

<script>
    import {roleApiMixin} from "../mixins/api/role-api";
    import RolesNavbar from "../components/navbars/RolesNavbar";
    import RolesTable from "../components/tables/RolesTable";
    import NewRoleModal from "../components/modals/NewRoleModal";
    import EditRoleModal from "../components/modals/EditRoleModal";
    import ManageRoleModal from "../components/modals/ManageRoleModal";

    export default {
        name: "Roles",
        mixins: [roleApiMixin],
        components: {
            RolesNavbar, RolesTable, NewRoleModal, EditRoleModal, ManageRoleModal
        },
        created() {
            document.title = "User Manager - Roles";
            this.getRoles().then(response => {
                this.roles = response.data
            });
        },
        methods: {
            editRole(role) {
                this.$refs.editRoleModal.editRole(role)
            },
            manageRole(role) {
                this.$refs.manageRoleModal.manageRole(role)
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
            addRoleToTable(role) {
                this.roles.push(role)
            },
            updateRoleInTable(role) {
                let roleIndex = this.roles.findIndex(_role => _role.id === role.id);
                this.roles[roleIndex] = role;
                this.$refs.rolesTable.refreshTable();
            }
        }
    }
</script>

<style scoped>
</style>