# Load Balancer

Load Balancer for composing multi-node server of `ASKHY` application


## Build

```bash
docker build -t askhy_lb .
```


## Run
```bash
docker run -d -p 8080:80 \
  --name askhy_lb \
  askhy_lb
```


## 추가사항

현재 노드 구성에 맞게 `nginx.conf` 파일을 수정 한후 이미지를 빌드하고 컨테이너를 실행해야 합니다.

아래처럼 다수의 `askhy` 노드를 띄운 뒤 실행해야 합니다.

```bash
docker run -d \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  --name askhy1 \
  askhy

docker run -d \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  --name askhy2 \
  askhy

docker run -d \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=askhy \
  --name askhy3 \
  askhy
  ```