<template>
    <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold text-center md:text-left">{{ $t('professionalExperiences.title') }}</h2>
    <ol class="mt-6 md:py-6">
        <li v-for="n in 5" :key="n" class="relative mb-8 grid grid-cols-2 md:mb-0 md:gap-x-6 md:pb-6 md:last:pb-0 md:grid-cols-[auto_38px_minmax(0,1fr)]">
            <div class="pb-2 md:col-start-1 md:row-start-1 md:text-right"><span class="inline-flex min-h-8 items-center rounded-full bg-primary/12 px-3 text-sm text-primary">{{ $t(`professionalExperiences.${n}.date`) }}</span></div>
            <div aria-hidden="true" class="relative hidden justify-center md:col-start-2 md:row-start-1 md:flex">
                <span class="absolute -top-6 bottom-0 w-0.5 bg-black/12" />
                <span class="relative flex size-[38px] shrink-0 items-center justify-center rounded-full bg-[#f5f5f5]">
                    <span class="size-[30px] rounded-full bg-contrast" />
                </span>
            </div>
            <h3 class="text-2xl leading-8 wrap-break-word text-right md:hidden">{{ $t(`professionalExperiences.${n}.title`) }}</h3>
            <div class="col-span-2 md:hidden"><p class="text-base leading-6 tracking-[0.5px]">{{ $t(`professionalExperiences.${n}.location`) }}</p>
                <ul class="mt-3 list-disc pl-5 space-y-2">
                    <li v-for="(bullet, index) in $tm(`professionalExperiences.${n}.bullets`)" :key="index">{{ $rt(bullet) }}</li>
                </ul></div>
            <div class="hidden md:row-start-1 md:block md:col-start-3">
                <h3 class="text-2xl leading-8 wrap-break-word">{{ $t(`professionalExperiences.${n}.title`) }}</h3>
                <p class="text-base leading-6 tracking-[0.5px]">{{ $t(`professionalExperiences.${n}.location`) }}</p>
                <ul class="mt-3 list-disc pl-5 space-y-2">
                    <li v-for="(bullet, index) in $tm(`professionalExperiences.${n}.bullets`)" :key="index">{{ $rt(bullet) }}</li>
                </ul>
            </div>
        </li>
    </ol>
</template>
