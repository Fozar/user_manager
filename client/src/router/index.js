import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Users from "../views/Users";
import Groups from "../views/Groups";
import Roles from "../views/Roles";
import Auth from "../views/Auth";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "Home",
        component: Home
    },
    {
        path: "/auth",
        name: "Auth",
        component: Auth,
        meta: {
            guest: true
        }
    },
    {
        path: "/users",
        name: "Users",
        component: Users,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: "/groups",
        name: "Groups",
        component: Groups,
        meta: {
            requiresAuth: true
        }
    },
    {
        path: "/roles",
        name: "Roles",
        component: Roles,
        meta: {
            requiresAuth: true
        }
    }
];

let router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

router.beforeEach((to, from, next) => {
    if (to.matched.some(record => record.meta.requiresAuth)) {
        if (localStorage.getItem('jwt') == null) {
            next({
                path: '/auth',
                params: {nextUrl: to.fullPath}
            })
        } else {
            next()
        }
    } else if (to.matched.some(record => record.meta.guest)) {
        if (localStorage.getItem('jwt') == null) {
            next()
        } else {
            next({name: 'Users'})
        }
    } else {
        next()
    }
});

export default router
