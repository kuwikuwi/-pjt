<template>
  <div class="container">
    <h1>금융상품보기</h1>
    <div>
      <label for="search">은행 검색:</label>
      <input placeholder="은행을 입력하세요" v-model="search" id="search" />
    </div>
    <h2>예금 상품</h2>
    <table>
      <thead>
        <tr>
          <th @click="sort('kor_co_nm')">은행명 ▼</th>
          <th @click="sort('fin_prdt_nm')">상품명 ▼</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="depositproduct in filteredList" :key="depositproduct.fin_prdt_cd">
          <td @click="goDetail(depositproduct.fin_prdt_cd)" class="card">
            {{ depositproduct.kor_co_nm }}
          </td>
          <td @click="goDetail(depositproduct.fin_prdt_cd)" class="card">
            {{ depositproduct.fin_prdt_nm }}
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { ref, onMounted } from 'vue';
import { useFinlifeStore } from '@/stores/finlife';
import { useRouter } from 'vue-router';
import { computed } from '@vue/reactivity';

const router = useRouter();
const store = useFinlifeStore();
const sortKey = ref(null);
const isAscending = ref(true);
const search = ref('');

onMounted(() => {
  store.getDepositList();
});

const currentList = computed(() => {
  if (sortKey.value) {
    return [...store.depositList].sort((a, b) => {
      const valueA = a[sortKey.value];
      const valueB = b[sortKey.value];
      return isAscending.value ? valueA.localeCompare(valueB) : valueB.localeCompare(valueA);
    });
  } else {
    return store.depositList;
  }
});

const filteredList = computed(() => {
  const searchTerm = search.value.toLowerCase();
  return currentList.value.filter(depositproduct =>
    depositproduct.kor_co_nm.toLowerCase().includes(searchTerm) ||
    depositproduct.fin_prdt_nm.toLowerCase().includes(searchTerm)
  );
});

const goDetail = (fin_prdt_cd) => {
  router.push({ name: 'financedepositproductdetail', params: { fin_prdt_cd: fin_prdt_cd } });
};

const sort = (key) => {
  if (sortKey.value === key) {
    isAscending.value = !isAscending.value;
  } else {
    sortKey.value = key;
    isAscending.value = true;
  }
};
</script>

<style scoped>  
  .card {
    background-color: #ffffff;
    color: #000;
    cursor: pointer;
  }
  
  .container {
    padding-bottom: 50px;
  }
  
  table {
    border-collapse: collapse;
    width: 100%;
  }
  
  th, td {
    border: 1px solid #ddd;
    padding: 8px;
    text-align: left;
  }
  
  th {
    background-color: #f2f2f2;
    cursor: pointer;
  }
</style>
