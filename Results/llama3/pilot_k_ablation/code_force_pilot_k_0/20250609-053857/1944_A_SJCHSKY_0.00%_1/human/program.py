qs = int(input())
 
for _ in range(qs):
  n, k = [int(num) for num in input().split()]
 
  reachable_count = n
 
  while (k >= (reachable_count - 1)) and (k > 0):
    k -= (reachable_count - 1)
    reachable_count -= 1
  
  print(reachable_count)