import {validationMixin} from "vuelidate";
import {required} from "vuelidate/lib/validators";

export const roleValidationMixin = {
    mixins: [validationMixin],
    validations: {
        role: {
            name: {
                required
            }
        }
    },
    methods: {
        validateRoleState(name) {
            const {$dirty, $error} = this.$v.role[name];
            return $dirty ? !$error : null;
        },
        resetRoleForm() {
            this.role = {
                name: null,
            };

            this.$nextTick(() => {
                this.$v.$reset();
            });
        },
    }
};