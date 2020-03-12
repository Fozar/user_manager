<template>
    <div>
        <GroupsNavbar/>
        <GroupsTable v-bind:groups="groups" @delete-group="submitDelete" @edit-group="editGroup"
                     @manage-group="manageGroup" ref="groupsTable"/>

        <NewGroupModal @add-group-to-table="addGroupToTable" ref="newGroupModal"/>

        <EditGroupModal @update-group-in-table="updateGroupInTable" ref="editGroupModal"/>

        <ManageGroupModal ref="manageGroupModal"/>
    </div>
</template>

<script>
    import GroupsNavbar from "../components/navbars/GroupsNavbar";
    import GroupsTable from "../components/tables/GroupsTable";
    import {groupApiMixin} from "../mixins/api/group-api";
    import NewGroupModal from "../components/modals/NewGroupModal";
    import EditGroupModal from "../components/modals/EditGroupModal";
    import ManageGroupModal from "../components/modals/ManageGroupModal";

    export default {
        name: "Groups",
        mixins: [groupApiMixin],
        components: {
            GroupsNavbar, GroupsTable, NewGroupModal, EditGroupModal, ManageGroupModal
        },
        created() {
            document.title = "User Manager - Groups";
            this.getGroups().then(response => {
                this.groups = response.data
            });
        },
        methods: {
            editGroup(group) {
                this.$refs.editGroupModal.editGroup(group)
            },
            manageGroup(group) {
                this.$refs.manageGroupModal.manageGroup(group)
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
            addGroupToTable(group) {
                this.groups.push(group)
            },
            updateGroupInTable(group) {
                let groupIndex = this.groups.findIndex(_group => _group.id === group.id);
                this.groups[groupIndex] = group;
                this.$refs.groupsTable.refreshTable();
            }
        }
    }
</script>

<style scoped>
</style>