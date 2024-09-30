<script setup>

import { ref } from "vue";
import { useMisc } from '@/composables/misc';

const { isMobileDisplay } = useMisc()
const userCompetences = ref([
    {
        type:'framework',
        items:[
            {id:1, iconName:'mdi-language-php'},
            {id:2, iconName:'mdi-nodejs'},
            {id:3, iconName:'mdi-vuejs'},
            {id:4, iconName:'mdi-language-python'},
            {id:5, iconName:'mdi-bash'},
        ]
    },
    {
        type:'method',
        items:[
            {id:1, iconName:'mdi-all-inclusive-box'},
            {id:2, iconName:'mdi-cog-clockwise'},
            {id:3, iconName:'mdi-pyramid'},
        ]
    },
    {
        type:'devOps',
        items:[
            {id:1, iconName:'mdi-linux'},
            {id:2, iconName:'mdi-git'},
            {id:3, iconName:'mdi-docker'},
            {id:4, iconName:'mdi-ansible'},
            {id:5, iconName:'mdi-database'},
            {id:6, iconName:'mdi-server-network'},
        ]
    },
    {
        type:'other',
        items:[{id:1},{id:2},{id:3}]
    },
    {
        type:'softSkill',
        items:[{id:1},{id:2},{id:3},{id:4}]
    },

])


</script>

<template>
    <div :class="isMobileDisplay() ? 'text-center' : ''">
        <h4 class="text-h4 font-weight-bold mb-6">{{ $t('userCompetence.title') }}</h4>

        <v-row >
            <v-col :cols="12" :xl="4" :lg="4" :md="4" :sm="index === 4 ? 12 : 6" v-for="(competence, index) in userCompetences" :key="index">
                <h6 class="text-h6 mb-4">{{ $t(`userCompetence.${competence.type}.name`) }}</h6>
                <p
                    v-for="(item, itemIndex) in competence.items"
                    :key="itemIndex"
                    class="mb-2"
                    :class="isMobileDisplay() ? 'mobile-list-container' : ''"
                >
                    <v-icon :icon="item.iconName" color="contrast" class="mr-3" v-if="item.iconName" />
                    <span>{{ $t(`userCompetence.${competence.type}.item${item.id}`) }}</span>
                </p>
            </v-col>
        </v-row>
    </div>

</template>

<style scoped lang="scss">

</style>
