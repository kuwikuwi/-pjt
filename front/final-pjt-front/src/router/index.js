import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'

import ArticleUpdateView from '@/views/ArticleUpdateView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleView from '@/views/ArticleView.vue'
import CategoryCreateView from '@/views/CategoryCreateView.vue'


import ExchangeRateView from '@/views/ExchangeRateView.vue'

import FinanceDepositProductView from '@/views/FinanceDepositProductView.vue'
import DepositProductDetailView from '@/views/DepositProductDetailView.vue'
import FinanceSavingProductView from '@/views/FinanceSavingProductView.vue'
import SavingProductDetailView from '@/views/SavingProductDetailView.vue'

import MapView from '@/views/MapView.vue'

import LoginView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'


const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'main',
      component: MainView
    },
    {
      path: '/article/update/',
      name: 'articleupdate',
      component: ArticleUpdateView
    },
    {
      path: '/article/create',
      name: 'articlecreate',
      component: ArticleCreateView
    },
    {
      path: '/article/:pk',
      name: 'articledetail',
      component: ArticleDetailView
    },
    {
      path: '/articles',
      name: 'articles',
      component: ArticleView
    },
    {
      path: '/category',
      name: 'category',
      component: CategoryCreateView
    },
    {
      path: '/exchangerate',
      name: 'exchangerate',
      component: ExchangeRateView
    },
    {
      path: '/deposits',
      name: 'financedepositproduct',
      component: FinanceDepositProductView
    },
    {
      path: '/deposit/:fin_prdt_cd',
      name: 'financedepositproductdetail',
      component: DepositProductDetailView
    },
    {
      path: '/savings',
      name: 'financesavingproducts',
      component: FinanceSavingProductView
    },
    {
      path: '/saving/:fin_prdt_cd',
      name: 'financesavingproductdetail',
      component: SavingProductDetailView
    },
    {
      path: '/map',
      name: 'map',
      component: MapView
    },
    {
      path: '/login',
      name: 'login',
      component: LoginView
    },
    {
      path: '/signup',
      name: 'signup',
      component: SignUpView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfileView
    },
  ]
})

export default router
