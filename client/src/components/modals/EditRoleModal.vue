<template>
    <b-modal @hidden="resetRoleForm" @ok.prevent="submitEdit()" centered id="edit-role" title="Edit Role">
        <form>
            <b-form-group invalid-feedback="Name is required" label="Name" label-for="name-input">
                <b-form-input :state="validateRoleState('name')" id="name-input" name="name"
                              required type="text" v-model="role.name"/>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import {roleValidationMixin} from "../../mixins/validation/role-validation";
    import {roleApiMixin} from "../../mixins/api/role-api";

    export default {
        name: "EditRoleModal",
        mixins: [roleValidationMixin, roleApiMixin],
        data() {
            return {
                role: {}
            }
        },
        methods: {
            editRole(role) {
                this.role = {...role};
                this.$bvModal.show("edit-role")
            },
            submitEdit() {
                this.$v.role.$touch();
                if (this.$v.role.$anyError) {
                    return;
                }
                this.updateRole(this.role).then(response => {
                    if (response.status === 200) {
                        this.$emit('update-role-in-table', response.data);
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
        }
    }
</script>

<style scoped>

</style>