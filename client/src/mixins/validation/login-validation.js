import {validationMixin} from "vuelidate";
import {required} from "vuelidate/lib/validators";

export const authValidationMixin = {
    mixins: [validationMixin],
    validations: {
        credentials: {
            login: {
                required
            },
            password: {
                required
            }
        }
    },
    methods: {
        validateAuthState(name) {
            const {$dirty, $error} = this.$v.credentials[name];
            return $dirty ? !$error : null;
        },
    }
};