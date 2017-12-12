## Run Controller (official)

```bash
docker run -d \
  -v ~/ngrinder-controller:/opt/ngrinder-controller \
  -p 8000:80 \
  -p 16001:16001 \
  -p 12000-12009:12000-12009 \
  --name ngrinder_ctrl \
  ngrinder/controller:3.4
```



## Run Agent (official)

```bash
docker run -d \
  -v ~/ngrinder-agent:/opt/ngrinder-agent \
  --name ngrinder_agent \
  ngrinder/agent:3.4 \
  <controller_ip>:<controller_web_port>
```