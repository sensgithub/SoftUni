record_seconds = float(input())
distance = float(input())

time_sec_one_meter = float(input())
total_time = distance * time_sec_one_meter

delay = distance // 15 * 12.5
total_time = total_time + delay

if total_time < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
else:
    diff = total_time - record_seconds
    print(f"No, he failed! He was {diff:.2f} seconds slower.")
    