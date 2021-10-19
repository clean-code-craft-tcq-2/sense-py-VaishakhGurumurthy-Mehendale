
def calculateStats(numbers):
  avgValue = sum(numbers) / len(numbers)
  minimumValue = min(numbers)
  maximumValue = max(numbers)
  result = { 'avg':avgValue, 'min':minimumValue, 'max':maximumValue }
  return result
