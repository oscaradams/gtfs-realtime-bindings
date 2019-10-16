from google.transit import gtfs_realtime_pb2
import requests
import urllib3

feed = gtfs_realtime_pb2.FeedMessage()
selec_me = gtfs_realtime_pb2.TripUpdate()
trip_data = []

response = requests.get('http://datamine.mta.info/mta_esi.php?key=947398dd95ea59047e146305639c7048')
feed.ParseFromString(response.content)
for entity in feed.entity:
  if entity.HasField('trip_update'):
	trip_data.append(entity.trip_update)

i = 0
xy = len(trip_data) - 1
xyz = []
while i < xy:
	i = i + 1
	if trip_data[i].stop_time_update[0].stop_id == "901N":
		xyz.append(trip_data[i].stop_time_update[0])
print xyz
