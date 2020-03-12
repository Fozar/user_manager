<template>
    <b-table :items="users" :fields="fields" sticky-header="94vh" striped :no-border-collapse="true" :hover="true"
             show-empty class="user-table" ref="usersTable">
        <template v-slot:empty="scope">
            <h4 class="text-center">{{ scope.emptyText }}</h4>
        </template>
        <template v-slot:emptyfiltered="scope">
            <h4 class="text-center">{{ scope.emptyFilteredText }}</h4>
        </template>
        <template v-slot:cell(actions)="row">
            <b-button size="sm" @click="$emit('edit-user', row.item)" variant="outline-secondary" class="mr-1">
                Edit
            </b-button>
            <b-button size="sm" @click="$emit('manage-user', row.item)" variant="outline-secondary" class="mr-1">
                Manage Role/Groups
            </b-button>
            <b-button size="sm" @click="$emit('delete-user', row.item)" variant="outline-danger">
                Delete
            </b-button>
        </template>
    </b-table>
</template>

<script>
    export default {
        name: "UsersTable",
        props: ["users"],
        data() {
            return {
                fields: [
                    {key: 'id', stickyColumn: true, isRowHeader: true},
                    'login',
                    'first_name',
                    "last_name",
                    {
                        key: "birthday",
                        formatter: (value, key, item) => {
                            return new Date(item.birthday).toLocaleDateString()
                        }
                    },
                    {
                        key: "created_at",
                        formatter: (value, key, item) => {
                            return new Date(item.created_at).toLocaleString()
                        }
                    },
                    "email",
                    "actions"
                ]
            }
        },
        methods: {
            refreshTable() {
                this.$refs.usersTable.refresh()
            }
        }
    }


</script>

<style scoped>
    .user-table {
        -webkit-transition: all 0.2s ease;
        -moz-transition: all 0.2s ease;
        -o-transition: all 0.2s ease;
        transition: all 0.2s ease;
        padding-left: 16px;
        padding-right: 16px;
    }
</style>