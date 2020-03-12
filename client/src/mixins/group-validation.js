import {validationMixin} from "vuelidate";
import {required} from "vuelidate/lib/validators";

export const groupValidationMixin = {
    mixins: [validationMixin],
    validations: {
        group: {
            name: {
                required
            }
        }
    },
    methods: {
        validateGroupState(name) {
            const {$dirty, $error} = this.$v.group[name];
            return $dirty ? !$error : null;
        },
        resetGroupForm() {
            this.group = {
                name: null,
            };

            this.$nextTick(() => {
                this.$v.$reset();
            });
        },
    }
};