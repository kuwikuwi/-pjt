<!-- Profile.vue -->

<template>
    <div class="container">
      <h1>User Profile</h1>
      <div v-if="user">
        <p><strong>Username:</strong> {{ user.username }}</p>
        <p><strong>Email:</strong> {{ user.email }}</p>
        <br>
        <p><strong>가입한상품</strong></p>
        <p>준비중 입니다</p>
        <br>
        <p><strong>상품 비교</strong></p>
        <p>준비중 입니다</p>
        <button class="button" @click.prevent="err">회원정보 수정</button>
        <button class="button" @click.prevent="err">회원 탈퇴</button>
      </div>
      <div v-else class="container">
        <p>Loading...</p>
      </div>
    </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';

const user = ref(null);

onMounted(() => {
axios.get('http://127.0.0.1:8000/accounts/profile/')
    .then(response => {
    user.value = response.data;
    })
    .catch(error => {
    console.error('Error fetching user profile:', error);
    });
});

const err = () => {
  alert('준비중입니다.')
}

// export { user };
</script>

<style scoped>
/* 스타일링을 추가하거나 필요에 따라 수정하세요. */
.container {
  background-color: whitesmoke;
  color: black;
  text-align: center;
  margin: auto 0;
}
.button {
  width: 150px;
  background-color: whitesmoke;
  color: black;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
}
.button:hover {
  background-color: darkgray;
}
</style>
