<template>
    <b-table :items="roles" :fields="fields" sticky-header="94vh" striped :no-border-collapse="true" :hover="true"
             responsive="xl" show-empty class="role-table" ref="rolesTable">
        <template v-slot:empty="scope">
            <h4 class="text-center">{{ scope.emptyText }}</h4>
        </template>
        <template v-slot:emptyfiltered="scope">
            <h4 class="text-center">{{ scope.emptyFilteredText }}</h4>
        </template>
        <template v-slot:cell(actions)="row">
            <b-button size="sm" @click="$emit('edit-role', row.item)" variant="outline-secondary" class="mr-1">
                Edit
            </b-button>
            <b-button size="sm" @click="$emit('manage-role', row.item)" variant="outline-secondary" class="mr-1">
                Manage Groups/Users
            </b-button>
            <b-button size="sm" @click="$emit('delete-role', row.item)" variant="outline-danger">
                Delete
            </b-button>
        </template>
    </b-table>
</template>

<script>
    export default {
        name: "RolesTable",
        props: ["roles"],
        data() {
            return {
                fields: [
                    {key: 'id', stickyColumn: true, isRowHeader: true},
                    'name',
                    "actions"
                ]
            }
        },
        methods: {
            refreshTable() {
                this.$refs.rolesTable.refresh()
            }
        }
    }


</script>

<style scoped>
    .role-table {
        -webkit-transition: all 0.2s ease;
        -moz-transition: all 0.2s ease;
        -o-transition: all 0.2s ease;
        transition: all 0.2s ease;
        padding-left: 16px;
        padding-right: 16px;
    }
</style>