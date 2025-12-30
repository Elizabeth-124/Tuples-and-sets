#Tuples
dimensions=(900,4000)
print(f"Width: {dimensions[0]}")
print(f"Lenght: {dimensions[1]}")

dimensions[0]=1000   #This will result in an error as tuples are immutable
print(f"Width: {dimensions[0]}")
print(f"Lenght: {dimensions[1]}")