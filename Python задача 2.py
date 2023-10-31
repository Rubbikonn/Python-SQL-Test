# Условие задачи

# 2. На прямой дороге расположено n банкоматов. 
# Было решено построить ещё k банкоматов для того, 
# чтобы уменьшить расстояние между соседними банкоматами. 
# На вход подаются натуральные числа n и k, 
# а также n-1 расстояний L, где Li – расстояние между банкоматами i и  i+1. 
# Напишите функцию, которая добавляет k банкоматов таким образом, 
# чтобы максимальное расстояние между соседними банкоматами являлось минимально возможным, и возвращает список новых расстояний между банкоматами.

# Решение:

# Тестовые переменные:
n = 5
k = 3
distances = [100, 30, 20, 80]

# Функция:

def add_atms(n, k, distances):
  
  total_atms = n + k
  total_distance = sum(distances)
  max_distance = total_distance / total_atms
  new_distances = []
  
  for distance in distances:
      new_atms = int(distance / max_distance)
      new_distance = distance / (new_atms + 1)

      for _ in range(new_atms):
          new_distances.append(new_distance)
  
      remaining_distance = distance - (new_atms * new_distance)
      new_distances.append(remaining_distance)
  
  for _ in range(k):
      new_distances.append(max_distance)
  
  return new_distances

print(add_atms(n, k, distances))