<template>
    <b-modal @hidden="resetGroupForm" @ok.prevent="submitEdit()" centered id="edit-group" title="Edit Group">
        <form>
            <b-form-group invalid-feedback="Name is required" label="Name" label-for="name-input">
                <b-form-input :state="validateGroupState('name')" id="name-input" name="name"
                              required type="text" v-model="group.name"/>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>

    import {groupApiMixin} from "../../mixins/api/group-api";
    import {groupValidationMixin} from "../../mixins/validation/group-validation";

    export default {
        name: "EditGroupModal",
        mixins: [groupValidationMixin, groupApiMixin],
        data() {
            return {
                group: {}
            }
        },
        methods: {
            editGroup(group) {
                this.group = {...group};
                this.$bvModal.show("edit-group")
            },
            submitEdit() {
                this.$v.group.$touch();
                if (this.$v.group.$anyError) {
                    return;
                }
                this.updateGroup(this.group).then(response => {
                    if (response.status === 200) {
                        this.$emit('update-group-in-table', response.data);
                        this.$nextTick(() => {
                            this.$bvModal.hide('edit-group')
                        });
                        this.$bvToast.toast(`Group ${response.data.name} updated`, {
                            title: 'Group updated',
                            autoHideDelay: 5000,
                            variant: "dark"
                        })
                    } else {
                        this.$bvToast.toast(`Something went wrong. Error code: ${response.status}`, {
                            title: 'Error',
                            autoHideDelay: 5000,
                            variant: "danger"
                        })
                    }
                })
            },
        }
    }
</script>

<style scoped>

</style>