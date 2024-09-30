
import { useDisplay } from 'vuetify'
export function useMisc() {


    const display = useDisplay()


    const isMobileDisplay = () => {

        switch (display.name.value) {
            case 'xs': return true
            case 'sm': return true
        }
        return false
    }


    return {
        isMobileDisplay
    }

}
