import urllib.request
from bs4 import BeautifulSoup as bs4


# TODO : 범죄도시
for page in range(1, 2880, 1):
    url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=161242&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}"

# TODO : 범죄도시2
# for page in range(1,2741,1):
#     url = f"https://movie.naver.com/movie/bi/mi/pointWriteFormList.naver?code=192608&type=after&isActualPointWriteExecute=false&isMileageSubscriptionAlready=false&isMileageSubscriptionReject=false&page={page}"
