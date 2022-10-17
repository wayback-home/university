import urllib.request
import datetime
import json

client_id = "11"
client_secret = "11"


def main():
    node = "news"  # 크롤링 대상
    srcText = input("검색어 입력 ")
    cnt = 0
    jsonResult = []

    jsonResponse = getNaverSearch(node, srcText, 1, 100)
    total = jsonResponse["total"]

    while (jsonResponse != None) and (jsonResponse["display"] != 0):
        for post in jsonResponse["items"]:
            cnt += 1
            getPostData(post, jsonResult, cnt)

        start = jsonResponse["start"] + jsonResponse["display"]
        jsonResponse = getNaverSearch(node, srcText, start, 100)

    print("전체 검색 %d 건" % total)

    with open("%s_naver_%s.json" % (srcText, node), "w", encoding="utf8") as outfile:
        jsonFile = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

        outfile.write(jsonFile)

    print("가져온 데이터  %d 건" % (cnt))
    print("%s_naver_%s.json SAVED" % (srcText, node))


def getNaverSearch(node, srcText, start, display):
    base = httpopenapi.naver.comv1search
    node = "%s.json" % node
    parameters = "?query = %s&start = %s&display = %s" % (
        urllib.parse.quote(srcText),
        start,
        display,
    )

    url = base + node + parameters
    responseDecode = getRequestUrl(url)

    if responseDecode == None:
        return None
    else:
        return json.loads(responseDecode)


# urllib.parse.quote()


def getRequestUrl(url):
    req = urllib.request.Request(url)
    req.add_header(X - Naver - Client - Id, "_gJra_F38hGKFUClmgh3")
    req.add_header(X - Naver - Client - Secret, "8wTUNbdKRV")

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode("utf-8")
    except Exception as e:
        print(e)
        print("[%s] Error for URL" % s % (datetime.datetime.now(), url))
        return None


# urllib.request와 requests는 거의 동일한 기능을 수행.
# requests가 조금 더 고수준의 라이브러리.


def getPostData(post, jsonResult, cnt):
    title = post["title"]
    description = post["description"]
    org_link = post["originallink"]
    link = post["link"]

    # 네이버에서 제공하는 시간 (pubDate) 그리니치 평균시이며 문자열 형태
    # 연-월-일 시분초’ 형식으로 변경 필요

    pDate = datetime.datetime.strptime(post["pubDate"], "%a, %d %b %Y %H%M%S + 0900")
    pDate = pDate.strftime("%Y-%m-%d" % H % M % S)

    jsonResult.append(
        {
            "cnt": cnt,
            "title": title,
            "description": description,
            "org_link": org_link,
            "link": org_link,
            "pDate": pDate,
        }
    )
    return


if __name__ == "__main__":
    main()
