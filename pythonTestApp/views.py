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
            'msg': "orderId必传"
        })
    elif "amount" not in data:
        return Response({
            "status_code": 400,
            'msg': "amount必传"
        })
    elif data["orderId"] == "" or data["orderId"] == " ":
        print(data)
        return Response({
            "status_code": 400,
            'msg': "orderId不能为空"
        })
    elif data["amount"] == "" or data["amount"] == " ":
        return Response({
            "status_code": 400,
            'msg': "amount不能为空"
        })
    else:
        print("走到了")
        return Response({
            "status_code": 200,
            'msg': "订单："+str(data["orderId"])+ "，创建成功"
        })


