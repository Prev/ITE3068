## 조별 과제

네이버의 오픈소스 프로젝트인 Naver의 OSS(Open Source Software)인 Arcus(Memory Cache Cloud)를 사용해서 샘플 프로젝트에 구현해보고 Arcus 도입의 전/후 간의 성능을 비교해본다.

#### 성능 비교를 위해
- 기본적인 응답시간 비교
	- 일반 DBMS vs. Arcus
	- 캐시된 데이터의 성능과 캐시되지 않은 일반 상황의 성능비교
		- TPS 성능비교, 캐시로 인한 DBMS 트래픽 감소정도
- NGrinder를 사용한 Stress Test
- Hubblemon을 사용한 모니터링
- 멀티노드(Scalability) 구성을 통한 성능비교


## 채점 기준
- 도커사용(10%)
- Arcus 사용하지 않은 경우와 사용한 경우의 성능비교(20%)
- nBase-ARC 사용(20%)
- 멀티노드 사용(10%)
- Hubblemon 사용(10%)
- 스트레스 툴(Naver NGrinder) 사용(10%)
- 컨트리뷰션(20%)
	- 1개10%, 2개 15%, 3개 이상 20% 부여
 