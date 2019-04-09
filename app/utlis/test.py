import time

from app.utlis.alplay import AliPay

import requests

import json


def ali():
    app_id = "2016092500594458"
    # POST请求，用于最后的检测(检测是否支付成功，生成订单)
    notify_url = "http://127.0.0.1:5000/"
    # GET请求，用于页面的跳转展示（获取订单状态，显示给用户）
    return_url = "http://127.0.0.1:5000/"
    # 用户的私钥
    merchant_private_key_path = "/home/wang/code/python/web/OpenHi/app/utlis/app_private_key.pem"
    # 支付宝的公钥
    alipay_public_key_path = "/home/wang/code/python/web/OpenHi/app/utlis/aa.text"

    ali = AliPay(appid=app_id,
                 app_notify_url=notify_url,
                 return_url=return_url,
                 app_private_key_path=merchant_private_key_path,
                 alipay_public_key_path=alipay_public_key_path,  # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥
                 debug=True)  # 默认False
    return ali


if __name__ == '__main__':
    alipay = ali()
    # 生成支付的url
    query_params = alipay.direct_pay(
        subject="给老婆转账",  # 商品简单描述
        out_trade_no="x2" + str(time.time()),  # 商户订单号
        total_amount=100.00,  # 交易金额(单位: 元 保留俩位小数)
    )

    zz_params = alipay.zz_play(
        out_trade_no="2x" + str(time.time()).split(".")[0],
        payee_account="kmptca5402@sandbox.com",
        amount=50000,
        payee_real_name="沙箱环境"
    )

    # 支付宝网关,带上订单参数才有意义
    pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(query_params)
    # pay_url = "https://openapi.alipaydev.com/gateway.do?{}".format(zz_params)
    print(pay_url)

    # respeons = requests.get(pay_url)
    #
    # print(json.loads(respeons.content))
