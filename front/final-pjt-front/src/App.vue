<template>
  <header class="header">
    <a href="http://localhost:5173/">
      <img src="@/img/logo.png" alt="" class="logo">
    </a>
    <nav v-if="authStore.isLogin">
      <form @submit.prevent="authStore.logOut" >
        <input type="submit" value="LogOut" class="logout">
      </form>
    </nav>
    <nav v-else >
      <RouterLink :to="{ name: 'signup'}" class="logout">SignUp</RouterLink> <span></span>
      <RouterLink :to="{ name: 'login'}" class="logout">Login</RouterLink>
      
    </nav>
  </header>
  <div>
  <div v-if="authStore.isLogin" class="menu">
    <RouterLink :to="{name: 'main'}" class="button">HOME</RouterLink> |
    <RouterLink :to="{name: 'articles'}" class="button">자유게시판</RouterLink> |
    <RouterLink :to="{name:'financedepositproduct'}" class="button">예금</RouterLink> |
    <RouterLink :to="{name: 'financesavingproducts'}" class="button">적금</RouterLink> |
    <RouterLink :to="{name: 'exchangerate'}" class="button">환율 계산</RouterLink> |
    <RouterLink :to="{name: 'map'}" class="button">은행 찾기</RouterLink> |
    <RouterLink :to="{name: 'profile'}" class="button">Profile</RouterLink> |
    <a class="button" href="https://frogue.danbee.ai/toad?chatbot_id=4c839121-c416-424e-8732-4baf42c200be&force_welcome=Y">나에게 맞는 상품 찾기</a>
  </div>
  <div v-else class="menu">
    <RouterLink :to="{name: 'main'}" class="button">HOME</RouterLink> |
    <RouterLink :to="{name:'financedepositproduct'}" class="button">예금</RouterLink> |
    <RouterLink :to="{name: 'financesavingproducts'}" class="button">적금</RouterLink> |
    <RouterLink :to="{name: 'exchangerate'}" class="button">환율 계산</RouterLink> |
    <RouterLink :to="{name: 'map'}" class="button">은행 찾기</RouterLink> |
    <a class="button" href="https://frogue.danbee.ai/toad?chatbot_id=4c839121-c416-424e-8732-4baf42c200be&force_welcome=Y">나에게 맞는 상품 찾기</a>
  </div>
  <RouterView />
  <button></button>
  <!-- <iframe src="https://frogue.danbee.ai/toad?chatbot_id=4c839121-c416-424e-8732-4baf42c200be&force_welcome=Y" allow="microphone; autoplay" allowusermedia="true" style="position: fixed; right: 40px; bottom: 40px; width: 350px; height: 600px; border-radius: 20px; border: 0; box-shadow: rgba(79, 98, 114, 0.2) 0px 6px 60px 0px;"></iframe> -->
</div>
  <div class="footer">
    &copy; <a href="https://youtu.be/ZRyxH-db4iY?si=mBRA8MMadhs7Vp4F" class="easteregg">2023 치트와 수트</a>
  </div>
</template>

<script setup>
import { RouterLink, RouterView } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
</script>

<style scoped>

.header {
  background-color: whitesmoke;
  text-align: right;
}

.menu{
  background-color: #EA6046;
  color: white;
  text-align:center;
  border-radius: 5px;
  width: auto;
  height: 40px;
  margin-top: 20px;
  padding-top: 10px;
  font-size: 18px;
}
.footer {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #333;
  color: #fff;
  text-align: center;
  padding: 10px;
}
.logout {
  background-color: #EA6046;
  color: #fff;
  padding: 5px 15px;
  margin: 5px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-size: 14px;
}
.auth {
  position: fixed;
  top: 0;
  right: 0;
  text-align: right;
  padding: 15px;
  background-color: black;
  color: #F8973F;
}
.easteregg {
  text-decoration-line: none;
  text-decoration: none;
  color: #fff;
}
.button {
  text-decoration: none;
  text-decoration-line: none;
  color: white;
}
.logo {
  width: 2%;
  height: 2%;
  float: left;
}
</style>
