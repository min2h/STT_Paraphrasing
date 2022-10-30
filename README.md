# STT_Paraphrasing
# request parameter

{
 openApiURL = "필요한 API_URL"
 accessKey = "API key값 [발급받아야함]" 
 audioFilePath = "[파일위치]"
}

# API used
![image](https://user-images.githubusercontent.com/91533318/198885605-abddf037-fde4-4a2c-a8d1-c5a906688446.png)
문장 패러프레이즈 인식 API는 두 개의 문장이 동등한 의미를 가지는지 여부를 판별하는 기술입니다.

문장 패러프레이즈 인식은 도치, 유의어, 유의 어구 등 다양한 표현 변경이 있는 두 문장 사이의 의미 동등성을 인식해 내는 것 뿐만 아니라, 주어진 두 문장 사이에 어휘 겹침이 존재하면서 서로 다른 의미를 가지도록 표현된 경우 의미 비동등성도 판별하여 그 결과를 제공합니다.

엑소브레인 패러프레이즈 인식 API는 실세계 적용을 목표로 다양한 유형의 문장 쌍에 대해 견고성을 개선하였습니다. 예를 들어, 도치형(A에서 B로 갔다. vs. B에서 A로 갔다.), 대체형(A가 O를 했다. vs. B가 O를 했다.), 부정형(A가 O를 했다. vs. A가 O를 하지 않았다.), 등 딥러닝 기술이 쉽게 틀리기 쉬운 다양한 유형의 문장 쌍에 대해 견고성을 개선하였습니다.

문장 패러프레이즈 인식 API는 HTTP 기반의 REST API 인터페이스로 JSON 포맷 기반의 입력을 지원하며 ETRI에서 제공하는 Access Key 인증을 통해 사용할 수 있는 Open API입니다.


![image](https://user-images.githubusercontent.com/91533318/198885630-8ea2f692-0fd9-40b7-8116-98e772269455.png)
최신 인공지능 기술에 기반하여 한국어, 영어, 다국어(일본어/중국어/독어/불어/스페인어/러시아어/베트남어/아랍어/태국어)에 대해 고성능의 음성인식 정확률을 제공하는 서비스로서, 사용자가 발성한 녹음된 입력 음성 데이터(단위 파일 또는 버퍼)를 음성인식 서버로 전달하여 문자(텍스트)로 제공합니다. 음성인식 API는 HTTP 기반의 REST API 인터페이스로 JSON 포맷 기반의 입력 및 출력을 지원하며 ETRI에서 제공하는 API Key 인증을 통해 사용할 수 있는 Open API 입니다.



--요청 파라미터 추가 방법--
https://www.youtube.com/watch?v=hkW4ICWSf5c

[출처] [2021 ETRI 오픈 API 활용사례 공모전] ETRI오픈API 사용해보기 / BY 한국전자통신연구원 ETRI
