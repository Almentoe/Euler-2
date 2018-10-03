import numpy.polynomial.polynomial
P1 = 1
P2 = 2
P3 = 5
P4 = 10
P5 = 20
P6 = 50
P7 = 100
P8 = 200
COIN_VALUES = (P1,P2,P3,P4,P5,P6,P7,P8)
# need the number of solutions to sum pj*qj = 200
# 1 = p1
# 2 = 2*p1 or p2
# 5 = 5*p1 or 2*p2 + p1 or p3
# 10 = 5*p2 or 2*p3 or p4
#counter = 0
#for q1 in range(0,200//P1 +1):
#    for q2 in range(0,200//P2 + 1):
#        for q3 in range(0,200//P3 + 1):
#            for q4 in range(0,200//P4 + 1):
#                for q5 in range(0,200//P5 + 1):
#                    for q6 in range(0,200//P6 + 1):
#                        for q7 in range(0,200//P7 + 1):
#                            for q8 in range(0,200//P8 + 1):
#                                if q1*P1 + q2*P2 + q3*P3 + q4*P4 + q5*P5 + q6*P6 + q7*P7 + q8*P8 == 200:
#                                    counter += 1


COIN_VALUES[0]                         
# 200*200...*200
# 200*100*
# perhaps P8 rep by (0,0,0,0,0,0,0,1)
# I want the minimum number of coins needed to break a higher coin
#Hence
# P8 = 2*P7
# P7 = 2*P6
# P6 = 2*P5 + P4
# P5 = 2*P4
# P4 = 2*P3
# P3 = 2*P2 + P1
# P2 = 2*P1
def powx(n):
    return numpy.polynomial.polynomial.polypow([0,1],n)

def geosumtrunc(m,n):
    index = 0
    geosum = [0,]
    while index <= m:
        geosum = numpy.polynomial.polynomial.polyadd(geosum,powx(n*index))
        index += 1
    return geosum

def deg(Poly):
    return len(Poly)-1

def SingleCoinGeo(Value,Coin):
    assert (Value//Coin)*Coin == Value
    return geosumtrunc(Value//Coin,Coin)

def CoinGeo(Range,Deg,Value):
    Geo = [1,]
    Coin = COIN_VALUES
    index = 0
    while index < Range:
        Geo = numpy.polynomial.polynomial.polymul(Geo,SingleCoinGeo(Value,Coin[index]))
        index += 1
    return int(Geo[Deg])

print(CoinGeo(8,200,200))
        
        
        
        
        
        
    