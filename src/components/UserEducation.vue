<template>
    <h2 class="text-[34px] leading-10 tracking-[0.25px] font-bold text-center md:text-left">{{ $t('userEducation.title') }}</h2>
    <ol class="mt-6 md:py-6">
        <li v-for="n in 2" :key="n" class="relative mb-8 grid grid-cols-2 md:mb-0 md:gap-x-6 md:pb-6 md:last:pb-0 md:grid-cols-[minmax(0,1fr)_38px_auto]">
            <div class="text-right md:col-start-3 md:row-start-1 md:text-left"><span class="inline-flex min-h-8 items-center rounded-full bg-primary/12 px-3 text-sm text-primary">{{ $t(`userEducation.${n}.date`) }}</span></div>
            <div aria-hidden="true" class="relative hidden justify-center md:col-start-2 md:row-start-1 md:flex">
                <span class="absolute -top-6 bottom-0 w-0.5 bg-black/12" />
                <span class="relative flex size-[38px] shrink-0 items-center justify-center rounded-full bg-[#f5f5f5]">
                    <span class="size-[30px] rounded-full bg-contrast" />
                </span>
            </div>
            <h3 class="text-2xl leading-8 wrap-break-word col-start-1 row-start-1 md:hidden">{{ $t(`userEducation.${n}.title`) }}</h3>
            <div class="col-span-2 md:hidden"><p class="text-base leading-6 tracking-[0.5px]">{{ $t(`userEducation.${n}.location`) }}</p>
                <p class="mt-2">{{ $t(`userEducation.${n}.information`) }}</p></div>
            <div class="hidden md:row-start-1 md:block md:col-start-1">
                <h3 class="text-2xl leading-8 wrap-break-word">{{ $t(`userEducation.${n}.title`) }}</h3>
                <p class="text-base leading-6 tracking-[0.5px]">{{ $t(`userEducation.${n}.location`) }}</p>
                <p class="mt-2">{{ $t(`userEducation.${n}.information`) }}</p>
            </div>
        </li>
    </ol>
</template>
