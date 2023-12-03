<template>
    <div class="main">
        <img src="@/img/logo.png" alt="" class="logo">
        <br>
        <div class="main-img">
            <img src="@/img/2.jpg" alt="" class="img">
            <h1 class="first">요람에서</h1><h1 class="second">무덤까지</h1>
            <h1 class="third">당신과 함께하는 금융</h1>
        </div>
        
        <!-- <br>
        <RouterLink :to="{name:'financedepositproduct'}" class="button">예금 한눈에</RouterLink>
        <br>
        <RouterLink :to="{name: 'financesavingproducts'}" class="button">적금 한눈에</RouterLink>
        <br>
        <RouterLink :to="{name: 'exchangerate'}" class="button">환율 계산</RouterLink>
        <br>
        <RouterLink :to="{name: 'map'}" class="button">은행 찾기</RouterLink> -->
    </div>
</template>

<script setup>

</script>

<style scoped>
.main {
    text-align: center;
    padding-bottom: 100px;
}
.button {
    text-decoration: none;
    color:#F8973F;
    font-size: 30px;
}
.logo {
    width: 150px;
    height: 150px;
}
.first {
    color: black;
    position: absolute;
    top: 5%;
    left: 30%;
}
.second {
    color: black;
    position: absolute;
    top: 5%;
    right: 30%;
}
.img {
    text-align: center;
    width: 50%;
    height: 50%;
}
.main-img {
    position: relative;
}
.third {
    color: black;
    position: absolute;
    bottom: 0%;
    left: 50%;
    transform: translate(-50%, -50%);
}
</style>