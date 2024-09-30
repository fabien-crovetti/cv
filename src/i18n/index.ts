
import { createI18n } from 'vue-i18n'
import fr from "@/i18n/fr";
import en from "@/i18n/en";




let defaultLocale  = 'fr-FR'

if(localStorage.getItem('defaultLocale')){
    defaultLocale = localStorage.getItem('defaultLocale') || ""
}else{
    if(navigator.language){
        localStorage.setItem('defaultLocale',defaultLocale)
    }
}

const i18n = createI18n({
    legacy:false,
    warnHtmlMessage: false,
    locale: defaultLocale,
    fallbackLocale: 'fr-FR',
    messages:{
        'fr-FR':fr,
        'en-US':en,
    }
})
export default i18n
