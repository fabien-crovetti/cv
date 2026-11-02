import { createI18n } from 'vue-i18n'
import fr from '@/i18n/fr'
import en from '@/i18n/en'

export const DEFAULT_LOCALE = 'fr-FR'

export const SUPPORTED_LOCALES = ['fr-FR', 'en-US'] as const

export type Locale = typeof SUPPORTED_LOCALES[number]

const i18n = createI18n({
    legacy: false,
    globalInjection: true,
    warnHtmlMessage: false,
    locale: DEFAULT_LOCALE,
    fallbackLocale: DEFAULT_LOCALE,
    messages: {
        'fr-FR': fr,
        'en-US': en,
    },
})

/**
 * Restaure la langue enregistrée dans le navigateur.
 * À appeler uniquement après l'hydratation Vue.
 */
export function restoreLocale(): void {
    if (typeof window === 'undefined') return

    const savedLocale = localStorage.getItem('defaultLocale')

    if (
        savedLocale &&
        SUPPORTED_LOCALES.includes(savedLocale as Locale)
    ) {
        i18n.global.locale.value = savedLocale as Locale
    } else {
        localStorage.setItem('defaultLocale', DEFAULT_LOCALE)
    }
}

export default i18n
