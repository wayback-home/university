import datetime
import json
import urllib.request
import pandas as pd

ServiceKey = "HPGTaDn%2FOaGT8JrPDJ9LlcJCALn7QpFFU4LPiv5zwIJtnwM06IijGWhSTpi7T4yLu%2BsWjiBR0ioPJ%2BuoKVdv8Q%3D%3D"


# [CODE 1]
def get_request_url(url):
    request = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(request)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


# [CODE 2]
def get_tourism_stats_item(yyyymm, national_code, ed_cd):
    service_url = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + ServiceKey  # 인증키
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + national_code
    parameters += "&ED_CD=" + ed_cd

    url = service_url + parameters
    print(url)  # 액세스 거부 여부 확인용 출력

    # [CODE 1]
    result_data = get_request_url(url)

    if result_data is None:
        return None
    else:
        return json.loads(result_data)


# [CODE 3]
def get_tourism_stats_service(nat_cd, ed_cd, start_year, end_year):
    json_result = []
    result = []
    nat_name = ""
    ed = ""
    data_end = ""

    for year in range(start_year, end_year + 1):
        for month in range(1, 13):
            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            json_data = get_tourism_stats_item(yyyymm, nat_cd, ed_cd)  # [CODE 2]

            if json_data["response"]["header"]["resultMsg"] == "OK":
                # 데이터가 없는 마지막 항목인 경우 ----------------------------
                if json_data["response"]["body"]["items"] == "":
                    data_end = "{0}{1:0>2}".format(str(year), str(month - 1))
                    print("data_end = ", data_end)
                    print(
                        "데이터 없음.... \n 제공되는 통계 데이터는 %s년 %s월까지 입니다."
                        % (str(year), str(month - 1))
                    )
                    break

                # json_data를 출력하여 확인...........................................
                print(
                    json.dumps(json_data, indent=4, sort_keys=True, ensure_ascii=False)
                )

                nat_name = json_data["response"]["body"]["items"]["item"]["natKorNm"]
                nat_name = nat_name.replace(" ", "")
                num = json_data["response"]["body"]["items"]["item"]["num"]
                ed = json_data["response"]["body"]["items"]["item"]["ed"]

                print("[ %s_%s : %s ]" % (nat_name, yyyymm, num))
                print("-----------------------------------------------------")
                json_result.append(
                    {
                        "nat_name": nat_name,
                        "nat_cd": nat_cd,
                        "yyyymm": yyyymm,
                        "visit_cnt": num,
                    }
                )

                result.append([nat_name, nat_cd, yyyymm, num])

    # TODO UnboundLocalError: local variable 'data_end' referenced before assignment 해결
    return json_result, result, nat_name, ed, data_end


# [CODE 0]
def main():
    # 요청변수(Request Parameter)
    # get 국가코드
    nat_cd = input("국가 코드를 입력하세요(중국: 112 / 일본: 130 / 미국: 275) : ")
    start_year = int(input("데이터를 몇 년부터 수집할까요? : "))
    end_year = int(input("데이터를 몇 년까지 수집할까요? : "))
    # get 출입국구분코드, E = 방한외래관광객, D = 해외 출국
    ed_cd = "E"

    # [CODE 3]
    json_result, result, nat_name, ed, data_end = get_tourism_stats_service(
        nat_cd, ed_cd, start_year, end_year
    )

    # 파일저장 1 : json 파일
    with open(
        "./%s_%s_%d_%s.json" % (nat_name, ed, start_year, data_end),
        "w",
        encoding="utf8",
    ) as outfile:
        json_file = json.dumps(
            json_result, indent=4, sort_keys=True, ensure_ascii=False
        )
        outfile.write(json_file)

    # 파일저장 2 : csv 파일
    columns = ["입국자국가", "국가코드", "입국연월", "입국자 수"]
    result_df = pd.DataFrame(result, columns=columns)
    result_df.to_csv(
        "./%s_%s_%d_%s.csv" % (nat_name, ed, start_year, data_end),
        index=False,
        encoding="utf8",
    )


if __name__ == "__main__":
    print("한국교통대학교 컴퓨터공학과 1826047 조태현")
    print("공공데이터포털, 한국문화관광연구원_출입국관광통계서비스")
    main()
