import pandas as pd
df=pd.read_csv("laptop sales update 2.csv")

#def categorize_price(price):
 #      if 8000 <= price < 20000:
  #        return 'low'
   #    elif 20000 <= price < 45000:
    #       return 'mid'
     #  elif 45000<= price< 65000:
      #      return"high"    
       #else:
        #    return 'premium'  
#df['price_range'] = df['Total amount'].apply(categorize_price)

#df.to_csv("laptop sales update 2.csv", index = False)
most_frequent_product = df['Product'].value_counts().idxmax()
print(f"The most repeated product is: {most_frequent_product}")

