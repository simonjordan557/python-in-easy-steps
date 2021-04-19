zoo = ( "Kangaroo", "Leopard", "Moose" )
print("Tuple:", zoo, "\tLength:", len(zoo))
print(type(zoo))

bag = { "Red", "Green", "Blue" }
print("Set:", bag, "\tLength:", len(bag))
print(type(bag))

print("\nIs Green In bag Set?", "Green" in bag)
print("Is Orange In bag Set?", "Orange" in bag)

box = { "Red", "Purple", "yellow" }
print("\nSet:", box, "\tLength:", len(box))
print("Common To Both Sets:", bag.intersection(box))
