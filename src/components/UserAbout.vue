<script setup>

import { useMisc } from '@/composables/misc';

const { isMobileDisplay } = useMisc()
</script>

<template>
    <div :class="isMobileDisplay() ? 'text-center' : ''">
        <h4 class="text-h4 font-weight-bold mb-6">{{ $t('userAbout.title') }}</h4>
        <p class="mb-2">{{ $t('userAbout.text1') }}</p>
        <p class="mb-2">{{ $t('userAbout.text2') }}</p>
        <p class="mb-2">{{ $t('userAbout.text3') }}</p>
        <p class="mb-2">{{ $t('userAbout.text4') }}</p>
    </div>

</template>

<style scoped lang="scss">

</style>
