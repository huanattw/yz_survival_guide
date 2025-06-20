import requests
import time

def log(msg, mode=0):
    temp = "{} {} ".format(time.strftime(
        "[%Y-%m-%d %H:%M:%S]", time.localtime()), msg)
    print(temp)

if  __name__ == "__main__":
    token =""
    while 1==1 :
        try:
            url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_rc"
            payload = 'sel_flag=54&token={}'.format(token)
            headers = {
            'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CKxPortal=2569308812.47873.0000; TS01e1254b=01d03ec66933af81db36c5271119b1857c29df44f739c53f93b64d686a32e7dcd5682477602d87c0331960872b40ccd3cf0662c29e529b6d94f0332e310815d9670cb3de21'
            }

            response = requests.request("POST", url, headers=headers, data=payload)

            r = response.json()
            if r[0]['StaffCode'] != 'A':
                log("return Error Staff Code")
                continue

            url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_BACK_DOOR"

            payload = 'sel_flag=54&token={}'.format(token)
            headers = {
            'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CKxPortal=2552531596.47873.0000; TS01e1254b=01d03ec6698e8d6d1341380ad6d4f9e6a7fb16e60888b36a1a0554ea719cbb409f8146bbb750f3579f04c40000c7bcaa49df8e41f1c8648cbd086bd085f86359ba2f5552ff'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if (response.text != 'N'):
                log("return Error-GET_BACK_DOOR_54")
                continue


            url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_RC_STR"
            payload = 'sel_flag=93&token={}'.format(token)
            headers = {
            'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CKxPortal=2552531596.47873.0000; TS01e1254b=01d03ec6698e8d6d1341380ad6d4f9e6a7fb16e60888b36a1a0554ea719cbb409f8146bbb750f3579f04c40000c7bcaa49df8e41f1c8648cbd086bd085f86359ba2f5552ff'
            }
            response = requests.request("POST", url, headers=headers, data=payload)

            url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_rc"

            payload = 'sel_flag=51&token={}'.format(token)
            headers = {
            'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'CKxPortal=2552531596.47873.0000; TS01e1254b=01d03ec6698e8d6d1341380ad6d4f9e6a7fb16e60888b36a1a0554ea719cbb409f8146bbb750f3579f04c40000c7bcaa49df8e41f1c8648cbd086bd085f86359ba2f5552ff'
            }

            response = requests.request("POST", url, headers=headers, data=payload)
            if len(response.json()) <= 0:
                log("Cannt find item")
                continue
            guid = response.json()[0]['guid']

            if guid is not None:
                log("\nFind course: {}\nguid: {}".format(response.json()[0]['cos_name'], guid),1)
                url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_BACK_DOOR"

                payload = 'sel_flag=54&token={}'.format(token)
                headers = {
                'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'CKxPortal=2552531596.47873.0000; TS01e1254b=01d03ec669db5d9f99451cd9dbf0ac991d159cebea3588a8b7039424784440b397db3c93665a7e35f3d934b519ddaf11b2cc2344ed4e1a15d92f5add4abc3ef386f0991bd4'
                }

                response = requests.request("POST", url, headers=headers, data=payload)

                url = "https://portalfun.yzu.edu.tw/AcademicWebAPI/api//rollcall/get_rc"

                buildings = [[],[24.97041818933712, 121.26650992041856],[24.969319396439428, 121.26814304782492],[24.969351203740178, 121.26692777137603],[],[24.97004807072018, 121.26823873888391],[24.97072469297397, 121.26755295296132],[24.968676019033104, 121.26676608918812]]
                building_no = 1
                lat = buildings[building_no][0]
                lng = buildings[building_no][1]
                payload = 'sel_flag=52&token={}&std_no=&guid={}1&gps_long={}&gps_lat={}&gps_acc=75&roll_call_datetime=&device_type=ios&ShowLang=zh'.format(token, guid,lng,lat)
                headers = {
                'User-Agent': 'XamPrismYzu.iOS/23.05.0803 CFNetwork/1410.1 Darwin/22.6.0',
                'Content-Type': 'application/x-www-form-urlencoded',
                'Cookie': 'CKxPortal=2552531596.47873.0000; TS01e1254b=01d03ec6696d44db398608e9878ecbd28c05a91a7de73c15d4e0dee7c75fe174c6046ce2be8a1cf392d2f6d8486b5d0ed59c9201a31ed3e6e17ef2e95dffdc1b612a248bf4'
                }
                response = requests.request("POST", url, headers=headers, data=payload)
                obj = response.json()[0]
                log("\nresult: {}\nreason:{}".format(obj['check_flag'],obj['check_reason']),1)
        
            else:
                log("No GUID Found")
        except Exception as e:
            log("Found Error: {}".format(e.args[0]), 1)
        finally:
          time.sleep(30)
