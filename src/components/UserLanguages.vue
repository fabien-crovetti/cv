<template>
    <h2 class="text-xl font-medium leading-8 mb-4">{{ $t('userLanguages.title') }}</h2>
    <ul class="space-y-2">
        <li v-for="code in ['Fr', 'En', 'Jp']" :key="code">
            <strong>{{ $t(`userLanguages.name${code}`) }}</strong> — {{ $t(`userLanguages.label${code}`) }}
        </li>
    </ul>
</template>
