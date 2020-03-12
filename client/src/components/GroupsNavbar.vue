<template>
    <div id="navbar-wrapper">
        <b-navbar id="navbar" type="white" variant="white">
            <b-nav-form>
                <b-button pill v-b-modal.new-group variant="success">
                    <font-awesome-icon icon="plus"/>
                    New Group
                </b-button>
            </b-nav-form>
        </b-navbar>

        <b-modal id="new-group" centered title="New Group" @hidden="resetGroupForm"
                 @ok.prevent="submitCreate()">
            <form ref="newGroupForm">
                <b-form-group label="Name" label-for="name-input"
                              invalid-feedback="Name is required">
                    <b-form-input id="name-input" v-model="group.name" :state="validateGroupState('name')"
                                  required type="text" name="name"/>
                </b-form-group>
            </form>
        </b-modal>
    </div>
</template>

<script>
    import {groupValidationMixin} from "../mixins/group-validation";

    export default {
        name: "GroupsNavbar",
        mixins: [groupValidationMixin],
        data() {
            return {
                group: {
                    name: ""
                },
            }
        },
        methods: {
            submitCreate() {
                this.$v.group.$touch();
                if (this.$v.group.$anyError) {
                    return;
                }
                this.$emit("submit-create", this.group);
                this.$nextTick(() => {
                    this.$bvModal.hide('new-group')
                })
            }
        }
    }
</script>

<style scoped>
    #navbar-wrapper {
        height: 6vh;
    }

    #navbar {
        height: 100%;
    }
</style>