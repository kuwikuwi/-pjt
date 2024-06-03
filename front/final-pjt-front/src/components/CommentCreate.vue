<template>
    <div>
        <form @submit.prevent="createComment">
            <label for="content" class="form-label">댓글</label>
            <input type="text" name="content" id="content" v-model="content" class="form-input">
            <button class="button">작성완료</button>
        </form>
    </div>
</template>

<script setup>
import { useCommentStore } from '../stores/comments'
import { ref } from 'vue'
const commentstore = useCommentStore()
const props = defineProps({
    articlePk: Number
})
const content = ref('')
const createComment = function () {
    console.log(props)
    commentstore.commentCreate(props.articlePk, content.value)
    content.value=''
}

</script>

<style scoped>
.form-label {
  font-size: 16px;
  display: block;
  margin-bottom: 8px;
  color: white;
}

.form-input {
  width: 300px;

  font-size: 14px;
  border: 1px solid #ccc;
  border-radius: 5px;
  height: 20px;
}
.button {
  width: 80px;
  background-color: #EA6046;
  color: white;
  border-radius: 5px;
  padding: 2px;
  cursor: pointer;
  transition: background-color 0.2s;
  margin-left: 10px;
}
.button:hover {
  background-color: #fba594;
}
</style>