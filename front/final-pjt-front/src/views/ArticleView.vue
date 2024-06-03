<template>
    <div>
        <h1>자유게시판</h1>
        <RouterLink :to="{name:'articlecreate'}" class="create-button">게시글 생성</RouterLink>
        <ul class="ul">
            <div v-for="article in articlestore.articleList"
            :key="article.pk"
            :article="article"
            @click="goDetail(article.pk)"
            >
            <h3>{{ article.title }}</h3>
            <hr>
            </div>
        </ul>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router'
import { onMounted } from 'vue'
import { useArticleStore } from '@/stores/articles'
import { useRouter } from 'vue-router'



const router = useRouter()
const articlestore = useArticleStore()


onMounted(()=> {
    articlestore.getArticleList()
})

const goDetail = (pk) => {
    router.push({name:'articledetail', params:{pk: pk}})
}

</script>

<style scoped>
.create-button {
    text-decoration: none;
    color: black;
    float: right;
}
.ul {
    margin-top: 70px;
    margin-bottom: 100px;
}
</style>