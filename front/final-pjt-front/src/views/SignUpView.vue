<template>
  <div>
  <br>
  <form @submit.prevent="signUp" class="form-signup">
    <label for="username" class="form-label">ID  </label>
    <input class="form-input" type="text" name="uesrname" id="username" v-model.trim="username">
    <br>
    <label for="password1" class="form-label">비밀번호  </label>
    <input class="form-input" type="password" name="password1" id="password1" v-model.trim="password1">
    <br>
    <label for="password2" class="form-label">비밀번호 확인  </label>
    <input class="form-input" type="password" name="password2" id="password2" v-model.trim="password2">
    <br>
    <label for="email" class="form-label">이메일  </label>
    <input class="form-input" type="email" name="email" id="email" v-model.trim="email">
    <br>
    <label for="age" class="form-label">나이  </label>
    <input class="form-input" type="number" name="age" id="age" v-model.trim="age">
    <br>
    <label for="money" class="form-label">보유 잔고  </label>
    <input class="form-input" type="number" name="money" id="money" v-model.trim="money">
    <br>
    <label for="salary" class="form-label">연봉  </label>
    <input class="form-input" type="number" name="salary" id="salary" v-model.trim="salary">
    <br>
    <input type="submit" value="SignUp" class="submit-button">
  </form>
</div>
</template>

<script setup>
import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)
const age = ref(null)
const money = ref(null)
const salary = ref(null)

const signUp = function () {
const payload = {
  username: username.value,
  password1: password1.value,
  password2: password2.value,
  email: email.value,
  age: parseInt(age.value),  // 값이 정수로 변환되도록 parseInt를 추가
  money: parseInt(money.value),
  salary: parseInt(salary.value),
}
authStore.signUp(payload)
}

</script>

<style scoped>
.form-signup {
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