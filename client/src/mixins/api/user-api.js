export const userApiMixin = {
    data() {
        return {
            users: []
        }
    },
    methods: {
        getUsers() {
            return this.axios.get(`/users`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        createUser(user) {
            return this.axios.post("/users", user, {
                "withCredentials": true
            }).then(response => {
                return response
            })
        },
        getUser(id) {
            return this.axios.get(`/users/${id}`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        deleteUser(user_id) {
            // Delete user in DB
            return this.axios.delete(`/users/${user_id}`, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateUser(user) {
            return this.axios.put(`/users/${user.id}`, user, {
                "withCredentials": true
            }).then(response => {
                return response
            })
        },
        getUserMetadata(user_id) {
            return this.axios.get(`/users/${user_id}/metadata`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateUserMetadata(user_id, metadata) {
            return this.axios.put(`/users/${user_id}/metadata`, metadata).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
    }
};