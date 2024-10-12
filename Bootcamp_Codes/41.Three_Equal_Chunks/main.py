# Three Equal Chunks
# Given a list slice it into Three Equal Chunks and reverse each chunk.

# sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
# Output
# Chunk-1 = [18, 55, 21]
# Chunk-2 = [22, 24, 33]
# Chunk-3 = [79, 35, 68]

sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]

#slice the list into 3 equal lists
list_1 = sample_list[0:3]
list_2 = sample_list[3:6]
list_3 = sample_list[6:]

#reverse the lists
list_1 = list_1[-1::-1]
list_2 = list_2[-1::-1]
list_3 = list_3[-1::-1]

#print the output 
print(f"Chunk-1 = {list_1}")
print(f"Chunk-2 = {list_2}")
print(f"Chunk-3 = {list_3}")