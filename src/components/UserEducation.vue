<script setup>

import { useMisc } from '@/composables/misc';

const { isMobileDisplay } = useMisc()
</script>

<template>

    <h4 class="text-h4 font-weight-bold" :class="isMobileDisplay() ? 'text-center' : ''">{{ $t('userEducation.title') }}</h4>

    <div class="mt-6">
        <div v-if="isMobileDisplay()">
            <div class="mb-8" v-for="n in 2" :key="n">
                <v-row>
                    <v-col :cols="6" class="pa-0">
                        <p class="text-h5">{{ $t(`userEducation.${n}.title`) }} </p>
                    </v-col>
                    <v-col :cols="6" class="text-right pa-0">
                        <v-chip color="primary">{{ $t(`userEducation.${n}.date`) }}</v-chip>
                    </v-col>
                    <v-col :cols="12" class="pa-0">
                        <p class="text-body-1">{{ $t(`userEducation.${n}.location`) }}</p>
                    </v-col>
                    <v-col :cols="12" class="pa-0">
                        <p class="mt-2">{{ $t(`userEducation.${n}.information`) }}</p>
                    </v-col>
                </v-row>
            </div>
        </div>
        <v-timeline side="start" v-else>
            <v-timeline-item dot-color="contrast" v-for="n in 2"  :key="n">
                <template v-slot:opposite>
                    <v-chip color="primary">{{ $t(`userEducation.${n}.date`) }}</v-chip>
                </template>
                <div :class="n === 2 ? 'pl-6' : ''">
                    <p class="text-h5">{{ $t(`userEducation.${n}.title`) }}</p>
                    <p class="text-body-1">{{ $t(`userEducation.${n}.location`) }}</p>
                    <p class="mt-2">{{ $t(`userEducation.${n}.information`) }}</p>
                </div>
            </v-timeline-item>

        </v-timeline>
    </div>
</template>

<style scoped lang="scss">

</style>
