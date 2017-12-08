# SW Studio 2

## 목표

네이버의 오픈소스 프로젝트인 Arcus(Memory Cache Cloud)를 사용해서 샘플 프로젝트에 구현해보고 Arcus 도입의 전/후 간의 성능을 비교해본다.

## 성능 비교를 위해

- 기본적인 응답시간 비교
	- 일반 DBMS vs. Arcus
	- 캐시된 데이터의 성능과 캐시되지 않은 일반 상황의 성능비교
		- TPS 성능비교, 캐시로 인한 DBMS 트래픽 감소정도
- NGrinder를 사용한 Stress Test
- Hubblemon을 사용한 모니터링
- 멀티노드(Scalability) 구성을 통한 성능비교


## 채점 기준별 작업 사항

* [x] 도커사용(10%)
* [x] Arcus 사용하지 않은 경우와 사용한 경우의 성능비교(20%)
* [x] nBase-ARC 사용(20%)
* [ ] 멀티노드 사용(10%)
* [ ] Hubblemon 사용(10%)
* [x] 스트레스 툴(Naver NGrinder) 사용(10%)
* [ ] 컨트리뷰션(20%)
	* [ ] 1개 10%
	* [ ] 2개 15%
	* [ ] 3개 이상 20% 부여
 

## [ASKHY](https://github.com/Prev/askhy)

성능 개선을 위해 샘플 프로젝트를 간단히 제작하였다.
[Python](https://www.python.org/) + [Flask](http://flask.pocoo.org/) + [MySQL](https://www.mysql.com/) 조합으로 개발되었으며, docker 이미지화 되어 [Docker Hub에 배포](https://hub.docker.com/r/prev/askhy/)된 상태이다.

![Screenshot](https://prev.kr/askhy/screenshot.png)


#### [ASKHY@arcus-combined](https://github.com/Prev/askhy/tree/arcus-combined)

위 ASKHY 프로젝트에 Arcus를 도입하여 성능 개선을 한 forked 프로젝트이다.

위 어플리케이션을 실행하기 전에 Arcus 컨테이너를 실행한 후, 그 정보와 함께 이 프로젝트를 실행하면 Arcus를 캐시 스토리로 써 DBMS 트래픽이 감소하고 TPS 성능이 증가한다.

Arcus 이미지는 Docker Hub에 [공개되어있는 이미지](https://hub.docker.com/r/ruo91/arcus/)를 사용하였다.


#### [ASKHY@nBase-ARC-combined](https://github.com/Prev/askhy/tree/redis-combined)

위 ASKHY 프로젝트에 nBase-ARC(redis)를 도입하여 성능 개선을 한 forked 프로젝트이다.

위 어플리케이션을 실행하기 전에 nBase-ARC 컨테이너를 실행한 후, 그 정보와 함께 이 프로젝트를 실행하면 nBase-ARC(redis)를 캐시 스토리로 써 DBMS 트래픽이 감소하고 TPS 성능이 증가한다.

nBase-ARC 이미지는 Docker Hub에 [공개되어있는 이미지](https://hub.docker.com/r/hyeongseok05/nbase-arc/)를 사용하였다.
