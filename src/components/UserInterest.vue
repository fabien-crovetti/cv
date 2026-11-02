<script setup>

import { ref } from 'vue'

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
    <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold mb-10 text-center md:text-left">{{ $t('interest.title') }}</h2>

    <div class="-m-3 flex flex-wrap">
        <div class="w-full min-w-0 p-3 lg:w-1/3 md:w-1/3" v-for="(interest, index) in userInterest" :key="index">
            <p class="text-xl font-medium leading-8 tracking-[0.15px] max-md:mx-auto max-md:w-[230px] max-md:max-w-full max-md:text-left">
                <span aria-hidden="true"   :class="interest" class="mdi inline-flex align-middle text-2xl leading-none text-secondary mr-4" />{{ $t(`interest.item${index+1}`) }}
            </p>
        </div>
    </div>
</template>
