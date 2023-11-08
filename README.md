## Twitch-Roulette-Assistant
[스트리머 전용]
트위치 10연차 뽑기와 기본 뽑기의
csv파일을 분류하는 코드입니다.

뽑은 사람의 ID가 결과의 시트 이름으로 나오게 되며
[ID] - [닉네임] - [뽑기 결과] - [개수]
형태로 시트가 구성되어 있습니다.

update 2.0
+ csv파일을 여러개 선택할 수 있도록 만들어졌습니다.
+ multiprocessing을 통해 하나씩 처리하던 것을 동시에 처리할 수 있도록 수정했습니다.

update 2.1
+ multiprocessing bug fix
