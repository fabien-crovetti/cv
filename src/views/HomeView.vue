<script setup>

import UserProfile from "@/components/UserProfile.vue";

import UserAbout from "@/components/UserAbout.vue";
import PersonalInformation from "@/components/PersonalInformation.vue";
import UserLanguages from "@/components/UserLanguages.vue";
import UserCompetences from "@/components/UserCompetences.vue";

import ProfessionalExperience from "@/components/ProfessionalExperience.vue";
import UserEducation from "@/components/UserEducation.vue";
import UserPortfolio from "@/components/UserPortfolio.vue";
import UserInterest from "@/components/UserInterest.vue";

</script>

<template>
    <div class="mx-auto" style="max-width: 1400px">
        <div class="-m-3 flex flex-wrap">
            <aside class="w-full min-w-0 p-3 lg:w-1/4 text-center"><user-profile/></aside>
            <div class="w-full min-w-0 p-3 lg:w-3/4 space-y-10">
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><user-about/></section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><professional-experience/></section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><user-competences/></section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-8"><div><personal-information/></div><div><user-languages/></div></div>
                </section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><user-portfolio/></section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><user-education/></section>
                <section class="rounded bg-white shadow-card p-5 sm:p-8 md:px-12"><user-interest/></section>
            </div>
        </div>
    </div>
</template>
