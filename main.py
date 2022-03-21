import math 
import Charging
all_station = []
all_geo = []
m = Charging.map()
origin = "成功大學"  #input("請輸入出發點")
end = "交通大學"  #input("請輸入目的地")
fillpertimes = 50
start,final = m.Latitude_longitude(origin, end)
start_final_length = gmaps.distance_matrix(start,final , mode='driving')["rows"][0]["elements"][0]["distance"]["value"]/1000
min_times = math.ceil(start_final_length/fillpertimes)
min_km = start_final_length/(min_times+2)
near,location = m.nearby(start,min_km)

a = gmaps.places_nearby(page_token = location['next_page_token'])
for i in range(20):
      if a['results'][i]['geometry']['location']['lng']< start['lng']:
         near.append(a['results'][i]['geometry']['location'])
x ,y= m.dis_sta(near,start,final,fillpertimes,min_km)
min, geo= m.dis(x,y,start,final)
all_station.append(min)
all_geo.append(geo)

geo,min

start = geo
fillpertimes = 50
arrive = m.isarrive(start,final,fillpertimes)
if arrive == 0:
  min_km = start_final_length/(min_times+2)
  near,location = m.nearby(start,min_km)
else:
  print('已經抵達')

a = gmaps.places_nearby(page_token = location['next_page_token'])
for i in range(20):
      if a['results'][i]['geometry']['location']['lat'] > start['lat']:
         near.append(a['results'][i]['geometry']['location'])
x ,y= m.dis_sta(near,start,final,fillpertimes,min_km)
min, geo= m.dis(x,y,start,final)
all_station.append(min)
all_geo.append(geo)

geo,min


start = geo
fillpertimes = 50
arrive = m.isarrive(start,final,fillpertimes)
if arrive == 0:
  min_km = start_final_length/(min_times+2)
  near,location = m.nearby(start,min_km)
else:
  print('已經抵達')

start

a = gmaps.places_nearby(page_token = location['next_page_token'])
for i in range(20):
      if a['results'][i]['geometry']['location']['lat'] > start['lat']:
         near.append(a['results'][i]['geometry']['location'])
x ,y= m.dis_sta(near,start,final,fillpertimes,min_km)
min, geo= m.dis(x,y,start,final)
all_station.append(min)
all_geo.append(geo)
