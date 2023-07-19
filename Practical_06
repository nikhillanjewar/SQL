import pandas as pd 
import matplotlib.pyplot as plt  
dataBase = pd.read_csv("sales.csv")
x_axis = dataBase['month_number'].to_list()
y_axis = dataBase['total_profit'].to_list()

# Displaying the monthly profit and month using the line chart 
plt.plot(x_axis,y_axis,label="Overall Profit")
plt.legend()
plt.show()
table_schema = list(dataBase.columns)
product_list = list(dataBase.columns[1:len(table_schema)-2])
months = dataBase['month_number'].to_list();
# Adjenceny  List 
product_sales = list()
for product in product_list : 
    product_sales.append({product : dataBase[product].to_list()})
index = 0
for index in range(0,len(product_sales)) : 
    for key in product_sales[index] : 
        # print(f"{key} : {product_sales[index][key]}")
        plt.plot(x_axis,product_sales[index][key],label=f"{key}")
        plt.legend()
        index +=1 
plt.show()
# Comparison of sales between the facewash and facecream using bar-chart 
sales_of_facewash = sum(dataBase['facewash'].to_list())
sales_of_facecream = sum(dataBase['facecream'].to_list())
plt.bar("FaceWash",sales_of_facewash,label="FaceWash")
plt.bar("FaceCream",sales_of_facecream,label="FaceCream")
plt.legend()
plt.show()
# Sales of each product in 12 Months 
each_product_sales = [sum(dataBase[product_name].to_list()) for product_name in product_list]
plt.pie(each_product_sales,labels=product_list)
plt.legend(title="Yealy Sales")
plt.show()
