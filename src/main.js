import '@/styles/main.css'
import '@mdi/font/css/materialdesignicons.css'
import 'roboto-fontface/css/roboto/roboto-fontface.css'
import { routes } from '@/router'

import App from './App.vue'
import i18n, { restoreLocale } from '@/i18n'

import { ViteSSG } from 'vite-ssg'

export const createApp = ViteSSG(
    App,
    {
        routes,
        base: import.meta.env.BASE_URL,
    },
    ({ app, router, isClient, head }) => {
        app.use(i18n)
        if (!isClient) head.push({ htmlAttrs: { lang: 'fr' } })

        if (isClient) {
            app.mixin({
                mounted() {
                    if (this.$root === this) {
                        restoreLocale()
                    }
                },
            })
            // Workaround pour les erreurs de chargement dynamique
            router.onError((err, to) => {
                if (err?.message?.includes?.('Failed to fetch dynamically imported module')) {
                    if (!localStorage.getItem('cv:dynamic-reload')) {
                        console.log('Reloading page to fix dynamic import error')
                        localStorage.setItem('cv:dynamic-reload', 'true')
                        location.assign(to.fullPath)
                    } else {
                        console.error('Dynamic import error, reloading page did not fix it', err)
                    }
                } else {
                    console.error(err)
                }
            })

            router.isReady().then(() => {
                localStorage.removeItem('cv:dynamic-reload')
            })
        }
    },
)
