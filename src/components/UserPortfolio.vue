<script setup>

import {ref} from "vue";

const portfolioImg = ref([
    new URL(`@/assets/portfolio01.png`, import.meta.url).href,
    new URL(`@/assets/portfolio02.png`, import.meta.url).href,
    new URL(`@/assets/portfolio03.png`, import.meta.url).href,
])

</script>

<template>
    <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold mb-10 text-center md:text-left">{{ $t('portfolio.title') }}</h2>

    <div class="-m-3 flex flex-wrap">
        <div class="w-full min-w-0 p-3 lg:w-1/3 md:w-1/3" v-for="n in 3"  :key="n">
            <section class="overflow-hidden rounded bg-white shadow-card mb-6">
                <div class="p-0">
                    <a class="no-underline text-primary font-bold block"  :href="$t(`portfolio.${n}.url`)" target="_blank" rel="noopener noreferrer">
                        <img class="block max-h-80 w-full object-cover" :src="portfolioImg[n-1]" :alt="$t(`portfolio.${n}.name`)" :title="$t(`portfolio.${n}.name`)" />
                    </a>
                </div>
                <div class="px-4 py-3">
                    <a class="no-underline text-primary font-bold block" :href="$t(`portfolio.${n}.url`)" target="_blank" rel="noopener noreferrer">{{ $t(`portfolio.${n}.name`) }}</a>
                    <p>{{ $t(`portfolio.${n}.information`) }}</p>
                    <hr class="border-0 border-t border-black/12 my-2" />
                    <div class="[&_ul]:list-disc [&_ul]:pl-4" v-html="$t(`portfolio.${n}.skills`)"/>
                </div>
            </section>
        </div>
    </div>
</template>
