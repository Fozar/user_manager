<template>
    <b-modal @hidden="resetGroupForm" @ok.prevent="submitCreate()" centered id="new-group"
             title="New Group">
        <form>
            <b-form-group invalid-feedback="Name is required" label="Name"
                          label-for="name-input">
                <b-form-input :state="validateGroupState('name')" id="name-input" name="name"
                              required type="text" v-model="group.name"/>
            </b-form-group>
        </form>
    </b-modal>
</template>

<script>
    import {groupValidationMixin} from "../../mixins/validation/group-validation";
    import {groupApiMixin} from "../../mixins/api/group-api";

    export default {
        name: "NewGroupModal",
        mixins: [groupValidationMixin, groupApiMixin],
        data() {
            return {
                group: {
                    name: null
                }
            }
        },
        methods: {
            submitCreate() {
                this.$v.group.$touch();
                if (this.$v.group.$anyError) {
                    return;
                }
                this.createGroup(this.group).then(response => {
                    // Push to groups array
                    this.$emit('add-group-to-table', response.data);
                    // Show notification
                    this.$bvToast.toast(`Group ${response.data.name} added`, {
                        title: 'Group added',
                        autoHideDelay: 5000,
                        variant: "dark"
                    })
                });
                this.$nextTick(() => {
                    this.$bvModal.hide('new-group')
                })
            }
        }
    }
</script>

<style scoped>

</style>