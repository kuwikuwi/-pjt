import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useAuthStore = defineStore('counter', () => {
  const router = useRouter()
  const API_URL = 'http://127.0.0.1:8080'
  const token = ref(null)
  const isLogin = computed(() => {
      if (token.value === null) {
      return false
      } else {
      return true
      }
  })
  const signUp = function (payload) {
    const { username, password1, password2, email, age, money, salary } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        username, 
        password1, 
        password2,
        email,
        age,
        money,
        salary,
      }
    })
      .then((res) => {
        console.log(res)
        const password = password1
        logIn({ username, password })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((res) => {
        console.log(res.data)
        token.value = res.data.key
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((res) => {
        token.value = null
        router.push({ name: 'main' })
      })
      .catch((err) => {
        console.log(err)
      })
    }
  return { signUp, logIn, logOut, isLogin, token, API_URL }
}, {persist: true})
