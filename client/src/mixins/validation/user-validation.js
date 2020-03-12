import {validationMixin} from "vuelidate";
import {email, required, sameAs} from "vuelidate/lib/validators";

export const userValidationMixin = {
    mixins: [validationMixin],
    validations: {
        user: {
            login: {
                required
            },
            password: {
                required
            },
            repeatPassword: {
                sameAsPassword: sameAs('password')
            },
            first_name: {
                required
            },
            last_name: {
                required
            },
            birthday: {
                required
            },
            email: {
                email
            }
        }
    },
    methods: {
        validateUserState(name) {
            const {$dirty, $error} = this.$v.user[name];
            return $dirty ? !$error : null;
        },
        resetUserForm() {
            this.user = {
                login: null,
                password: null,
                repeatPassword: null,
                first_name: null,
                last_name: null,
                birthday: null,
                email: null
            };

            this.$nextTick(() => {
                this.$v.$reset();
            });
        },
    }
};