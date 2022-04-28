import collections
from . import Expense
import matplotlib.pyplot as plt

# read the expenses data
expenses = Expense.Expenses()
expenses.read_expenses('data/spending_data.csv')

# get all spending categories 
spending_categories = []
for expense in expenses.list:
    spending_categories.append(expense.category)

# count categories using Counter Collection
spending_counter = collections.Counter(spending_categories)
# print(spending_counter)
top5 = spending_counter.most_common(5)
# gets top most common values[most common is a collections.Counter function]


categories, count = zip(*top5)
# zip creates lists of keys and list of values

# Plot the top 5 most common categories
fig,ax = plt.subplots()

#  creating the bar chart
ax.bar(categories,count)
ax.set_title('# of Purchases by Category')# sets the title

# display the graph
plt.show()




