<script setup>

import {ref, computed} from "vue";
import { useMisc } from '@/composables/misc';
import { useI18n } from "vue-i18n";
import LocaleSelector from "@/layout/LocaleSelector.vue";

const { isMobileDisplay } = useMisc()
const t = useI18n();

const userImg = ref(new URL(`@/assets/user.png`, import.meta.url).href);
const linkedInImg = ref(new URL(`@/assets/linkedin.png`, import.meta.url).href);

const pdfPath = computed(()=>{
    if(t.locale.value === 'en-US'){
        return new URL(`/cv-fabien-crovetti-en.pdf`, import.meta.url).href
    }
    return new URL(`/cv-fabien-crovetti-fr.pdf`, import.meta.url).href
})

</script>

<template>
    <v-card color="secondary" style="position: sticky; top: 22px">
        <v-card-text>
            <locale-selector class="text-right"/>
            <v-img
                :width="isMobileDisplay() ? 120 : 220"
                aspect-ratio="1/1"
                cover
                :src="userImg"
                class="mx-auto"
            ></v-img>
            <h5 class="text-h5 font-weight-bold mt-4">CROVETTI Fabien</h5>
            <h6 class="text-h6 mt-4 mb-4">{{ $t('userProfile.job') }}</h6>
            <div>
                <a href="https://www.linkedin.com/in/fabien-crovetti-240738278/" class="d-inline-block mr-4" style="vertical-align: middle" target="_blank"><img :src="linkedInImg" alt="linkedIn" width="24"></a>
                <a :href="pdfPath" target="_blank" class="d-inline-block text-decoration-none text-contrast font-weight-bold" style="vertical-align: middle">{{ $t('userProfile.download') }}</a>
            </div>
        </v-card-text>
    </v-card>
</template>

<style scoped lang="scss">

</style>
