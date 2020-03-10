<template>
    <b-table :items="groups" :fields="fields" sticky-header="94vh" striped :no-border-collapse="true" :hover="true"
             responsive="xl" show-empty class="group-table" ref="groupsTable">
        <template v-slot:empty="scope">
            <h4 class="text-center">{{ scope.emptyText }}</h4>
        </template>
        <template v-slot:emptyfiltered="scope">
            <h4 class="text-center">{{ scope.emptyFilteredText }}</h4>
        </template>
        <template v-slot:cell(actions)="row">
            <div class="container">
                <b-button size="sm" @click="$emit('edit-group', row.item)" variant="outline-secondary" class="mr-1">
                    Edit
                </b-button>
                <b-button size="sm" @click="$emit('manage-group', row.item)" variant="outline-secondary" class="mr-1">
                    Manage Role/Users
                </b-button>
                <b-button size="sm" @click="$emit('delete-group', row.item)" variant="outline-danger">
                    Delete
                </b-button>
            </div>
        </template>
    </b-table>
</template>

<script>
    export default {
        name: "GroupsTable",
        props: ["groups"],
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
                this.$refs.groupsTable.refresh()
            }
        }
    }


</script>

<style scoped>
    .group-table {
        -webkit-transition: all 0.2s ease;
        -moz-transition: all 0.2s ease;
        -o-transition: all 0.2s ease;
        transition: all 0.2s ease;
        padding-left: 16px;
        padding-right: 16px;
    }
</style>