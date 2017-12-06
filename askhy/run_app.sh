docker build -t askhy -f compose/askhy/Dockerfile .

docker rm -f askhy

docker run -p 8080:80 \
  --link mysql:mysql_host \
  -e DATABASE_HOST=mysql_host \
  -e DATABASE_USER=root \
  -e DATABASE_PASS=root \
  -e DATABASE_NAME=test \
  --name askhy \
  askhy
