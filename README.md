# LOBSTER CSV

The function is usefull if you want to use the CSV files from the [LOBSTER website](https://lobsterdata.com/). The original files do not have any label for the columns, this function labels the dataframe using Pandas. The message file is straing foward to label, the order book it can be problematic because we have different CSV files to choose from depending on the order book depth (level 10,50 and so on). The function can take care of that automatically.

## Arguments

+ format_time: bool
  The format_time (defalult=False) if True adds a new column with time in HH:MM:SS.000000 format.
+ format_price: bool
  The format_price (defalult=False) if True shows all the prices in the "normal" format. For example if a Bid price is $ 95.43 the LOBSTER file shows 9543000, with format_price=True the price becomes a numpy.float64 95.43.

---

Message type:

Columns names: 'Time', 'Type', 'Order_ID', 'Size', 'Price', 'Direction'

![1707174637953](image/README/1707174637953.png)

---

Order Book type:

'Ask_Price_1',  'Ask_Size_1', 'Bid_Price_1',  'Bid_Size_1'

+ How the CSV Order Book file is presented originally![1707174082570](image/README/1707174082570.png)
+ How the CSV Order Book file is presented after the function

  ![1707174149861](image/README/1707174149861.png)

---

Contact me for any issue.
