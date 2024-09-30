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
        <v-row>

            <v-col :cols="12" :xl="3" :lg="3" class="text-center">
                <user-profile/>
            </v-col>

            <v-col :cols="12" :xl="9" :lg="9" >
                <v-card>
                    <v-card-text class="px-12">

                        <user-about/>

                        <v-divider class="my-10"/>

                        <v-row>
                            <v-col :cols="12" :xl="6" :lg="6" :md="6">
                                <personal-information/>
                            </v-col>
                            <v-col :cols="12" :xl="6" :lg="6" :md="6">
                                <user-languages/>
                            </v-col>
                        </v-row>

                        <v-divider class="my-10"/>

                        <user-competences/>

                    </v-card-text>
                </v-card>

                <v-card class="mt-10">
                    <v-card-text class="px-12">

                        <professional-experience/>

                        <v-divider class="my-10"/>

                        <user-education/>

                    </v-card-text>
                </v-card>


                <v-card class="mt-10 pb-10">
                    <v-card-text class="px-12">

                        <user-portfolio/>

                        <v-divider class="my-10"/>

                       <user-interest/>

                    </v-card-text>
                </v-card>

            </v-col>
        </v-row>
    </div>


</template>

<style scoped lang="scss">

</style>
