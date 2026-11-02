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

            <div class="w-full min-w-0 p-3 lg:w-1/4 text-center" >
                <user-profile/>
            </div>

            <div class="w-full min-w-0 p-3 lg:w-3/4" >
                <section class="rounded bg-white shadow-card">
                    <div class="p-4 text-sm leading-[1.425] px-12">

                        <user-about/>

                        <hr class="border-0 border-t border-black/12 my-10" />

                        <div class="-m-3 flex flex-wrap">
                            <div class="w-full min-w-0 p-3 lg:w-1/2 md:w-1/2" >
                                <personal-information/>
                            </div>
                            <div class="w-full min-w-0 p-3 lg:w-1/2 md:w-1/2" >
                                <user-languages/>
                            </div>
                        </div>

                        <hr class="border-0 border-t border-black/12 my-10" />

                        <user-competences/>

                    </div>
                </section>

                <section class="rounded bg-white shadow-card mt-10">
                    <div class="p-4 text-sm leading-[1.425] px-12">

                        <professional-experience/>

                        <hr class="border-0 border-t border-black/12 my-10" />

                        <user-education/>

                    </div>
                </section>

                <section class="rounded bg-white shadow-card mt-10 pb-10">
                    <div class="p-4 text-sm leading-[1.425] px-12">

                        <user-portfolio/>

                        <hr class="border-0 border-t border-black/12 my-10" />

                       <user-interest/>

                    </div>
                </section>

            </div>
        </div>
    </div>

</template>
