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


    </div>
</template>

<script>
    import {roleValidationMixin} from "../../mixins/validation/role-validation";

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
        methods: {}
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