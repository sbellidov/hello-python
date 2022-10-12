# Exercises - Day 21

# Exercises: Level 1
# 1 - Python has the module called statistics and we can use this module to do all the statistical calculations.
# However, to learn how to make function and reuse function let us try to develop a program, which calculates
# the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation).
# In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample.
# You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class.
# Check the output below.
# ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
 
# print('Count:', data.count()) # 25
# print('Sum: ', data.sum()) # 744
# print('Min: ', data.min()) # 24
# print('Max: ', data.max()) # 38
# print('Range: ', data.range() # 14
# print('Mean: ', data.mean()) # 30
# print('Median: ', data.median()) # 29
# print('Mode: ', data.mode()) # {'mode': 26, 'count': 5}
# print('Standard Deviation: ', data.std()) # 4.2
# print('Variance: ', data.var()) # 17.5
# print('Frequency Distribution: ', data.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

# # you output should look like this
# print(data.describe())
# Count: 25
# Sum:  744
# Min:  24
# Max:  38
# Range:  14
# Mean:  30
# Median:  29
# Mode:  (26, 5)
# Variance:  17.5
# Standard Deviation:  4.2
# Frequency Distribution: [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]

class Statistics():
    def __init__(self, list):
        self.list = list
    
    def count(self):
        return len(self.list)
    
    def sum(self):
        return sum(self.list)
    
    def min(self):
        return min(self.list)
    
    def max(self):
        return max(self.list)
    
    def range(self):
        return max(self.list) - min(self.list)
    
    def mean(self):
        return round(sum(self.list) / len(self.list),1)
    
    def median(self):
        self.list.sort()
        return self.list[len(self.list)//2]
    
    def mode(self):
        unique_values = set(self.list)
        freq = dict.fromkeys(unique_values,0)
        mode_max_value = 0
        for element in self.list:
            freq[element] += 1
            if freq[element] > mode_max_value:
                mode_max_value = freq[element]
                mode = { 'mode': element, 'count': mode_max_value}
        return mode
    
    def std(self):
        return round(self.var()**0.5, 1)
    
    def var(self):
        numerador = []
        for item in self.list:
            numerador.append((item - self.mean())**2)
        return round( sum(numerador) / self.count() , 1 )
    
    def freq_dist(self):
        freq = []
        unique_values = set(self.list)
        for element in unique_values:
            freq.append((self.list.count(element)/self.count()*100,element))
        freq.sort(key=lambda x: x[0], reverse=True) # Ordenación de una tupla , descendente (reverse=True), por el primer elemento (key=lambda x: x[0])
        return freq



ages = Statistics([31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26])
print('Count:', ages.count()) # 25
print('Sum: ', ages.sum()) # 744
print('Min: ', ages.min()) # 24
print('Max: ', ages.max()) # 38
print('Range: ', ages.range()) # 14
print('Mean: ', ages.mean()) # 30
print('Median: ', ages.median()) # 29
print('Mode: ', ages.mode()) # {'mode': 26, 'count': 5}
print('Standard Deviation: ', ages.std()) # 4.2
print('Variance: ', ages.var()) # 17.5
print('Frequency Distribution: ', ages.freq_dist()) # [(20.0, 26), (16.0, 27), (12.0, 32), (8.0, 37), (8.0, 34), (8.0, 33), (8.0, 31), (8.0, 24), (4.0, 38), (4.0, 29), (4.0, 25)]


# Exercises: Level 2
# 1 - Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties and it has total_income,
# total_expense, account_info, add_income, add_expense and account_balance methods. Incomes is a set of incomes and its description.
# The same goes for expenses.

class PersonAccount:
    def __init__(self, firstname = 'Unknown', lastname = 'Unknown', incomes = [], expenses = []):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses
    
    def total_income(self):
        return sum(item['amount'] for item in self.incomes)
    
    def total_expense(self):
        return sum(item['amount'] for item in self.expenses)
    
    def account_info(self):
        print('\nExtracto de cuenta:')
        for item in self.incomes:
            print(f"INGRESO | {item['amount']}€ | {item['description']}")
        for item in self.expenses:
            print(f"GASTO   | {-item['amount']}€ | {item['description']}")
            
    
    def add_income(self , amount , description):
        self.incomes.append({'amount':amount , 'description': description})
    
    def add_expense(self , amount , description):
        self.expenses.append({'amount':amount , 'description': description})
    
    def account_balance(self):
        return self.total_income() - self.total_expense()

persona1 = PersonAccount(
    'Sergio',
    'Bellido',
    [
        {'amount':1500 , 'description': 'Salario'},
        {'amount':100 , 'description': 'Intereses'},
        {'amount':350 , 'description': 'Regalos'}
        ],
    [
        {'amount':490 , 'description': 'Hipoteca'},
        {'amount':125 , 'description': 'Comunidad'},
        {'amount':350 , 'description': 'Comida'},
        {'amount':650 , 'description': 'Gastos Varios'}
        ],
)

print(f'\n*********************************')
print(f'{persona1.firstname} {persona1.lastname}')
print(f'Total Ingresos: {persona1.total_income()} €')
print(f'Total Gastos: {persona1.total_expense()} €')
print(f'Balance: {persona1.account_balance()} €')
persona1.account_info()
print(f'\n*********************************')

persona1.add_income(750,'Trabajo secundario')
persona1.add_expense(45,'Seguro de salud')

print(f'\n*********************************')
print(f'{persona1.firstname} {persona1.lastname}')
print(f'Total Ingresos: {persona1.total_income()} €')
print(f'Total Gastos: {persona1.total_expense()} €')
print(f'Balance: {persona1.account_balance()} €')
persona1.account_info()
print(f'\n*********************************')


persona2 = PersonAccount()
print(f'\n*********************************')
print(f'{persona2.firstname} {persona2.lastname}')
print(f'Total Ingresos: {persona2.total_income()} €')
print(f'Total Gastos: {persona2.total_expense()} €')
print(f'Balance: {persona2.account_balance()} €')
persona2.account_info()
print(f'\n*********************************')
