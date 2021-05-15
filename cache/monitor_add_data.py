import requests
import json
import random
from datetime import datetime
import time
API_URL = 'http://127.0.0.1:8000/monitor/add_data/'


def add_data(device_id, indicator_id, value):
    data = {
        'device_id':device_id,
        'indicator_id': indicator_id,
        'value': value,
    }
    create_time = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S')
    print('{} 新增数据：设备id-{}，指标id-{}，监测值-{}'.format(create_time, device_id, indicator_id, value))
    r = requests.post(API_URL, data=data)
    rj = json.loads(r.text)
    print(rj)


def generator():
    device_id, indicator_id = 3, 1
    value = random.uniform(20.1, 25.4)
    add_data(device_id, indicator_id, value)


if __name__ == '__main__':
    while True:
        generator()
        time.sleep(10)