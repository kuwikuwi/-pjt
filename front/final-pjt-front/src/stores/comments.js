import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'
import { useArticleStore } from './articles.js'

export const useCommentStore = defineStore('comment', () => {
  const articleStore = useArticleStore()
  const commentCreate = function (pk, content) {
    axios({
      method: 'post',
      url: `http://127.0.0.1:8000/api/v1/article/${pk}/comments/`,
      data: {
        content
      }
    })
    .then(res => articleStore.detailArticle.comment_set.push(res.data))
    .catch(err => console.log(err))
  }



  const deleteComment = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/comment/${pk}/`,
      data: {
        pk
      }
    })
  }
  return { commentCreate, deleteComment }
})
