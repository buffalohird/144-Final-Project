


def weightDistance(originalZ, otherZ, gamma=0.999):
  discount = gamma ** abs(originalZ - otherZ)
  return discount


#print weightDistance(5000.0, 4000.0) #0.367695424771
#print weightDistance(5000.0, 3000.0) #0.135199925397
#print weightDistance(5000.0, 10000.0) #0.00672111195987
