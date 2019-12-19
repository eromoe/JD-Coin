# encoding:utf-8

import requests
import redis

appId = "18037773"
apiKey = "opPSLkjXliSrYXfrKizsFGiC"
secretKey = "tfXgvzAcGXoasQmnoRvElWBPRsleOFbg"

###
{'refresh_token': '25.3cb47937a3d79c0552463462d73e9438.315360000.1891850261.282335-18037773', 'expires_in': 2592000, 'session_key': '9mzdCPA10u7tfQacqSQuqSRdb3SIkZjC1dtiD31DUncNIL2LofooOskV9UbjRD+sbSRBZ1bVobroRriKS4TvXgc/zKefXg==', 'access_token': '24.34f96f012fa9111074eb1867286381e3.2592000.1579082261.282335-18037773',
    'scope': 'publicvis-ocr_ocr brain_ocr_scope brain_ocr_general brain_ocr_general_basic vis-ocr_business_license brain_ocr_webimage brain_all_scope brain_ocr_idcard brain_ocr_driving_license brain_ocr_vehicle_license vis-ocr_plate_number brain_solution brain_ocr_plate_number brain_ocr_accurate brain_ocr_accurate_basic brain_ocr_receipt brain_ocr_business_license brain_solution_iocr brain_qrcode brain_ocr_handwriting brain_ocr_passport brain_ocr_vat_invoice brain_numbers brain_ocr_business_card brain_ocr_train_ticket brain_ocr_taxi_receipt vis-ocr_household_register vis-ocr_vis-classify_birth_certificate vis-ocr_台湾通行证 vis-ocr_港澳通行证 vis-ocr_机动车检验合格证识别 vis-ocr_车辆vin码识别 vis-ocr_定额发票识别 vis-ocr_保单识别 brain_ocr_vin brain_ocr_quota_invoice brain_ocr_birth_certificate brain_ocr_household_register brain_ocr_HK_Macau_pass brain_ocr_taiwan_pass brain_ocr_vehicle_certificate brain_ocr_insurance_doc wise_adapt lebo_resource_base lightservice_public hetu_basic lightcms_map_poi kaidian_kaidian ApsMisTest_Test权限 vis-classify_flower lpq_开放 cop_helloScope ApsMis_fangdi_permission smartapp_snsapi_base iop_autocar oauth_tp_app smartapp_smart_game_openapi oauth_sessionkey smartapp_swanid_verify smartapp_opensource_openapi smartapp_opensource_recapi fake_face_detect_开放Scope vis-ocr_虚拟人物助理 idl-video_虚拟人物助理', 'session_secret': 'c1960f8da6fc896c0f1807b215ef9129'}
###


def getToken():
    host = '127.0.0.1'
    port = 6379
    client = redis.Redis(host=host, port=port)
    if client.get("token") == None:
        json = requestToken()
        if client.get("refresh_token") == None:
            json = requestToken()
            client.set("token", json['access_token'],
                       None, json["expires_in"]*1000)
            client.set("refresh_token", json['access_token'],
                       None, 31536000 * 10*1000)
            return json['access_token']
    else:
        return client.get("token")


def requestToken():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + \
        apiKey+"&client_secret="+secretKey
    response = requests.get(host)
    if response:
        print(response.json())
        return response.json()