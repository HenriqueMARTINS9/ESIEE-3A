import math

def volumeSphere (r):
    volume = (4*math.pi*(r**3))/3
    return volume

print(volumeSphere(int(input('entrez le rayon de la sphère : '))))