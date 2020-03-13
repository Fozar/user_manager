<template>
    <div id="sidebar-wrapper" class="bg-dark">
        <ul class="sidebar-nav">
            <li class="sidebar-brand">
                <router-link tag="a" active-class="selected" to="/" exact>
                    <font-awesome-icon icon="user"/>
                    User Manager
                </router-link>
            </li>
            <li class="sidebar-brand">
                <router-link active-class="selected" exact tag="a" to="/auth" v-if="!loggedIn">
                    Log In
                </router-link>
                <b-link @click="logOut" v-else>
                    Log Out
                </b-link>
            </li>
            <li v-if="loggedIn">
                <router-link tag="a" active-class="selected" to="/users" exact>
                    Users
                </router-link>
            </li>
            <li v-if="loggedIn">
                <router-link tag="a" active-class="selected" to="/groups" exact>
                    User Groups
                </router-link>
            </li>
            <li v-if="loggedIn">
                <router-link tag="a" active-class="selected" to="/roles" exact>
                    User Roles
                </router-link>
            </li>
        </ul>
    </div>
</template>

<script>
    export default {
        name: "Sidebar",
        data() {
            return {
                get loggedIn() {
                    return localStorage.getItem('jwt') != null;
                }
            }
        },
        methods: {
            logOut() {
                localStorage.removeItem('user');
                localStorage.removeItem('jwt');
                this.$router.push('auth')
                location.reload();
            }
        }
    }
</script>

<style>
    #sidebar-wrapper {
        position: sticky;
        width: 100%;
        min-height: 100%;
        overflow-y: auto;
        background: #212529;
    }

    .sidebar-nav {
        position: absolute;
        top: 0;
        width: 100%;
        margin: 0;
        padding: 0;
        list-style: none;
    }

    .sidebar-nav li {
        border: 0 solid white;
        text-indent: 20px;
        line-height: 40px;
    }

    .sidebar-nav li a {
        display: block;
        text-decoration: none;
        color: #999999;
        -webkit-transition: all 0.2s ease;
        -moz-transition: all 0.2s ease;
        -o-transition: all 0.2s ease;
        transition: all 0.2s ease;
    }

    .sidebar-nav li a:hover {
        text-decoration: none;
        color: #fff;
        border-bottom-left-radius: 20px;
        border-top-left-radius: 20px;
        background: rgba(255, 255, 255, 0.3);
    }

    .sidebar-nav li a:active,
    .sidebar-nav li a:focus {
        text-decoration: none;
    }

    .selected,
    .selected:hover {
        margin-left: 10px;
        border-bottom-left-radius: 20px;
        border-top-left-radius: 20px;
        color: #999999 !important;
        background: #fff !important;
    }

    .sidebar-nav > .sidebar-brand {
        height: 65px;
        font-size: 18px;
        line-height: 60px;
    }

    .sidebar-nav > .sidebar-brand a {
        color: #999999;
    }

    .sidebar-nav > .sidebar-brand a:hover {
        color: #fff;
        background: none;
    }
</style>