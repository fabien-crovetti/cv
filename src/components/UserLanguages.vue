<script setup>
    import { ref } from "vue";

    const userLanguages = ref([
        {score:'4.5', countryCode:'Fr'},
        {score:'3', countryCode:'En'},
        {score:'0.5', countryCode:'Jp'},
    ])

</script>

<template>
    <h3 class="text-xl font-medium leading-8 tracking-[0.15px] mb-4">{{ $t('userLanguages.title') }}</h3>

    <div class="mb-4" v-for="(language, index) in userLanguages" :key="index">
        <span class="inline-block" style="width:100px;vertical-align: middle">{{ $t(`userLanguages.name${language.countryCode}`) }} :</span>
        <div class="inline-block" style="vertical-align: middle">
            <span class="inline-flex text-contrast align-middle" role="img" :aria-label="`${language.score} / 5`">
                <span v-for="n in 5" :key="n" aria-hidden="true" class="mdi inline-flex size-[43px] items-center justify-center text-[25px]"
                    :class="Number(language.score) >= n ? 'mdi-circle' : Number(language.score) >= n - 0.5 ? 'mdi-circle-half' : 'mdi-circle-outline'" />
            </span>
        </div>
        <span class="ml-2 inline-block" style="vertical-align: middle">{{ $t(`userLanguages.label${language.countryCode}`) }}</span>
    </div>

</template>
