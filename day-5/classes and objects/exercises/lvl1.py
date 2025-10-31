# Python has the module called statistics and we can use this module to do all the statistical calculations. function and reuse function let us try to develop a program, 
# which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). 
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics 
# and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.



import statistics
from collections import Counter

class StatOperations:
    def __init__(self, data):
        self.data = data
    
    def count(self):
        return len(self.data)
    
    def sum(self):
        return sum(self.data)
    
    def min(self):
        return min(self.data)
    
    def max(self):
        return max(self.data)
    
    def range(self):
        return self.max() - self.min()
    
    def mean(self):
        return round(statistics.mean(self.data))
    
    def median(self):
        return statistics.median(self.data)
    
    def mode(self):
        mode_value = statistics.mode(self.data)
        mode_count = self.data.count(mode_value)
        return {'mode': mode_value, 'count': mode_count}
    
    def var(self):
        return round(statistics.variance(self.data), 1)
    
    def std(self):
        return round(statistics.stdev(self.data), 1)


# Sample data
ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]

# Create instance
data = StatOperations(ages)

# Print results
print('Count:', data.count())  # 25
print('Sum:', data.sum())  # 744
print('Min:', data.min())  # 24
print('Max:', data.max())  # 38
print('Range:', data.range())  # 14
print('Mean:', data.mean())  # 30
print('Median:', data.median())  # 29
print('Mode:', data.mode())  # {'mode': 26, 'count': 5}
print('Standard Deviation:', data.std())  # 4.2
print('Variance:', data.var())  # 17.5
