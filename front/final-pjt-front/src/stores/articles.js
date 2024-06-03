import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'


export const useArticleStore = defineStore('post', () => {
  const articleList = ref([])
  const getArticleList = function () {
    axios({
      method: 'get',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
    })
    .then(res => articleList.value = res.data)
    .catch(err => console.log(err))
  }
  const detailArticle = ref([])
  const getDetailArticle = function (pk) {
    axios({
      method: 'get',
      url: `http://127.0.0.1:8000/api/v1/article/${pk}`,
    })
    .then(res => detailArticle.value = res.data)
    .catch(err => console.log(err))
  }

  const createArticle = function ({category, title, content}) {
    axios({
      method: 'post',
      url: 'http://127.0.0.1:8000/api/v1/articles/',
      data: {
        category,
        title,
        content
      },
    })    
  }

  const updateArticle = function ({category, title, content, pk}) {
    axios({
      method: 'put',
      url: `http://127.0.0.1:8000/api/v1/article/${pk}/`,
      data: {
        category,
        title,
        content,
      },
    })
    .then((res) => {
      getDetailArticle(pk)
    })
  }

  const deleteArticle = function (pk) {
    axios({
      method: 'delete',
      url: `http://127.0.0.1:8000/api/v1/article/${pk}/`,
      data: {
        pk
      },
    })
    .then(res => {
      getArticleList()
    })
  }

  
  return { articleList, getArticleList, detailArticle, getDetailArticle, createArticle, updateArticle, deleteArticle }
})
