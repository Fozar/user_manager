<template>
    <div id="wrapper">
        <Sidebar />
        <Content />
    </div>
</template>

<script>
    import Sidebar from "./Sidebar"
    import Content from "./Content";

    export default {
        name: "Wrapper",
        components: {
            Sidebar, Content
        }
    }
</script>

<style scoped>
    #wrapper {
        height: 100%;
        display: grid;
        grid-template-columns: 13% auto;
    }
</style>