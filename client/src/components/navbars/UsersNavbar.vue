<template>
    <div id="navbar-wrapper">
        <b-navbar id="navbar" type="white" variant="white">
            <b-nav-form>
                <b-button pill v-b-modal.new-user variant="success">
                    <font-awesome-icon icon="plus"/>
                    New User
                </b-button>
            </b-nav-form>
        </b-navbar>
    </div>
</template>

<script>
    export default {
        name: "UsersNavbar",
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