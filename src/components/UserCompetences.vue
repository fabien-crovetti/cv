<script setup>

import { ref } from "vue";

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
    <div class="text-center md:text-left">
        <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold mb-6">{{ $t('userCompetence.title') }}</h2>

        <div class="-m-3 flex flex-wrap">
            <div class="w-full min-w-0 p-3 lg:w-1/3 md:w-1/3" v-for="(competence, index) in userCompetences" :key="index" :class="index === 4 ? 'sm:w-full md:w-1/3' : 'sm:w-1/2 md:w-1/3'">
                <h3 class="text-xl font-medium leading-8 tracking-[0.15px] mb-4">{{ $t(`userCompetence.${competence.type}.name`) }}</h3>
                <p
                    v-for="(item, itemIndex) in competence.items"
                    :key="itemIndex"
                    class="mb-2 max-md:mx-auto max-md:w-[230px] max-md:max-w-full max-md:text-left"
                >
                    <span aria-hidden="true"  :class="item.iconName" class="mdi inline-flex align-middle text-2xl leading-none text-contrast mr-3" v-if="item.iconName"  />
                    <span>{{ $t(`userCompetence.${competence.type}.item${item.id}`) }}</span>
                </p>
            </div>
        </div>
    </div>

</template>
