k = int(input())
room_numbers = list(map(int, input().split()))

groups = len(room_numbers) // k

gr_rooms = set(room_numbers)

for i in gr_rooms:
    room_numbers.remove(i)

captain_room = gr_rooms.symmetric_difference(room_numbers)
for x in captain_room:
    print(x)
