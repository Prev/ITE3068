# 1. 프로젝트 목표

## 1.1 전체적 목표
 네이버의 오픈소스 프로젝트인 Arcus(Memory Cache Cloud)를 사용해서 샘플 프로젝트에 구현해보고 Arcus 도입의 전/후 간의 성능을 비교해본다. 이때 Docker를 사용해서 서버를 구성해보고 NGrinder를 사용해서 스트레스 테스트를 진행한다. 또한 Arcus와 유사한 캐싱 오픈소스인 nBase-ARC를 사용해보거나 멀티노드를 구성해서 성능 비교를 해본다.

## 1.2. 단계별 세부목표 및 작업 내역
* [x] 도커사용
* [x] Arcus 사용하지 않은 경우와 사용한 경우의 성능비교
* [x] nBase-ARC 사용
* [x] 멀티노드 사용
* [ ] Hubblemon 사용
* [x] 스트레스 툴(Naver NGrinder) 사용

## 1.3. 다운로드 방법

```bash
git clone https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6
cd single6
git submodule init
git submodule update
```

<br>

# 2. 아키텍처
## 2.1. 도커 이미지
모든 서비스는 도커 상에서 실행되며 일부 이미지는 직접 개발하였고, 일부 이미지는 공개되어있는 모듈을 사용하였다.



| 이미지                                                                                    | 이미지 주소                                    | 설명                                                         | 비고             |
|----------------------------------------------------------|--------------------------------|--------------------------------------|------------|
| [ASKHY (샘플 프로젝트)](#31-askhy-웹-어플리케이션)            | prev/askhy                                | MySQL을 사용하는 기본 웹 어플리케이션      | 직접개발       |
| [ASKHY@arcus-combined](#32-askhyarcus-combined)    | prev/askhy:arcus-combined   | `ASKHY`에 `arcus`로 성능 개선을 한 버전  | 직접개발       |
| [ASKHY@redis-combined](#33-askhyredis-combined)    | prev/askhy:redis-combined     |`ASKHY`에 `nBase-ARC`로 성능 개선을 한 버전   | 직접개발       |
| [MySQL](#35-mysql)                                                          | mysql:3.6                                 | RDBMS                                                   | 오픈소스 사용 |
| [NGrinder-Controller](#36-ngrinder)                                    | ngrinder/controller                   | 부하 테스트용 서비스                                | 오픈소스 사용 |
| NGrinder-Agent                                                                    |  ngrinder/agent                        | 부하 테스트 에이전트                                | 오픈소스 사용 |
| [Arcus Admin](#37-arcus)                                                 | ruo91/arcus                              | Cache storage `arcus` 관리자             | 오픈소스 사용 |
| Arcus Node (memcached)                                               |  ruo91/arcus:memcached        |  Cache storage `arcus` 노드                | 오픈소스 사용 |
| [nBase-ARC](#38-nbase-arc)                                       | hyeongseok05/nbase-arc       |  Cache storage nBase-ARC 노드         | 오픈소스 사용 |


<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/4e0fbc257a3ed18d0c5cc7d557687278/image.png" width="600">

*로컬에서 실행되고 있는 컨테이너들*

<br>
<br>

---

## 2.2. 서버 아키텍처
### A. 기본 아키텍처

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/66af4b1c21f7c43cf8e58f848084cfe1/image.png" width="500">

*기본적인 노드로만 구성한 서버 아키텍처*

### B. Arcus 사용시의 아키텍처

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/071a8366788cdb50dc49a181520aba10/image.png" width="700">

*Arcus를 함께 넣어 구성한 서버 아키텍처*


### C. nBase-ARC 사용시의 아키텍처
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/23d1f0b32b2930d375b5f59f4992651f/image.png" width="700">

*nBase-ARC를 함께 넣어 구성한 서버 아키텍처*


### C. 멀티노드 구성시의 아키텍처
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/c97e99b1afa99dbac088c0333819b426/SW_Studio2__4_.png" width="700">

*멀티노드로 웹 어플리케이션을 구성한 서버 아키텍처*


<br>

# 3. 프로젝트 및 이미지
## 3.1. ASKHY: 웹 어플리케이션
`Flask`로 직접 만든 간단한 **웹 어플리케이션**으로, `Nginx` 및 `UWSGI`와 함께 작동하며 `MySQL` 컨테이너와 통신한다.

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/3fb9fafe421ed746dd08c36742f1dff9/image.png" width="700">

*웹 어플리케이션인 "부탁하냥"의 화면*

<br>

또한 이 어플리케이션에 대해 `Dockerfile`을 작성하여 이미지화 시켰으며 **Docker Hub**에도 해당 이미지를 업로드 해둔 상태이다. (https://hub.docker.com/r/prev/askhy/)

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/e9680d757b084371c0631f0c6c4e89af/dockerhub.png" width="700">

*Docker Hub에 올라간 ASKHY 어플리케이션*


서비스 컨셉은 기본적인 게시판과 비슷하지만 게시글을 `부탁`이라는 이름으로 쓰며, 댓글을 `응원`이라는 이름을 붙여서 개발하였다.

위 어플리케이션에 대한 MySQL 스키마는 아래와 같다.

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/474e0bf26ae899c195a3f90cac40d05b/SW_Studio2__5_.png" width="500">

이 모델을 바탕으로 성능 테스트를 위해 메인 화면에서 수행 시간이 꽤 걸리는 데이터를 받도록  했다. 메인 화면에서 요구하는 데이터는 다음과 같다.

- 부탁(`ask`) 고유 ID
- 부탁 메시지
- 부탁 등록 시간
- 부탁 별 응원(`cheer`) 수
- 부탁 별 순수 응원 수: IP 하나 당 중복되는 응원을 제거하여, 순수하게 몇 명이 해당 부탁에 응원을 했는지를 보여주는 숫자

이를 쿼리로 표현하면 다음과 같다.

```sql
SELECT
	*,
	(SELECT COUNT(*) FROM `cheer` WHERE ask_id = ask.id) AS cheer_cnt,
	(SELECT COUNT(DISTINCT ip_address) FROM `cheer` WHERE ask_id = ask.id) AS cheer_cnt_pure
FROM `ask`
```

위 쿼리를 5개의 “부탁”과 약 7만개의 “응원” 데이터에 대해 실행한 결과 약 0.1초가 걸림을 확인할 수 있었다.

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/5afa0d1418406fe63cd4fa943a02bba9/image.png" width="400">

*7만개 행에 대한 쿼리 수행 시간*


어플리케이션은 아래 명령어로 실행할 수 있다. (`MySQL` 컨테이너가 먼저 띄워져 있어야 함)


```bash
$ docker run -p 8080:80 \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  --name askhy \
  prev/askhy
```

<br>

위 코드는 https://github.com/Prev/askhy/tree/1.1 에서 확인할 수 있다.


## 3.2. ASKHY@arcus-combined
위 웹 어플리케이션에 `arcus`를 이용하여 성능 개선을 시킨 버전이다.  Branch를 통해 관리 중에 있다. 

내부적으로는 `naver/arcus-python-client`를 사용해서 arcus서버와 통신하며, docker 실행 시 arcus서버와 관련된 환경변수를 입력 받도록 설계되어있다.

```bash
$ docker run -p 8080:80 \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  -e ARCUS_URL=172.17.0.4:2181 \
  -e ARCUS_SERVICE_CODE=ruo91-cloud \
  --name askhy \
  askhy
```

*askhy@arcus-combined 이미지의 실행 방법*

캐시는 `부탁 별 응원 수`와  `부탁 별 순수 응원 수`를 저장하는 방식으로 개발하였다.  
성능 부하가 발생하는 가장 큰 요인이 위 두개 요소이기 때문에, 기본적인 데이터는 `MySQL`에서 요청해서 가져오며 위 두개의 컬럼에 대해서만 캐시를 이용한다.

전체 프로세스는 다음과 같다.

1. `ask` 테이블에 대해서만 쿼리 조회
2. `ask`.`id`를 바탕으로 캐시에서 `cheer_count`와 `pure_cheer_count` 조회
3. 있다면 캐시를 사용하고 6으로 이동
4. 없다면 `ask`와 `cheer`을 중첩으로 조회하는 무거운 쿼리 재 조회
5.`MySQL`에서 받아온 데이터를 다시 캐시에 저장
6. `HTML` 렌더링

위 코드는 https://github.com/Prev/askhy/tree/1.1-arcus-combined 에서 확인할 수 있다.

## 3.3. ASKHY@redis-combined
위 웹 어플리케이션에 `nBase-ARC(redis)`를 이용하여 성능 개선을 시킨 버전이다.  3.2와 마찬가지로 Branch를 통해 관리 중에 있다.

내부적으로는 `redis python client`를 사용해서 nBase-ARC서버와 통신하며(redis와 호환성을 가지기 때문), docker 실행 시 nBase-ARC서버와 관련된 환경변수를 입력 받도록 설계되어있다.

```bash
$ docker run -p 8080:80 \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  -e REDIS_HOST=172.17.0.9 \
  -e REDIS_PORT=6000 \
  --name askhy \
  askhy
```
*askhy@redis-combined 이미지의 실행 방법*

성능 개선 로직은 `3.2 ASKHY@arcus-combined`와 완전히 동일하며, 위 코드는 https://github.com/Prev/askhy/tree/1.1-redis-combined 에서 확인할 수 있다.

## 3.4. ASKHY Load Balancer
위 웹 어플리케이션을 멀티노드로 구성하기 위해 `nginx` 를 이용하여 간단하게 `Load Balancer`를 만들고 도커와 함께 서버 구성을 진행하였다.

```bash
upstream askhyapp {
	server 172.17.0.3;
	server 172.17.0.4;
	server 172.17.0.5;
}
server {
	listen 80;
	location / {
		proxy_pass http://askhyapp;
	}
}
```
*Load Balancer의 nginx conf 파일*


실행하기 위해서는 먼저 다수의 `ASKHY` 컨테이너를 띄운 뒤 `nginx.conf`를 알맞게 수정하고 다음 명령어를 수행하면 된다.
```bash
$ docker build -t askhy_lb .

$ docker run -d -p 8080:80 \
  --name askhy_lb \
  askhy_lb
```

## 3.5 MySQL

Docker Hub의 공식 이미지를 사용하였다. 아래 명령어를 통해 실행한다.

```bash
$ docker run -d \
  -e MYSQL_ROOT_PASSWORD=root \
  -e MYSQL_DATABASE=askhy \
  --name mysql \
  mysql:5.7
```

## 3.6 NGrinder

Docker Hub의 공식 이미지를 사용하였다. 아래 명령어를 통해 실행한다.

```bash
$ docker run -d \
  -v ~/ngrinder-controller:/opt/ngrinder-controller \
  -p 8000:80 \
  -p 16001:16001 \
  -p 12000-12009:12000-12009 \
  --name ngrinder_ctrl \
  ngrinder/controller:3.4
```

```bash
$ docker run -d \
  -v ~/ngrinder-agent:/opt/ngrinder-agent \
  --name ngrinder_agent \
  ngrinder/agent:3.4 \
  <controller_ip>:<controller_web_port>
```

## 3.7 Arcus

Dockerhub에 올라온 오픈소스를 활용하였다. 총 3개의 노드와 1개의 어드민을 띄웠으며 아래 명령어를 통해 실행하였다. (환경에 따라 추가 설정을 해주어야 한다)

```bash
$ docker run -d --name="arcus-admin" -h "arcus" arcus-admin
$ docker run -d --name="arcus-memcached-1" -h "memcached-1" arcus-memcached
$ docker run -d --name="arcus-memcached-2" -h "memcached-2" arcus-memcached
$ docker run -d --name="arcus-memcached-3" -h "memcached-3" arcus-memcached
```

## 3.8 nBase-ARC

Dockerhub에 올라온 오픈소스를 활용하였다. 아래 명령어를 통해 실행한다.

```bash
$ docker run -p 6000:6000 -d --name=nbasearc hyeongseok05/nbase-arc
```


<br>

# 4. 성능 비교
MySQL만 사용한 버전(1), MySQL과 Arcus를 사용한 버전(2), MySQL과 nBase-ARC를 사용한 버전(3), MySQL만 사용하지만 서버 어플리케이션을 멀티노드로 구성한 버전(4)으로 각각 성능 테스트를 진행하였다. 성능 측정 시에는 약 4만개의 데이터를 넣어두고 뷰에 대한 측정만 진행하였다.

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/dc2ac1674f823131363783979838612e/그림1.png" width="700">

TPS (Transaction Per Second)의 경우 약 4~5배 차이가 남을 확인할 수 있었고, MTT (Mean Test Time)의 경우에도 마찬가지로 약 4~5배 차이가 남을 확인할 수 있었다.

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/2cf805f4925a8c2d13100cdb25cb61c5/그림2.png" width="700">


<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/ed4a4d7d6ef9d12409a152d2cf061c05/image.png" width="700">

*NGrinder에서의 Stress Test*


### A. Cache Storage 미사용시
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/cb7ca279b468088585f32b524c0d210a/image.png" width="700">


### B. Arcus 사용시
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/a64ad84a0667cf008ad785eaad540eb4/image.png" width="700">


### C. nBase-ARC 사용시
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/72b3b8ecc43e7923760729e8b1a3f157/image.png" width="700">


### D. 멀티노드 어플리케이션 구성 + Cache Storage 미사용시
<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/a4cb2d6231a6c72aa90645b9b3cf4bf3/image.png" width="700">

<br>

# 5. 오픈소스 기여

`ASKHY`이라는 샘플 프로젝트를 만들게 된 계기는 `MySQL`을 사용하고 수행시간이 꽤 오래 걸리면서 `Docker`화 하기 좋은 프로젝트를 찾기 힘들었기 때문이다. 때문에 이번 프로젝트에 적합한 간단한 웹 어플리케이션을 만들고 **오픈소스**화 하게 되었다.


이 프로젝트는 [Github](https://github.com/Prev/askhy)과 [Docker Hub](https://hub.docker.com/r/prev/askhy/)를 통해 공개했는데, 기존 백엔드 경험이 없던 많은 학생들이 해당 프로젝트를 분석하고 직접 개선을 하여 성능 개선을 한 경우가 많다고 알고 있다.

![ASKHY Github](https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/dab54a6faa1c070b9479a3122d5e4a8f/github.png)

현재 이 프로젝트는 13개의 Star와 7개의 Fork를 받은 상태인데, 내 코드를 통해 다른 사람들에게 일종의 길잡이를 해주며 조금 다른 방법으로 오픈소스에 기여했다고 생각하고 있다.


<br>

# 6. 결론

Docker를 이용하여 단일 환경에서 다양한 라이브러리들을 활용하며 마치 노드가 여러 개인 것처럼 서버를 구성할 수 있었다. 또한 네이버의 다양한 오픈소스를 활용해보며 네이버는 어떤 식으로 자신들의 서버를 관리하는지, 자신들이 만든 소프트웨어를 공개할 때에는 어떤 방식으로 관리를 하는지도 알 수 있었다.

뿐만 아니라 느린 SQL을 사용할 때 cache storage를 사용하면 상당한 성능 개선을 시킬 수 있음을 직접 확인할 수 있었지만, 반대로 결과에 대한 확실한 보장을 위해서는 concurrent에 대한 고려를 해주어야 하여 마냥 쉽지만은 않음을 알 수 있었다.

또한 프로젝트는 git을 최대한 활용하여 GitLab의 Issue Board를 통해서 할 작업을 관리하였고, Submodule System과 branch 통해 프로젝트를 체계적으로 관리하였다.

![image](https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/a9e8028008e5a0b64b907814cca35686/image.png)
*GitLab의 Issue Board*

<img src="https://hconnect.hanyang.ac.kr/SW_studio2_2017/single6/uploads/119edb55e679181d7f20edcf86733403/structure.png" width="300">

*서브모듈로 관리되고 있는 프로젝트*
