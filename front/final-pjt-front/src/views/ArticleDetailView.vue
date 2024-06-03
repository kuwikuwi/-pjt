<template>
    <div class="post-detail">
        <!-- <h1>게시글</h1> -->
        <div class="post-info">
            <p class="category">카테고리 : {{ articlestore.detailArticle.category?.name }}</p>
            
            <p class="post-title">{{ articlestore.detailArticle.title }}</p>
        </div>
        <hr>
        <p class="post-content">{{ articlestore.detailArticle.content }}</p>        
        <hr>
        

        <div class="post-dates">
            <p class="created-date">작성일 : {{ articlestore.detailArticle.created_at }}</p>
            <p class="updated-date">수정일 : {{ articlestore.detailArticle.updated_at }}</p>
        </div>
        <button @click="updateArticle" class="button">수정</button>
        <button @click="deleteArticle" class="button">삭제</button>
        <hr>
        <CommentCreate
            :articlePk="articlestore.detailArticle.id"
        />
        <ul class="comment-list">
            <CommentList 
                v-for="comment in articlestore.detailArticle.comment_set"
                :key="comment.id"
                :comment="comment"
                class="comment"
            />
        </ul>
        <hr>
    </div>
</template>

<script setup>
import CommentCreate from '@/components/CommentCreate.vue'
import CommentList from '@/components/CommentList.vue'
import { onMounted } from 'vue';
import { useRoute, useRouter } from 'vue-router';
import { useArticleStore } from '../stores/articles';

const router = useRouter()
const route = useRoute()
const articlestore = useArticleStore()
onMounted(()=> {
    articlestore.getDetailArticle(route.params.pk)
})
const updateArticle = function () {
    router.push({name:'articleupdate'})
}

const deleteArticle = function () {
    const pk = articlestore.detailArticle.id
    articlestore.deleteArticle(pk)
    router.push({name:'articles'})
}


</script>

<style scoped>
.post-details {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  background-color: #fff;
}

.post-info {
  margin-bottom: 20px;
}

.category {
  font-size: 16px;
  /* color: #333; */
}

.post-id {
  font-size: 14px;
  color: #888;
}

.post-title {
  font-size: 24px;
  font-weight: bold;
  margin-top: 10px;
  margin-bottom: 20px;
}

.post-dates {
  font-size: 12px;
  color: #888;
  margin-bottom: 10px;
}

.post-content {
  font-size: 16px;
  line-height: 1.6;
  margin-bottom: 20px;
}

.comment-list {
  list-style: none;
  padding: 5px;
}

.comment-item {
  font-size: 14px;
  margin-bottom: 10px;
}

.comment-id {
  font-weight: bold;
  margin-right: 5px;
}

.comment-content {
  margin-left: 5px;
}
.button {
  width: 50px;
  background-color: #EA6046;
  color: white;
  border-radius: 5px;
  padding: 2px;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-left: 5px;
}
.button:hover {
  background-color: #fba594;
}
.comment {
  margin-bottom: 6px;  
}
</style>