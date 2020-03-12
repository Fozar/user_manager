export const userApiMixin = {
    data () {
        return {
            users: []
        }
    },
    methods: {
        getUsers() {
            return this.axios.get(`http://localhost:5000/users`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        createUser(user) {
            return this.axios.post("http://localhost:5000/users", user, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getUser(id) {
            return this.axios.get(`http://localhost:5000/users/${id}`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        deleteUser(user_id) {
            // Delete user in DB
            return this.axios.delete(`http://localhost:5000/users/${user_id}`, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateUser(user) {
            return this.axios.put(`http://localhost:5000/users/${user.id}`, user, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getUserMetadata(user_id) {
            return this.axios.get(`http://localhost:5000/users/${user_id}/metadata`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateUserMetadata(user_id, metadata) {
            return this.axios.put(`http://localhost:5000/users/${user_id}/metadata`, metadata).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
    }
};