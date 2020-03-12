<template>
    <div id="navbar-wrapper">
        <b-navbar id="navbar" type="white" variant="white">
            <b-nav-form>
                <b-button pill v-b-modal.new-role variant="success">
                    <font-awesome-icon icon="plus"/>
                    New Role
                </b-button>
            </b-nav-form>
        </b-navbar>

        <b-modal id="new-role" centered title="New Role" @hidden="resetRoleForm"
                 @ok.prevent="submitCreate()">
            <form ref="newRoleForm">
                <b-form-group label="Name" label-for="name-input" invalid-feedback="Name is required">
                    <b-form-input id="name-input" v-model="role.name" :state="validateRoleState('name')"
                                  required type="text" name="name"/>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    import {roleValidationMixin} from "../mixins/role-validation";

    export default {
        name: "RolesNavbar",
        mixins: [roleValidationMixin],
        data() {
            return {
                role: {
                    name: ""
                },
            }
        },
        methods: {
            submitCreate() {
                this.$v.role.$touch();
                if (this.$v.role.$anyError) {
                    return;
                }
                this.$emit("submit-create", this.role);
                this.$nextTick(() => {
                    this.$bvModal.hide('new-role')
                })
            }
        }
    }
</script>

<style scoped>
    #navbar-wrapper {
        height: 6vh;
    }

    #navbar {
        height: 100%;
    }
</style>