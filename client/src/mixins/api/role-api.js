export const roleApiMixin = {
    data () {
        return {
            roles: []
        }
    },
    methods: {
        getRoles() {
            return this.axios.get(`/roles`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        createRole(role) {
            return this.axios.post("/roles", role, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getRole(role_id) {
            return this.axios.get(`/roles/${role_id}`).then(response => {
                return response.data
            }).catch((err) => {
                console.log(err)
            })
        },
        deleteRole(role_id) {
            // Delete role in DB
            return this.axios.delete(`/roles/${role_id}`, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateRole(role) {
            return this.axios.put(`/roles/${role.id}`, role, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getRoleMetadata(role_id) {
            return this.axios.get(`/roles/${role_id}/metadata`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateRoleMetadata(role_id, metadata) {
            return this.axios.put(`/roles/${role_id}/metadata`, metadata).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
    }
};