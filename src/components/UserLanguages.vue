<script setup>
    import { ref } from "vue";

    const userLanguages = ref([
        {score:'4.5', countryCode:'Fr'},
        {score:'3', countryCode:'En'},
        {score:'0.5', countryCode:'Jp'},
    ])

</script>

<template>
    <h6 class="text-h6 mb-4">{{ $t('userLanguages.title') }}</h6>

    <div class="mb-4" v-for="(language, index) in userLanguages" :key="index">
        <span class="d-inline-block" style="width:100px;vertical-align: middle">{{ $t(`userLanguages.name${language.countryCode}`) }} :</span>
        <div class="d-inline-block" style="vertical-align: middle">
            <v-rating
                :size="43"
                :model-value="language.score"
                readonly
                empty-icon="mdi-circle-outline"
                full-icon="mdi-circle"
                half-icon="mdi-circle-half"
                half-increments
                color="contrast"
            ></v-rating>
        </div>
        <span class="ml-2 d-inline-block" style="vertical-align: middle">{{ $t(`userLanguages.label${language.countryCode}`) }}</span>
    </div>


</template>

<style scoped lang="scss">

</style>
