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

        <b-modal id="new-role" centered title="New Role" @show="resetRoleForm"
                 @ok.prevent="submitCreate()">
            <form ref="newRoleForm">
                <b-form-group :state="nameState" label="Name" label-for="name-input"
                              invalid-feedback="Name is required">
                    <b-form-input id="name-input" v-model="role.name" :state="nameState"
                                  required type="text" name="name"/>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    export default {
        name: "RolesNavbar",
        data() {
            return {
                role: {
                    name: ""
                },
                nameState: null,
            }
        },
        methods: {
            checkFormValidity() {
                const valid = this.$refs.newRoleForm.checkValidity();
                this.nameState = valid;
                return valid
            },
            resetRoleForm() {
                this.role.name = "";
                this.nameState = null;
            },
            submitCreate() {
                if (!this.checkFormValidity())
                    return;
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