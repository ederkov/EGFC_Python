nums = []
for i in range(3):
    nums.append(float(input(f"Número {i+1}: ")))
nums.sort(reverse=True)
print("Ordenados:", nums)
