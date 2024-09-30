<script setup>

import {ref} from "vue";
import { useMisc } from '@/composables/misc';

const { isMobileDisplay } = useMisc()


const portfolioImg = ref([
    new URL(`@/assets/portfolio01.png`, import.meta.url).href,
    new URL(`@/assets/portfolio02.png`, import.meta.url).href,
    new URL(`@/assets/portfolio03.png`, import.meta.url).href,
])

</script>

<template>
    <h4 class="text-h4 font-weight-bold mb-10" :class="isMobileDisplay() ? 'text-center' : ''">{{ $t('portfolio.title') }}</h4>

    <v-row>
        <v-col :cols="12" :xl="4" :lg="4" :md="4" v-for="n in 3"  :key="n">
            <v-card class="mb-6">
                <v-card-text class="pa-0">
                    <a class="text-decoration-none text-primary font-weight-bold d-block"  :href="$t(`portfolio.${n}.url`)" target="_blank">
                        <v-img
                            max-height="320"
                            cover
                            :src="portfolioImg[n-1]"
                            :alt="$t(`portfolio.${n}.name`)"
                            :tile="$t(`portfolio.${n}.name`)"
                        />
                    </a>
                </v-card-text>
                <v-card-item>
                    <a class="text-decoration-none text-primary font-weight-bold d-block" :href="$t(`portfolio.${n}.url`)" target="_blank">{{ $t(`portfolio.${n}.name`) }}</a>
                    <p>{{ $t(`portfolio.${n}.information`) }}</p>
                </v-card-item>
            </v-card>
        </v-col>
    </v-row>
</template>

<style scoped lang="scss">

</style>
