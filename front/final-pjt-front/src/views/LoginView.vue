<template>
  <div>
      <br>
      <form @submit.prevent="logIn" class="form-login">
          <label for="username" class="form-label">ID</label>
          <input type="text" v-model.trim="username" class="form-input">
          <br>
          
          <label for="password" class="form-label">비밀번호</label>
          <input type="password" v-model.trim="password" class="form-input">
          <input type="submit" value="login" class="submit-button">
      </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const username = ref(null)
const password = ref(null)

const logIn = function () {
const payload = {
  username: username.value,
  password: password.value
}
authStore.logIn(payload)
}
</script>

<style scoped>


.form-login {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
  color: black;
}

.form-input {
  width: calc(100% - 20px);
  padding: 10px;
  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  margin-bottom: 8px;
}

.submit-button {
  display: block;
  width: 100%;
  padding: 10px;
  font-size: 16px;
  background-color: #F8973F;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}

.submit-button:hover {
  background-color: #ffbc7e;
}
</style>