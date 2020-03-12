export const roleApiMixin = {
    data () {
        return {
            roles: []
        }
    },
    methods: {
        getRoles() {
            return this.axios.get(`http://localhost:5000/roles`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        createRole(role) {
            return this.axios.post("http://localhost:5000/roles", role, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getRole(role_id) {
            return this.axios.get(`http://localhost:5000/roles/${role_id}`).then(response => {
                return response.data
            }).catch((err) => {
                console.log(err)
            })
        },
        deleteRole(role_id) {
            // Delete role in DB
            return this.axios.delete(`http://localhost:5000/roles/${role_id}`, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateRole(role) {
            return this.axios.put(`http://localhost:5000/roles/${role.id}`, role, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getRoleMetadata(role_id) {
            return this.axios.get(`http://localhost:5000/roles/${role_id}/metadata`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateRoleMetadata(role_id, metadata) {
            return this.axios.put(`http://localhost:5000/roles/${role_id}/metadata`, metadata).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
    }
};