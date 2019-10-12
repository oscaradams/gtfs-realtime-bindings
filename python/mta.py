from google.transit import gtfs_realtime_pb2
import requests

feed = gtfs_realtime_pb2.FeedMessage()
response = requests.get('http://datamine.mta.info/mta_esi.php?key=947398dd95ea59047e146305639c7048')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
    print entity.trip_update
