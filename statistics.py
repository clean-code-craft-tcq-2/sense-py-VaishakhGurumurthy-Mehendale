
def calculateStats(numbers):
  if(len(numbers)>0):
    avgValue = sum(numbers) / len(numbers)
    minimumValue = min(numbers)
    maximumValue = max(numbers)
    result = { 'avg':avgValue, 'min':minimumValue, 'max':maximumValue }
    return result
  else:
    return { 'avg':float("nan"), 'min':float("nan"), 'max':float("nan") }
