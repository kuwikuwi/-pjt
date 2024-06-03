from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.conf import settings
# Create your models here.

class DepositProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)  
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note  = models.TextField()
    join_deny  = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
    join_way  = models.TextField()
    spcl_cnd  = models.TextField()
    mtrt_int = models.TextField()
    
    
class DepositOptions(models.Model):
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()


class SavingProducts(models.Model):
    fin_prdt_cd = models.TextField(unique=True)
    kor_co_nm = models.TextField()
    fin_prdt_nm = models.TextField()
    etc_note  = models.TextField()
    join_deny  = models.IntegerField(validators=[MinValueValidator(1),MaxValueValidator(3)])
    join_way  = models.TextField()
    spcl_cnd  = models.TextField()  
    mtrt_int = models.TextField()


class SavingOptions(models.Model):
    product = models.ForeignKey(SavingProducts, on_delete=models.CASCADE)
    fin_prdt_cd = models.TextField()
    intr_rate_type_nm = models.CharField(max_length=100)
    intr_rate = models.FloatField()
    intr_rate2 = models.FloatField()
    save_trm = models.IntegerField()

