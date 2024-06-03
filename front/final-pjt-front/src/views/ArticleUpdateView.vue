<template>
  <div>
    <h1>게시글 수정</h1>
    <form @submit.prevent="updateArticle" class="article-form">
      <label for="category" class="form-label">카테고리 선택</label>
      <select name="category" id="category" v-model="category" class="select">
        <option
        v-for="category in categoryStore.categoryList"
        :key="category.id"
        :value="category.id"
        >
        {{ category.name }}
        </option>
      </select>
<br>
      <label for="title" class="form-label">제목</label>
      <input type="text" name="title" v-model="title" class="form-input">
      <br>
      <label for="content" class="form-label">내용</label>
      <textarea name="content" id="content" cols="30" rows="10" v-model="content" class="form-input"></textarea>
<br>
      <button class="submit-button">게시글 수정</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useCategoryStore } from '@/stores/categories'
import { useArticleStore } from '@/stores/articles'
import { onMounted } from 'vue';
import { useRouter } from 'vue-router';

const router = useRouter()
const articleStore = useArticleStore()


const title = ref(articleStore.detailArticle.title)
const content = ref(articleStore.detailArticle.content)
const category = ref(articleStore.detailArticle.category.id)
const categoryStore = useCategoryStore()
onMounted(() => {
  categoryStore.getCategoryList()
})


const updateArticle = function () {
  const article = {
    title: title.value,
    content: content.value,
    category: category.value,
    pk: articleStore.detailArticle.id
  }
  // console.log(post)
  articleStore.updateArticle(article)
  router.push({name: 'articledetail', params: {pk: article.pk}})
}
</script>

<style scoped>
.article-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  background-color: #fff;
  border: 1px solid #ccc;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}
.select {
  width: 400px;
  height: 40px;
  background-size: 35px;
  padding: 5px 30px 5px 10px;
  border-radius: 5px;
  outline: 0 none;

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