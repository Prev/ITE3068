docker build -t askhy -f compose/askhy/Dockerfile .

docker rm -f askhy

docker run -p 8080:80 \
  --link mysql:mysql_host \
  --link arcus-admin:arcus_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=test \
  -e ARCUS_URL=arcus_host:2181 \
  -e ARCUS_SERVICE_CODE=ruo91-cloud \
  --name askhy \
  askhy
