from arcus import *
from arcus_mc_node import ArcusMCNodeAllocator, EflagFilter

import os

connection_url = os.environ.get('ARCUS_URL')
service_code = os.environ.get('ARCUS_SERVICE_CODE')
timeout = 20

client = Arcus(ArcusLocator(ArcusMCNodeAllocator(ArcusTranscoder())))

client.connect(connection_url, service_code)

testmsg = "My Test Message"

ret = client.set('test:ohoohohohoh', testmsg, timeout)
print(ret.get_result())

ret = client.get('test:ohoohohohoh')
print(ret.get_result())


assert testmsg == ret.get_result()