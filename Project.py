# -*- coding: utf-8 -*-
#한글주석을 위해 작성

from urllib.parse import urlencode, unquote
import requests
import json
import key



url = key.REACT_APP_API_LINK
#사용하려는 데이터가 담긴 링크 ignore처리 되었다.
queryString = "?" + urlencode(
    {
        "ServiceKey" : unquote(key.REACT_APP_API_KEY),
        "goodId" : "1182"
    }
)
#사용하려는 데이터가 담긴 링크의 세부옵션을 조정하는 곳.
#ServiceKey는 APi키값이다. ignore처리 되었음.
#goodId는 상품 한 건 조회시 사용되는 값이다.

response = requests.get(url + queryString)
print("===== response json data start =====")
print(response)
print("===== response json data end =====")
print()
#통신이 잘 되었는지 확인하는 구문.
#<Response [200]>이 출력 시 통신이 성공했다는 뜻.


r_dict = json.loads(response.text)

print(r_dict)
#데이터를 확인하는 구문.

