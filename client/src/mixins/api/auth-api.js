export const authApiMixin = {
    methods: {
        login(credentials) {
            return this.axios.post("/auth/login", {
                "login": credentials.login,
                "password": credentials.password
            }, {
                "withCredentials": true
            }).then(response => {
                return response
            }).catch((err) => {
                console.log(err)
            });
        }
    }
};