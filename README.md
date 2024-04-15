Crawl은 사이트 주소를 입력받아 해당 사이트의 stim map을 검색합니다. 
이후 접속 가능한 사이트 목록을 수집 모든 사이트의 스크린샷을 저장합니다.
이를 통해 RAG 시스템에 입력할 정보 파일을 생성합니다.

streamlit에서는 RAG 시스템을 웹으로 구현했습니다.
OPENAI KEY가 필요하며 ChatOpenAI 모델을 사용했습니다.

![image](https://github.com/parks602/RAG_langchain_steramlit/assets/34082230/6d50b1e4-ee3c-4b24-a255-772d0817837f)

다음과 같은 UI를 가지고 있습니다.
OPEINAI KEY와 RAG 시스템에 입력할 파일을 업로드합니다.
이후 RAG 시스템 생성 후 질문해보세요.
