# coveragePythonTest
## 使用方式
1.在项目根目录下（manage.py所在目录）
输入 coverage  erase  清楚原来的覆盖率数据

2.启动项目，在项目根目录下
输入 python manage.py runserver 0.0.0.0:8000

3.调用接口
url=127.0.0.1:8000/create/
body={
    "orderId":1,
    "amount":2
}

4.在项目根目录下， CONTROL+C关闭项目进程，收集覆盖率

5.产出覆盖率报告
输入 coverage combine（合并报告）coverage report（查看报告）coverage html（产出html报告）