import navigation.newnav as nav
import random

Intersection = 2038506795
Prev = 97248035
# Exception:97248035


# print(nav.intersections[Intersection][Prev])
# print(nav.intersections[Prev][Intersection])

# ks = nav.thegraph.keys()
# key_list = list(ks)
# max = len(key_list)-1

# orig = key_list[random.randint(0,max)]
# end = key_list[random.randint(0,max)]
# print("orig:" + str(orig))
# print("end:" + str(end))
gpstest = nav.gps(Intersection)
gpstest.process()
ns = gpstest.getnodes(Prev)

print(ns)

# print(gpstest.path)
# # print(gpstest.path[orig])
# print(gpstest.path[end])


# try:
#     ns = gpstest.getnodes(end)
#     print(ns)
# except Exception as e:
#     print("exception:" + str(e))
#     print("lmao")

