<script setup>

import { ref } from 'vue'
import { useMisc } from '@/composables/misc';

const { isMobileDisplay } = useMisc()


const userInterest = ref([
    'mdi-motorbike',
    'mdi-tools',
    'mdi-dice-d20',
    'mdi-controller',
    'mdi-book-open-variant-outline',
    'mdi-guitar-acoustic',
])

</script>

<template>
    <h4 class="text-h4 font-weight-bold mb-10" :class="isMobileDisplay() ? 'text-center' : ''">{{ $t('interest.title') }}</h4>

    <v-row>
        <v-col :cols="12" :xl="4" :lg="4" :md="4" v-for="(interest, index) in userInterest" :key="index">
            <p class="text-h6" :class="isMobileDisplay() ? 'mobile-list-container' : ''">
                <v-icon color="secondary" :icon="interest" class="mr-4"/>{{ $t(`interest.item${index+1}`) }}
            </p>
        </v-col>
    </v-row>
</template>

<style scoped lang="scss">

</style>
