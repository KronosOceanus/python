import json,requests

API_KEY = 'daCzP95uMgbEbsxiYGB3rrj9sEdy56RR'

def getGeo(ip):
    '''根据 ip 得到经纬度
        要查询地点的 ip'''
    quiry = \
        'http://api.map.baidu.com/location/ip' \
        '?ak=daCzP95uMgbEbsxiYGB3rrj9sEdy56RR' \
        '&ip={}' \
        '&coor=bd09ll'.format(ip)
    response = requests.get(quiry)
    j = json.loads(response.text)
    return j.get('content').get('point').values()

def getTimezone(location, coord_type, timestamp, ak):
    '''根据经纬度查询时区信息
        location 经纬度
        coord_type 坐标系类型	bd09ll，gcj02ll，wgs84ll，bd09mc
        timestamp unix 时间戳
        ak API_KEY'''
    quiry = \
        "http://api.map.baidu.com/timezone/v1" \
        "?coord_type={}" \
        "&location={}" \
        "&timestamp={}" \
        "&ak={}".format(coord_type, location, timestamp, ak)
    response = requests.get(quiry)
    j = json.loads(response.text)
    return j.get('timezone_id')


locationList = list(getGeo("218.26.154.68"))
location = locationList[1] + ','  + locationList[0]
timezone = getTimezone(location, 'wgs84ll', '1473130354', API_KEY)
print(timezone)