<script setup>
import { ref, onMounted, onBeforeUnmount, nextTick } from 'vue'
import { useI18n } from 'vue-i18n'

const { locale } = useI18n()
const open = ref(false)
const container = ref(null)
const trigger = ref(null)
const choices = ref([])

function close(returnFocus = false) {
    open.value = false
    if (returnFocus) trigger.value?.focus()
}
function selectLocale(value) {
    localStorage.setItem('defaultLocale', value)
    locale.value = value
    close(true)
}
function outside(event) {
    if (!container.value?.contains(event.target)) close()
}
async function focusChoice(index) {
    open.value = true
    await nextTick()
    choices.value[index]?.focus()
}
onMounted(() => document.addEventListener('pointerdown', outside))
onBeforeUnmount(() => document.removeEventListener('pointerdown', outside))
</script>

<template>
    <div ref="container" class="relative" @keydown.esc.stop.prevent="close(true)" @focusout="!container.contains($event.relatedTarget) && close()">
        <button ref="trigger" type="button" class="inline-flex items-center" :aria-label="locale === 'fr-FR' ? 'Choisir la langue' : 'Choose language'"
            :aria-expanded="open" aria-controls="locale-choices" @click="open = !open" @keydown.down.prevent="focusChoice(0)" @keydown.up.prevent="focusChoice(1)">
            <span aria-hidden="true" class="flag-container" :class="`flag-${locale}`" />
            <span aria-hidden="true" class="mdi mdi-menu-down text-2xl leading-none" />
        </button>
        <Transition enter-active-class="transition duration-150 ease-out" enter-from-class="scale-90 opacity-0" enter-to-class="scale-100 opacity-100"
            leave-active-class="transition duration-100 ease-in" leave-from-class="opacity-100" leave-to-class="opacity-0">
            <ul v-if="open" id="locale-choices" class="absolute right-0 z-20 w-[100px] origin-top-right rounded bg-white py-2 text-left text-black/87 shadow-lg">
                <li v-for="(value, index) in ['fr-FR', 'en-US']" :key="value">
                    <button ref="choices" type="button" class="flex w-full items-center px-4 py-1 hover:bg-black/5 focus-visible:bg-black/5"
                        :lang="value" :aria-pressed="locale === value" @click="selectLocale(value)"
                        @keydown.down.prevent="focusChoice((index + 1) % 2)" @keydown.up.prevent="focusChoice((index + 1) % 2)">
                        <span aria-hidden="true" class="flag-container shrink-0" :class="`flag-${value}`" />
                        <span class="ml-5">{{ value === 'fr-FR' ? 'FR' : 'EN' }}</span>
                    </button>
                </li>
            </ul>
        </Transition>
    </div>
</template>

<style scoped>

.flag-container{
    display: inline-block;
    width: 20px;
    height: 14px;
    background-size: cover;

}
.flag-container.flag-fr-FR {
        background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAYAAAAougcOAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9bxVKqDnbQ4pChOlkQFXHUKhShQqgVWnUwufQLmjQkKS6OgmvBwY/FqoOLs64OroIg+AHi6OSk6CIl/i8ptIjx4Lgf7+497t4B/kaFqWbXOKBqlpFOJoRsblXoeUUIQwiiD1GJmfqcKKbgOb7u4ePrXZxneZ/7c/QqeZMBPoF4lumGRbxBPL1p6Zz3iSOsJCnE58RjBl2Q+JHrsstvnIsO+3lmxMik54kjxEKxg+UOZiVDJZ4ijimqRvn+rMsK5y3OaqXGWvfkLwzntZVlrtMcRhKLWIIIATJqKKMCC3FaNVJMpGk/4eGPOn6RXDK5ymDkWEAVKiTHD/4Hv7s1C5MTblI4AXS/2PbHCNCzCzTrtv19bNvNEyDwDFxpbX+1Acx8kl5va7EjoH8buLhua/IecLkDDD7pkiE5UoCmv1AA3s/om3LAwC0QWnN7a+3j9AHIUFepG+DgEBgtUva6x7uDnb39e6bV3w8+1nKSUGk0ogAAAAZiS0dEAP8A/wD/oL2nkwAAAAlwSFlzAAALEwAACxMBAJqcGAAAAAd0SU1FB+YKGQgWOSbmPuwAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAAANklEQVQ4y2NkUJ76nwEP2DPLjsHZSQen/J9Hjxk+eYTjM4KBiYEOYNSSUUtGLRm1ZNSSYW8JALb8CHDGSv9LAAAAAElFTkSuQmCC");
    }

.flag-container.flag-en-US {
        background-image: url("data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABkAAAARCAIAAACn2JBZAAABhGlDQ1BJQ0MgcHJvZmlsZQAAKJF9kT1Iw0AcxV9bS6VUOthB1CFDdbIgKuKoVShChVArtOpgcukXNGlIUlwcBdeCgx+LVQcXZ10dXAVB8APE0clJ0UVK/F9SaBHjwXE/3t173L0D/M0qU82ecUDVLCOTSgq5/KoQekUEQwgjiKjETH1OFNPwHF/38PH1LsGzvM/9OfqUgskAn0A8y3TDIt4gnt60dM77xDFWlhTic+Ixgy5I/Mh12eU3ziWH/TwzZmQz88QxYqHUxXIXs7KhEk8RxxVVo3x/zmWF8xZntVpn7XvyF0YK2soy12kOI4VFLEGEABl1VFCFhQStGikmMrSf9PAPOn6RXDK5KmDkWEANKiTHD/4Hv7s1i5MTblIkCQRfbPtjBAjtAq2GbX8f23brBAg8A1dax19rAjOfpDc6WvwIiG4DF9cdTd4DLneAgSddMiRHCtD0F4vA+xl9Ux7ovwXCa25v7X2cPgBZ6ip9AxwcAqMlyl73eHdvd2//nmn39wMcEnKEy2zBYgAAAAlwSFlzAAAuIwAALiMBeKU/dgAAAAd0SU1FB+YMGwoNKbSqDFcAAAAZdEVYdENvbW1lbnQAQ3JlYXRlZCB3aXRoIEdJTVBXgQ4XAAADFUlEQVQ4y2O8M2ueQmwkEzv7/gOn8qtWXn35gwEJnFqdzbVx3efJa3hzQ775B5mFTkWW1RJn768PUv/x4fWcJcpdDUwsvDyX4jM+3b7j5Gi+d1NNcbgWA3GgOFxr0+QE8a0bfj57prdinoCWJtOyR9+EinLuN3Y8WLJchJ+nvTlzx8wYNmZGPKawMDFunRyeY6X8rrhaOilWNSv9699/7d0LmapnnIyoWvk9PePfr1+XMvK/P3rk5mp1/1BDlp8qVoMy/VSvrcqQ3b/z5+3bepuXCRsanD5zxTOoqXr6SWZGQdOnH37P23BByUTZ0Mf5SV3rbzZmKUN9d3dzY1U+Xl4u1pvXf526xm6u9VtD08tKPkRd5F1br3RmslxY8Ldff2bOWRdStObph98MDAyMC5dsgdvJzcXhYmPw6fARFj4+CQdbRhaWv3//3WxshYS9el3Vu5Onvz1+LOHuyi4o8PXbjx07j3399h3h9xBnExQ//P0jbGXBwMDw/c1bqMCXrxDy55s33MqK3MqKf3/+/PbiJSMDg6elNrJWxhMCegxUAkwM1APUNIvx6/MX+FXc7er/Nn87V6KnclkhfpUsa/aeQY5HD3drbi6On+8/vNi5m0tWRsjcjJmHm4GBgZmHm11UlJmZ6f+fPy8OHP7z6ROfrc2eIxdR4jGhdiuENaHILtDPgZuL4/WJk4/qO0ULMo69/SF98QYXTOn5C9efPXvt6Wkjbm/7ZPPWu6m5puWFG869Kug9hAgvc0Xuk6uy8nIi2P//vdU36eXqDQLtjV07rwYWrEbzRUD+qoKSyS/fvJcL8lfta303e54P58+jCxLNFbkZGBiYWjPMt6+rMzXReXv+4iW/KHZVlcdOHtrhM6Ztuo01UKZvui1v27Br9zFOOTm9GROZ2Nk5ZsxY0RbRmmnOVFkWz83MdHvazKdzFwn1tE45ds87d+Wvv//xhPGff/890pdU1k5/8+GLQnSEUmPlu77JkTKcTB+uXb8UmcQuKfnSJ8A/d2HvymtEpoDeldec/Jv37j/Jp6Kst3DG3y9fATQDT+cRGyT7AAAAAElFTkSuQmCC");
    }
</style>
