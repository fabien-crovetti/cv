

<script setup>
//
</script>

<template>
    <v-app>
        <v-main class="pa-6">
            <router-view />
        </v-main>
    </v-app>
</template>

<style lang="scss">

body{
    background-image: url('assets/background.png') !important;
    background-size: cover !important;
    background-attachment: fixed !important;
    height: 100vh;
}
#app{
    background: transparent !important;
}
.v-application{
    background: transparent !important;
}

</style>
