from arcus import *
from arcus_mc_node import ArcusMCNodeAllocator, EflagFilter

connection_url = '172.17.0.5:2181'
service_code = 'ruo91-cloud'
timeout = 20

client = Arcus(ArcusLocator(ArcusMCNodeAllocator(ArcusTranscoder())))

client.connect(connection_url, service_code)

ret = client.set('test:ohoohohohoh', 'test...', timeout)
print(ret.get_result())

ret = client.get('test:ohoohohohoh')
print(ret.get_result())


