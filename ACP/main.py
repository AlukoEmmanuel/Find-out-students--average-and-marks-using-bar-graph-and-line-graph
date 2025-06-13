import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FuncFormatter

# Step 1: Create the DataFrame directly
data = pd.DataFrame({
    'month_number': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
    'facecream': [2500, 2630, 2140, 3400, 3600, 2760, 2980, 3700, 3540, 1990, 2340, 2900],
    'facewash': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'toothpaste': [5200, 5100, 4550, 5870, 4560, 4890, 4780, 5860, 6100, 8300, 7300, 7400],
    'bathingsoap': [9200, 6100, 9550, 8870, 7760, 7490, 8980, 9960, 8100, 10300, 13300, 14400],
    'shampoo': [1200, 2100, 3550, 1870, 1560, 1890, 1780, 2860, 2100, 2300, 2400, 1800],
    'moisturizer': [1500, 1200, 1340, 1130, 1740, 1555, 1120, 1400, 1780, 1890, 2100, 1760],
    'total_units': [21100, 18330, 22470, 22270, 20960, 20140, 29550, 36140, 23400, 26670, 41280, 30020],
    'total_profit': [211000, 183300, 224700, 222700, 209600, 201400, 295500, 361400, 234000, 266700, 412800, 300200]
})

# Debug: Inspect the DataFrame
print(data.head())
print(data.columns)
print(data.dtypes)

# Step 2: Line plot for profit
plt.figure(figsize=(10, 6))
plt.plot(data['month_number'], data['total_profit'], linestyle=':', marker='o', 
         color='red', markeredgecolor='black', markerfacecolor='black', linewidth=3)
plt.xlabel('Month')
plt.ylabel('Profit ($)')
plt.title('Monthly Profit')
plt.xticks(data['month_number'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.gca().yaxis.set_major_formatter(FuncFormatter(lambda x, _: f'{int(x/1000)}K'))
plt.grid(True)
plt.savefig('profit_plot.png')
plt.show()

# Step 3: Multi-line plot for all products
plt.figure(figsize=(10, 6))
products = ['facecream', 'facewash', 'toothpaste', 'bathingsoap', 'shampoo', 'moisturizer']
for product in products:
    plt.plot(data['month_number'], data[product], marker='o', linewidth=3, label=product, alpha=0.7)
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.title('Monthly Sales of All Products')
plt.xticks(data['month_number'], ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                  'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend(loc='upper left', bbox_to_anchor=(1, 1))
plt.grid(True)
plt.savefig('all_products_plot.png')
plt.show()

# Step 4: Bar plot for facecream and facewash
plt.figure(figsize=(10, 6))
x = np.arange(len(data['month_number']))
width = 0.35
plt.bar(x - width/2, data['facecream'], width, label='Face Cream')
plt.bar(x + width/2, data['facewash'], width, label='Face Wash')
plt.xlabel('Month')
plt.ylabel('Sales (Units)')
plt.title('Face Cream vs. Face Wash Sales')
plt.xticks(x, ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
plt.legend()
plt.grid(True, axis='y')
for i, v in enumerate(data['facecream']):
    plt.text(i - width/2, v + 50, str(v), ha='center')
for i, v in enumerate(data['facewash']):
    plt.text(i + width/2, v + 50, str(v), ha='center')
plt.savefig('facecream_facewash_plot.png')
plt.show()