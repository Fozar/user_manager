<template>
    <b-modal @hidden="resetRoleForm" @ok.prevent="submitCreate()" centered id="new-role"
             title="New Role">
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
        name: "NewRoleModal",
        mixins: [roleValidationMixin, roleApiMixin],
        data() {
            return {
                role: {
                    name: null
                }
            }
        },
        methods: {
            submitCreate() {
                this.$v.role.$touch();
                if (this.$v.role.$anyError) {
                    return;
                }
                this.createRole(this.role).then(response => {
                    // Push to roles array
                    this.$emit('add-role-to-table', response.data);
                    // Show notification
                    this.$bvToast.toast(`Role ${response.data.name} added`, {
                        title: 'Role added',
                        autoHideDelay: 5000,
                        variant: "dark"
                    })
                });
                this.$nextTick(() => {
                    this.$bvModal.hide('new-role')
                })
            }
        }
    }
</script>

<style scoped>

</style>