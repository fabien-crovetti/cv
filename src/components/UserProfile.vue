<script setup>

import {ref, computed} from "vue";
import { useI18n } from "vue-i18n";
import LocaleSelector from "@/layout/LocaleSelector.vue";

const t = useI18n();

const userImg = ref(new URL(`@/assets/user.png`, import.meta.url).href);
const linkedInImg = ref(new URL(`@/assets/linkedin.png`, import.meta.url).href);

const pdfPath = computed(()=>{
    if(t.locale.value === 'en-US'){
        return `${import.meta.env.BASE_URL}cv-fabien-crovetti-en.pdf`
    }
    return `${import.meta.env.BASE_URL}cv-fabien-crovetti-fr.pdf`
})

</script>

<template>
    <section class="sticky top-[22px] rounded bg-secondary text-white shadow-card">
        <div class="p-4 text-sm leading-[1.425]">
            <locale-selector class="text-right"/>
            <img :src="userImg" alt="CROVETTI Fabien" class="mx-auto size-[120px] object-cover md:size-[220px]" />
            <h1 class="text-2xl leading-8 font-bold mt-4">CROVETTI Fabien</h1>
            <p class="text-xl font-medium leading-8 tracking-[0.15px] mt-4 mb-4">{{ $t('userProfile.job') }}</p>
            <div>
                <a href="https://www.linkedin.com/in/fabien-crovetti-240738278/" class="inline-block mr-4" style="vertical-align: middle" target="_blank" rel="noopener noreferrer"><img :src="linkedInImg" alt="linkedIn" width="24"></a>
                <a :href="pdfPath" target="_blank" rel="noopener noreferrer" class="inline-block no-underline text-contrast font-bold" style="vertical-align: middle">{{ $t('userProfile.download') }}</a>
            </div>
        </div>
    </section>
</template>
