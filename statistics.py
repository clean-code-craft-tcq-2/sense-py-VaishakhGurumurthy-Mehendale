import math
def calculateStats(numbers):
  if(len(numbers)>0):
    avgValue = sum(numbers) / len(numbers)
    minimumValue = min(numbers)
    maximumValue = max(numbers)
    result = { 'avg':avgValue, 'min':minimumValue, 'max':maximumValue }
    return result
  else:
    return { 'avg':math.nan, 'min':math.nan, 'max':math.nan }
