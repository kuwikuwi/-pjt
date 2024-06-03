from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.conf import settings
from rest_framework.decorators import api_view
from django.http import JsonResponse
import requests
from rest_framework.response import Response
from .models import DepositProducts, DepositOptions, SavingOptions, SavingProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer, SavingOptionsSerializer, SavingProductsSerializer
from rest_framework import status

# API_KEY = settings.API_KEY

    
@api_view(['GET'])
def save_deposit_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for baseli in response['result'].get("baseList"):
        fin_prdt_cd  = baseli.get('fin_prdt_cd')
        if not fin_prdt_cd:
            fin_prdt_cd = -1
        kor_co_nm = baseli['kor_co_nm']           
        if not kor_co_nm:
            kor_co_nm = -1
        fin_prdt_nm = baseli['fin_prdt_nm']
        if not fin_prdt_nm:
            fin_prdt_nm = -1
        etc_note = baseli['etc_note']        
        if not etc_note:
            etc_note = -1
        join_deny = baseli['join_deny']
        if not join_deny:
            join_deny = -1
        join_member = baseli['join_deny']
        if not join_deny:
            join_deny = -1
        join_way = baseli['join_way']
        if not join_way:
            join_way = -1
        spcl_cnd = baseli['spcl_cnd']
        if not spcl_cnd:
            spcl_cnd = -1
        mtrt_int = baseli['mtrt_int']
        if not mtrt_int:
            mtrt_int = -1

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
            'mtrt_int': mtrt_int,
        }
        if not DepositProducts.objects.filter(fin_prdt_cd = fin_prdt_cd).exists():
            serializer = DepositProductsSerializer(data = save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    

    for opli in response['result']['optionList']:
        fin_prdt_cd = opli['fin_prdt_cd']
        product = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)  
        intr_rate_type_nm =  opli['intr_rate_type_nm']
        intr_rate =  opli['intr_rate']
        if not intr_rate:
            intr_rate = -1
        intr_rate2 =  opli['intr_rate2']
        if not intr_rate2:
            intr_rate2 = -1
        save_trm =  opli['save_trm']
        if not save_trm:
            save_trm = -1
        
        save_data = {            
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }
        
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['product'] = product
            serializer.save()       
            
    return JsonResponse({'message': 'okay'})


@api_view(['GET'])
def save_saving_products(request):
    api_key = settings.API_KEY
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_key}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    for baseli in response['result'].get("baseList"):
        fin_prdt_cd  = baseli.get('fin_prdt_cd')
        if not fin_prdt_cd:
            fin_prdt_cd = -1
        kor_co_nm = baseli['kor_co_nm']           
        if not kor_co_nm:
            kor_co_nm = -1
        fin_prdt_nm = baseli['fin_prdt_nm']
        if not fin_prdt_nm:
            fin_prdt_nm = -1
        etc_note = baseli['etc_note']        
        if not etc_note:
            etc_note = -1
        join_deny = baseli['join_deny']
        if not join_deny:
            join_deny = -1
        join_member = baseli['join_deny']
        if not join_deny:
            join_deny = -1
        join_way = baseli['join_way']
        if not join_way:
            join_way = -1
        spcl_cnd = baseli['spcl_cnd']
        if not spcl_cnd:
            spcl_cnd = -1
        mtrt_int = baseli['mtrt_int']
        if not mtrt_int:
            mtrt_int = -1

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
            'mtrt_int': mtrt_int,
        }
        if not SavingProducts.objects.filter(fin_prdt_cd = fin_prdt_cd).exists():
            serializer = SavingProductsSerializer(data = save_data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
    

    for opli in response['result']['optionList']:
        fin_prdt_cd = opli['fin_prdt_cd']
        product = get_object_or_404(SavingProducts, fin_prdt_cd=fin_prdt_cd)  
        intr_rate_type_nm =  opli['intr_rate_type_nm']
        intr_rate =  opli['intr_rate']
        if not intr_rate:
            intr_rate = -1
        intr_rate2 =  opli['intr_rate2']
        if not intr_rate2:
            intr_rate2 = -1
        save_trm =  opli['save_trm']
        if not save_trm:
            save_trm = -1
        
        save_data = {            
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }
        
        serializer = SavingOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data['product'] = product
            serializer.save()       
            
    return JsonResponse({'message': 'okay'})
        
@api_view(['GET'])
def deposit_products(request):
    if request.method == 'GET':
        deposit_products = DepositProducts.objects.all()
        serializer = DepositProductsSerializer(deposit_products, many=True)
        print(serializer.data)
        return Response(serializer.data)


@api_view(['GET'])
def saving_products(request):
    if request.method == 'GET':
        saving_products = SavingProducts.objects.all()
        serializer = SavingProductsSerializer(saving_products, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def deposit_product_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        deposit_product = DepositProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        deposit_options = DepositOptions.objects.filter(product=deposit_product)
        product_serializer = DepositProductsSerializer(deposit_product)
        options_serializer = DepositOptionsSerializer(deposit_options, many=True)
        return Response({
            'deposit_product': product_serializer.data,
            'deposit_options': options_serializer.data,
        })


@api_view(['GET'])
def saving_product_detail(request, fin_prdt_cd):
    if request.method == 'GET':
        saving_product = SavingProducts.objects.get(fin_prdt_cd=fin_prdt_cd)
        saving_options = SavingOptions.objects.filter(product=saving_product)
        product_serializer = SavingProductsSerializer(saving_product)
        options_serializer = SavingOptionsSerializer(saving_options, many=True)
        return Response({
            'saving_product': product_serializer.data,
            'saving_options': options_serializer.data,
        })
    
