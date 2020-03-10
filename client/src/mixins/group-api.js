export const groupApiMixin = {
    data () {
        return {
            groups: []
        }
    },
    methods: {
        getGroups() {
            return this.axios.get(`http://localhost:5000/groups`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        createGroup(group) {
            return this.axios.post("http://localhost:5000/groups", group, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getGroup(id) {
            return this.axios.get(`http://localhost:5000/groups/${id}`).then(response => {
                return response.data
            }).catch((err) => {
                console.log(err)
            })
        },
        deleteGroup(group_id) {
            // Delete group in DB
            return this.axios.delete(`http://localhost:5000/groups/${group_id}`, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateGroup(group) {
            return this.axios.put(`http://localhost:5000/groups/${group.id}`, group, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        },
        getGroupMetadata(group_id) {
            return this.axios.get(`http://localhost:5000/groups/${group_id}/metadata`).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
        updateGroupMetadata(group_id, metadata) {
            return this.axios.put(`http://localhost:5000/groups/${group_id}/metadata`, metadata).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            })
        },
    }
};