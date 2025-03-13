import math
import random

# Rastgele noktaların tanımlanması
num_points = 6
points = [(random.randint(0, 10), random.randint(0, 10)) for _ in range(num_points)]
print("Rastgele noktalar:", points)

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

# Mesafeleri hesaplamak için bir liste oluşturma
distances = []

# Her nokta çifti arasındaki mesafeyi hesaplama
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum mesafeyi bulma
min_distance = min(distances)

# Sonucu yazdırma
print("Minimum Öklid mesafesi:", min_distance)
