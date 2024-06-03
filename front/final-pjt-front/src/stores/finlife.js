import axios from 'axios'
import { ref } from 'vue'
import { defineStore } from 'pinia'

export const useFinlifeStore = defineStore('finlife', () => {
    const depositList = ref([])
    const getDepositList = function () {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/finlife/deposit-products/'
        })
        .then(res => depositList.value = res.data)
        .catch(err => console.log(err))
    }

    const depositProduct = ref([])
    const getDepositProduct = function (fin_prdt_cd) {
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/finlife/deposit-product-detail/${fin_prdt_cd}`,
        })
        .then((res) => {
            depositProduct.value = res.data
            console.log(res.data)
        })
        .catch(err => console.log(err))
    }

    const savingList = ref([])
    const getSavingList = function () {
        axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/finlife/saving-products/'
        })
        .then(res => savingList.value = res.data)
        .catch(err => console.log(err))
    }


    
    const savingProduct = ref([])
    const getSavingProduct = function (fin_prdt_cd) {
        axios({
            method: 'get',
            url: `http://127.0.0.1:8000/finlife/saving-product-detail/${fin_prdt_cd}`,
        })
        .then((res) => {
            savingProduct.value = res.data
            console.log(res.data)
        })
        .catch(err => console.log(err))
    }
    

    return { depositList, savingList, depositProduct, savingProduct, getDepositList, getDepositProduct, getSavingList, getSavingProduct }
})