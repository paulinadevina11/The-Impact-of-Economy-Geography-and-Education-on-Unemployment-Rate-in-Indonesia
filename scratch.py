import math

n = 9

for k in range(1, n**2 + 1):
    layer_num = (n - math.sqrt(n ** 2 - k + 1)) // 2
    print(f"Target: {k} ; layer = {layer_num}")

r = math.ceil(n/2)

for layer in range(r):
    max_count = n ** 2 + 1 - (n - 2 * layer)**2
    print(f"Layer {layer} ; max_count = {max_count}")
