<script setup>

import { useI18n } from "vue-i18n";
import {ref, onMounted} from "vue";

const defaultFlagClass = ref('flag-fr-FR')
const t = useI18n();

function selectLocale(locale){
    localStorage.setItem('defaultLocale',locale)
    defaultFlagClass.value = `flag-${locale}`

    t.locale.value = locale;
}

onMounted(()=>{
    if(localStorage.getItem('defaultLocale') === 'en-US'){
        defaultFlagClass.value = 'flag-en-US'
    }
})

</script>

<template>
    <div>
        <v-menu>
            <template v-slot:activator="{ props }">
            <span v-bind="props" class="cursor-pointer">
                <span class="flag-container" :class="defaultFlagClass"/>
                <v-icon icon="mdi-menu-down"/>
            </span>

            </template>
            <v-list width="100">
                <v-list-item>
                    <v-list-item-title class="cursor-pointer" @click="selectLocale('fr-FR')">
                        <span class="flag-container flag-fr-FR"/>
                        <span class="ml-5">FR</span>
                    </v-list-item-title>
                    <v-list-item-title class="cursor-pointer" @click="selectLocale('en-US')">
                        <span class="flag-container flag-en-US"/>
                        <span class="ml-5">EN</span>
                    </v-list-item-title>
                </v-list-item>
            </v-list>
        </v-menu>
    </div>
</template>

<style scoped lang="scss">

.flag-container{
    display: inline-block;
    width: 20px;
    height: 14px;
    background-size: cover;

    &.flag-fr-FR{
        background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAYAAAAougcOAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9bxVKqDnbQ4pChOlkQFXHUKhShQqgVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi6OSk6CIl/i8ptIjx4Lgf7+497t4B/kaFqWbXOKBqlpFOJoRsblXoeUUIQwiiD1GJmfqcKKbgOb7u4ePrXZxneZ/7c/QqeZMBPoF4lumGRbxBPL1p6Zz3iSOsJCnE58RjBl2Q+JHrsstvnIsO+3lmxMik54kjxEKxg+UOZiVDJZ4ijimqRvn+rMsK5y3OaqXGWvfkLwzntZVlrtMcRhKLWIIIATJqKKMCC3FaNVJMpGk/4eGPOn6RXDK5ymDkWEAVKiTHD/4Hv7s1C5MTblI4AXS/2PbHCNCzCzTrtv19bNvNEyDwDFxpbX+1Acx8kl5va7EjoH8buLhua/IecLkDDD7pkiE5UoCmv1AA3s/om3LAwC0QWnN7a+3j9AHIUFepG+DgEBgtUva6x7uDnb39e6bV3w8+1nKSUGk0ogAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+YKGQgWOSbmPuwAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAANklEQVQ4y2NkUJ76nwEP2DPLjsHZSQen/J9Hjxk+eYTjM4KBiYEOYNSSUUtGLRm1ZNSSYW8JALb8CHDGSv9LAAAAAElFTkSuQmCC");
    }
    &.flag-en-US{
        background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAIAAACn2JBZAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9bS6VUOthB1CFDdbIgKuKoVShChVArtOpgcukXNGlIUlwcBdeCgx+LVQcXZ10dXAVB8APE0clJ0UVK/F9SaBHjwXE/3t173L0D/M0qU82ecUDVLCOTSgq5/KoQekUEQwgjiKjETH1OFNPwHF/38PH1LsGzvM/9OfqUgskAn0A8y3TDIt4gnt60dM77xDFWlhTic+Ixgy5I/Mh12eU3ziWH/TwzZmQz88QxYqHUxXIXs7KhEk8RxxVVo3x/zmWF8xZntVpn7XvyF0YK2soy12kOI4VFLEGEABl1VFCFhQStGikmMrSf9PAPOn6RXDK5KmDkWEANKiTHD/4Hv7s1i5MTblIkCQRfbPtjBAjtAq2GbX8f23brBAg8A1dax19rAjOfpDc6WvwIiG4DF9cdTd4DLneAgSddMiRHCtD0F4vA+xl9Ux7ovwXCa25v7X2cPgBZ6ip9AxwcAqMlyl73eHdvd2//nmn39wMcEnKEy2zBYgAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+YMGwoNKbSqDFcAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAADFUlEQVQ4y2O8M2ueQmwkEzv7/gOn8qtWXn35gwEJnFqdzbVx3efJa3hzQ775B5mFTkWW1RJn768PUv/x4fWcJcpdDUwsvDyX4jM+3b7j5Gi+d1NNcbgWA3GgOFxr0+QE8a0bfj57prdinoCWJtOyR9+EinLuN3Y8WLJchJ+nvTlzx8wYNmZGPKawMDFunRyeY6X8rrhaOilWNSv9699/7d0LmapnnIyoWvk9PePfr1+XMvK/P3rk5mp1/1BDlp8qVoMy/VSvrcqQ3b/z5+3bepuXCRsanD5zxTOoqXr6SWZGQdOnH37P23BByUTZ0Mf5SV3rbzZmKUN9d3dzY1U+Xl4u1pvXf526xm6u9VtD08tKPkRd5F1br3RmslxY8Ldff2bOWRdStObph98MDAyMC5dsgdvJzcXhYmPw6fARFj4+CQdbRhaWv3//3WxshYS9el3Vu5Onvz1+LOHuyi4o8PXbjx07j3399h3h9xBnExQ//P0jbGXBwMDw/c1bqMCXrxDy55s33MqK3MqKf3/+/PbiJSMDg6elNrJWxhMCegxUAkwM1APUNIvx6/MX+FXc7er/Nn87V6KnclkhfpUsa/aeQY5HD3drbi6On+8/vNi5m0tWRsjcjJmHm4GBgZmHm11UlJmZ6f+fPy8OHP7z6ROfrc2eIxdR4jGhdiuENaHILtDPgZuL4/WJk4/qO0ULMo69/SF98QYXTOn5C9efPXvt6Wkjbm/7ZPPWu6m5puWFG869Kug9hAgvc0Xuk6uy8nIi2P//vdU36eXqDQLtjV07rwYWrEbzRUD+qoKSyS/fvJcL8lfta303e54P58+jCxLNFbkZGBiYWjPMt6+rMzXReXv+4iW/KHZVlcdOHtrhM6Ztuo01UKZvui1v27Br9zFOOTm9GROZ2Nk5ZsxY0RbRmmnOVFkWz83MdHvazKdzFwn1tE45ds87d+Wvv//xhPGff/890pdU1k5/8+GLQnSEUmPlu77JkTKcTB+uXb8UmcQuKfnSJ8A/d2HvymtEpoDeldec/Jv37j/Jp6Kst3DG3y9fATQDT+cRGyT7AAAAAElFTkSuQmCC");
    }
}



</style>
