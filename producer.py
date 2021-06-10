
from kafka import KafkaProducer
import json
import uuid
import time

view = {
    "userId": str(uuid.uuid4()),
    "pageId": str(uuid.uuid4()),
    "timestamp": time.time()*1000
}

bootstrap_servers = ['localhost:9092']
pageview = 'pageview'
usercount = 'usercount'

producer = KafkaProducer(bootstrap_servers = bootstrap_servers,value_serializer=lambda v: json.dumps(v).encode('utf-8'))
page_count = dict()
users = dict()
for _ in range(0,10):
    # new page view
    pageid = page_count.get(view["pageId"],None)
    if  pageid == None:
        page_count[view["pageId"]] = 1
        producer.send(pageview,{"pageId":view["pageId"],"count":1})
    # we have an existing page view
    else:
        page_count[view["pageId"]] += 1
        producer.send(pageview,{"pageId":view["pageId"],"count":page_count[view["pageId"]]})
    
    
    userid = users.get(view["userId"],None)
    # we have a new user
    if userid == None:
        users[view["userId"]] =  {view["pageId"]:1} # nested dic a user contains many pages counts
        producer.send(usercount,{"userId":view["userId"], "pages":users[view["userId"]]})
    else:
        # we have an existing user lets add a page count to that

        #lets check if we have an existing page count
        uid = view["userId"]
        pageId = users[uid].get(view["pageId"],None)
        if pageId == None:
            # lets add a new page to the user
            users[uid][view["pageId"]] = 1
            producer.send(usercount,{"userId":uid, "pages":users[uid]})
        else:
            # we have an existing page in the user, lets increase the count
            users[uid][view["pageId"]] += 1
            producer.send(usercount,{"userId":uid, "pages":users[uid]})

    
producer.flush()