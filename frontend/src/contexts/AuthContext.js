import React, {useState, useEffect, useContext} from "react"
import axios from "axios"

axios.defaults.xsrfCookieName = "csrftoken"
axios.defaults.xsrfHeaderName = "X-CSRFToken"
axios.defaults.withCredentials = true
let client = axios.create({
    baseURL: "http://127.0.0.1:8000"
})

export function useAuth() {
    return useContext(AuthContext)
}

const AuthContext = React.createContext()

export function AuthProvider({children}) {
    const [currentUser, setCurrentUser] = useState()

    const register = (email, password) => {
        client.post(
            "/register",
            {
                email: email,
                password: password
            }
        ).then((res) => {
            login(email, password)
        }).catch((error) => {
            console.log(error)
        })
    }

    const login = (email, password) => {
        client.post(
            "/login",
            {
                email: email,
                password: password
            }
        ).then((res) => {
            client.get("/user")
                .then((res) => {
                    setCurrentUser(res.data.user.email)
                }).catch((error) => {
                    console.log(error)
                })
        }).catch((error) => {
            console.log(error)
        })
    }

    const logout = () => {
        client.post("/logout")
            .then((res) => {
                setCurrentUser()
            }).catch((error) => {
                console.log(error)
        })
    }

    useEffect(() => {
        client.get("/user")
            .then((res) => {
                setCurrentUser(res.data.user.email)
            })
            .catch((error) => {
                setCurrentUser()
            })
    },[])

    const value = {
        currentUser,
        register,
        login,
        logout,
    }

    return (
        <AuthContext.Provider value={value}>
            {children}
        </AuthContext.Provider>
    )
}
