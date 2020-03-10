<template>
    <div id="page-content-wrapper">
        <transition name="fade" mode="out-in">
            <router-view/>
        </transition>
    </div>
</template>

<script>
    export default {
        name: "Content"
    }
</script>

<style scoped>
    #page-content-wrapper {
        width: 100%;
        height: 100vh;
    }

    .fade-enter-active, .fade-leave-active {
        transition: opacity .2s;
    }

    .fade-enter, .fade-leave-to
    {
        opacity: 0;
    }
</style>