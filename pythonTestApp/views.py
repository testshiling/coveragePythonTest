from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.

@api_view(http_method_names=['POST'])
def createOrder(request):
    data = json.loads(request.body)
    if "orderId" not in data:
        return Response({
            "status_code": 400,
            'msg': "orderId"
        })
    elif "amount" not in data:
        return Response({
            "status_code": 400,
            'msg': "amount"
        })
    elif data["orderId"] == "" or data["orderId"] == " ":
        print(data)
        return Response({
            "status_code": 400,
            'msg': "orderId"
        })
    elif data["amount"] == "" or data["amount"] == " ":
        return Response({
            "status_code": 400,
            'msg': "amount"
        })
    else:
        print("走到了")
        return Response({
            "status_code": 200,
            'msg': "订单："+str(data["orderId"])+ "，创建成功"
        })


