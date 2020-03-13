<template>
  <b-container class="mt-5 p-5 w-50 text-center border border-dark rounded-bottom rounded-lg">
      <HelloWorld/>
  </b-container>
</template>

<script>
    // @ is an alias to /src
    import HelloWorld from '@/components/HelloWorld.vue'

    export default {
        name: 'Home',
        created() {
            document.title = "User Manager";
        },
        components: {
            HelloWorld
        }
    }
</script>
