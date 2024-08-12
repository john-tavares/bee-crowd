start_time, travel_duration, time_zone_diff = map(int, input().split())

arrival_time = start_time + travel_duration + time_zone_diff

if arrival_time < 0:
    arrival_time += 24
elif arrival_time >= 24:
    arrival_time -= 24

print(arrival_time)