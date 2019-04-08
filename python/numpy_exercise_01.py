#
# test sub-matrix copy in ndarray data type
#
import numpy as np

inputa = np.asarray([ [0,0,0,0,0,0],
                      [1,1,1,1,1,1],
                      [2,2,2,2,2,2],
                      [3,3,3,3,3,3],
                      [4,4,4,4,4,4],
                      [5,5,5,5,5,5] ])
                      
print( inputa[1:4, 1:4] )

inputb = np.asarray([ [7,7,7],
                      [8,8,8],
                      [9,9,9] ])

inputa[1:4, 1:4] = inputb

print( inputa ) 

#
# covert a multi-dimension array into a 1D array.
#
print( inputa.flatten() )

#
# ndarray operation : accumulate, loop 
#
def profit(prices):
  max_px = 0
  min_px = prices[0]

  for px in prices[1:]:
    min_px = min(min_px, px)
    max_px = max(px - min_px, max_px)

  return max_px

prices = (20, 18, 14, 17, 20, 21, 15)
print( profit( prices ) )

cummin = np.minimum.accumulate

def profit_with_numpy(prices):
  """Price minus cumulative minimum price, element-wise."""
  prices = np.asarray(prices)
  return np.max(prices - cummin(prices))

print( profit_with_numpy( prices ) )

print( profit_with_numpy( [[20, 18, 14, 17], [20, 21, 15, 15] ] ) )

print( np.asarray( (20, 18, 14, 17, 20, 21, 15, 15) ) )

print("accumulate ")
print( np.maximum.accumulate( np.asarray( [20, 18, 14, 17, 20, 21, 15, 15]  ) ) )

print( (20, 18, 14, 17, 20, 21, 15, 15)  - np.minimum.accumulate( np.asarray( (20, 18, 14, 17, 20, 21, 15, 15) ) ) ) 

#
# numpy's interp() function.
# One-dimensional linear interpolation
#
prices = np.full(100, fill_value=np.nan)
prices[[0, 25, 60, -1]] = [80., 30., 75., 50.]

print( prices )

x = np.arange(len(prices))

print( "x = ", x)
print( x )
is_valid = ~np.isnan(prices)
print( is_valid )

pricesA = np.interp(x=x, xp=x[is_valid], fp=prices[is_valid])
print( pricesA )

print( "x[is_valid] = ", x[is_valid])
print( "prices[is_valid] = ", prices[is_valid])

pricesB = np.random.randn(len(prices)) *2 + pricesA
print( "pricesB = ", pricesB)
