/**
 * plugins/vuetify.js
 *
 * Framework documentation: https://vuetifyjs.com`
 */

// Styles
import '@mdi/font/css/materialdesignicons.css'
import 'vuetify/styles'

// Composables
import { createVuetify } from 'vuetify'

// https://vuetifyjs.com/en/introduction/why-vuetify/#feature-guides
export default createVuetify({
    theme: {
        defaultTheme: 'light',
        themes:{
            light: {
                colors:{
                    // primary:'#1d4372',
                    // secondary:'#f8931f',
                    // contrast:'#dd434f',

                    primary:'#03bfc0',
                    secondary:'#f25170',
                    contrast:'#f1d194',

                    // primary:'#212832',
                    // secondary:'#2bc5ab',
                    // contrast:'#2bc5ab',
                }
            }
        }
    },
})
