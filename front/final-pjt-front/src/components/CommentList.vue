<template>
    <div>
        <span>{{ comment.content }}</span>
        <button @click="deleteComment" class="button">삭제</button>
    </div>
</template>

<script setup>
import { useArticleStore } from '@/stores/articles'
import { useCommentStore } from '../stores/comments';
import { useRouter } from 'vue-router';

const router = useRouter()
const articlestore = useArticleStore()
const commentstore = useCommentStore()

const props = defineProps({
    comment: Object
})

const deleteComment = function () {
    commentstore.deleteComment(props.comment.id)
    router.go(0)
}


</script>

<style scoped>
.button {
  width: 50px;
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