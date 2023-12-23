## Twitch-Roulette-Assistant
[스트리머 전용]  
트위치
투네이션  
10연차 뽑기와 기본 뽑기의  
csv파일을 분류하는 코드입니다.  

### 결과물 구성 요소
[뽑은 사람의 ID] 시트 이름으로 나오게 되며  
[ID] - [닉네임] - [뽑기 결과] - [개수]  
형태로 시트가 구성되어 있습니다.  

update 2.1  
+ multiprocessing bug fix  
   
update 2.0  
+ csv파일을 여러개 선택할 수 있도록 만들어졌습니다.  
+ multiprocessing을 통해 하나씩 처리하던 것을 동시에 처리할 수 있도록 수정했습니다.  

### module - csv_processor 구성
작동 순서  
1. file_selector.py
선택한 파일(csv)의 위치들을 받아옵니다.  

2. data_processor.py
csv파일에서 우리가 이용할 수 있을 정도로 정형화 시킵니다.  
ex) ' Message'열의 글자인 "뽑기 후원 -"을 지우며  
(,)단위로 구분되어있는 10연속 뽑기를 분리하고 ' Message'열에 추가합니다.  
마지막으로 count_messages()로 ' 계정 ID'와 ' Name', ' Message'가 같은 것을 세어줍니다.
' Name'은 후원자가 설정한 이름이라 계정 ID가 같아도 ' Name'은 따로 표기됩니다.
(이러한 이유로 엑셀파일시트는 계정 ID 단위로 분류됩니다.)
  
3. excel_generator.py
엑셀파일을 생성하고 작업을 완료합니다.  
  
4. logger.py
main.py에서 로그 기능을 추가시킵니다.
