<template>
    <div class="text-center md:text-left">
        <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold mb-6">{{ $t('userCompetence.title') }}</h2>
        <div class="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6 text-left">
            <div v-for="(group, index) in $tm('competenceGroups')" :key="index">
                <h3 class="text-xl font-medium leading-8 mb-3">{{ $rt(group.name) }}</h3>
                <ul class="space-y-2"><li v-for="(item, itemIndex) in group.items" :key="itemIndex">{{ $rt(item) }}</li></ul>
            </div>
        </div>
    </div>
</template>
