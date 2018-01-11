from django.shortcuts import render,redirect
from django.http import HttpResponse
from booktest.models import Goods, GoodsBrands, GoodsCates


def brands(request):
    """图书列表"""
    brands = GoodsBrands.objects.all()
    context = {'brands': brands}
    return render(request, 'booktest/brands.html', context)


def brand_goods(request, bid):
    """根据品牌名获取商品"""
    goods = Goods.objects.filter(brand_id=bid)
    context = {'goods': goods}
    return render(request, 'booktest/b_goods.html', context)


def cates(request):
    cates = GoodsCates.objects.all()
    context = {'cates': cates}
    return render(request, 'booktest/cates.html', context)


def c_goods(request, cid):
    goods = Goods.objects.filter(cate_id=cid)
    context = {'goods': goods}
    return render(request, 'booktest/c_goods.html', context)


def goods(request):
    goods = Goods.objects.all()
    # good = Goods.objects.get(id=1)
    # brand = GoodsBrands.objects.filter(id=good.brand_id)
    # print(brand[0].name)
    # cate = GoodsCates.objects.get(id=good.cate_id)
    # print(cate.name)
    goods_list = []
    for good in goods:
        brand = GoodsBrands.objects.get(id=good.brand_id)
        cate = GoodsCates.objects.get(id=good.cate_id)
        good_list = [brand,cate, good]
        goods_list.append(good_list)
    context = {"goods_list": goods_list}
    return render(request, 'booktest/goods.html', context)