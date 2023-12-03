<template>
    <button class="button" @click.prevent="addCart">상품 추가</button>
    <div class="product">
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong1">은행</strong>  {{ store.depositProduct.deposit_product.kor_co_nm }}</p><hr>
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong2">상품명</strong> {{ store.depositProduct.deposit_product.fin_prdt_nm }}</p><hr>
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong3">가입 방법</strong> {{ store.depositProduct.deposit_product.join_way }}</p><hr>
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong4">만기 후 이자율</strong> {{ store.depositProduct.deposit_product.mtrt_int }}</p><hr>
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong5">우대조건</strong> <br><br>{{ store.depositProduct.deposit_product.spcl_cnd }}</p><hr>
        <p v-if="store.depositProduct && store.depositProduct.deposit_product"><strong class="strong6">기타 유의사항</strong> <br><br>{{ store.depositProduct.deposit_product.etc_note }}</p><hr>
    </div>
    <table>
        <thead>
            <tr>
                <th>저축 금리 유형</th>
                <th>저축 금리[소수점 2자리]</th>
                <th>최고 우대 금리[소수점 2자리]</th>
                <th>저축 기간[단위: 개월]</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="option in store.depositProduct.deposit_options" :key="option.deposit_options" class="card">
                <td>{{ option.intr_rate_type_nm }}</td>
                <td>{{ option.intr_rate }}</td>
                <td>{{ option.intr_rate2 }}</td>
                <td>{{ option.save_trm }}</td>
            </tr>
        </tbody>
    </table>
</template>

<script setup>
import { onMounted } from 'vue';
import { useFinlifeStore } from '@/stores/finlife'
import { useRoute, useRouter } from 'vue-router'

const store = useFinlifeStore()
const route = useRoute()

onMounted(() => {
    store.getDepositProduct(route.params.fin_prdt_cd)
})

const addCart = () => {
    alert('준비중입니다.')
}
</script>

<style scoped>
.product{
    padding-left: 20px;
}
h3, h4 {
    padding-left: 10px;
}
table {
    border-collapse: collapse;
    width: 100%;
    margin-bottom: 60px;
}

th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
    color: black;
}

th {
    background-color: #eae6e6;
    cursor: pointer;
}
.card {
    background-color: #ffffff;
    color: #000;
    cursor: pointer;
}
.button {
  width: 100px;
  background-color: #F8973F;
  color: white;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.2s;
  float: right;
  margin-top: 10px;
  padding: 3px;
}
.button:hover {
  background-color: #ffbc7e;
}
.strong1 {
    margin-right: 100px;
}
.strong2 {
    margin-right: 82px;
}
.strong3 {
    margin-right: 62px;
}
.strong4 {
    margin-right: 27px;
}
.strong5 {
    margin-right: 68px;
}
.strong6 {
    margin-right: 33px;
}
</style>
