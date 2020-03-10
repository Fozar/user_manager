import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Users from "../views/Users";
import Groups from "../views/Groups";
import Roles from "../views/Roles";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/users",
        name: "Users",
        component: Users
    },
    {
        path: "/groups",
        name: "Groups",
        component: Groups
    },
    {
        path: "/roles",
        name: "Roles",
        component: Roles
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router
