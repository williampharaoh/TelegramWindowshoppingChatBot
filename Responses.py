
from datetime import datetime
from itertools import product
import requests

r = requests.get('https://windowshoppingserver.herokuapp.com/product/All')
print(r)
data1 = r.json()

def allshops():
    base_url = 'https://windowshoppingserver.herokuapp.com/shop/All'
    shop = requests.get(base_url).json()
    sho = 'name  phonenumber   location\n\n\n'

    for s in shop:
        sho =sho+ f'{s["shopName"]} {s[phoneNumber]} {s["location"]} \n'

    return sho

def dataStr():
    base_url = 'https://windowshoppingserver.herokuapp.com/product/All'
    data = requests.get(base_url).json()
    # print(data)
    dat = 'name     price       description     quantity        Shop\n\n'

    for product in data:
        dat =dat+ f'{product["Name"]}       {product["Price"]}        {product["Description"]}      {product["Quantity"]}        {product["Shop"]}\n'
        print(dat)

    return dat

mother=[]
for X in data1:
    pname=X['Name']
    mother.append(pname)


basics=["hello","hie","hy","sup","who","help","groceries"]

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if  user_message in basics:
        if user_message in ("hello","hie","hy","sup"):
            return str("""Hi there ! am window shopping bot. How may I help you? \n\n1. To find out about the shops available reply to this massege with 'shop' \n\n2. To find out about the product you want  reply to this massege with 'NAME OF PRODUCT'""")
        
        if "who" in user_message:
            return str('   I am being  created by Edward Ali and william Pharaoh ')
        
        if "help" in user_message:

            return str('help Line \n 1.Search for the product by typing the NAME of product \n 2.Type GROCERIES to get all the latest available products \n 3.Type HELP to go to the help line menu')
        
        if "groceries" in user_message:
            return (dataStr())

    if 'shop' in user_message:
        return (allshops())
     

    
    # filter user input
   
        
    if user_message not in basics:
        filtered_arr=[]
        splitText=user_message.split()
        for X in splitText:
        # r = requests.get('https://windowshoppingserver.herokuapp.com/product/All')
            if X in mother:
                filtered_arr.extend([p for p in data1 if p['Name'] ==X])
        #data1 = r.json()
        if filtered_arr:
            print("filtered array is")
            print(filtered_arr)
            #sortedByPrice=filtered_arr.sort(key=lambda x: x["Quantity"], reverse=True)
            sortedByPrice=sorted(filtered_arr, key=lambda x: x['Price'], reverse=False)
            print("sorrted by price in ascending order")
            print(sortedByPrice)
            lowestThree=sortedByPrice[:3]
            print("lowest 3")
            print(lowestThree)

           
            
            #base_url = 'https://windowshoppingserver.herokuapp.com/product/All'
            firstThree = lowestThree
            # Printing firstThree
            datr = 'name     price       description     quantity        Shop\n\n'

            for product in firstThree:
                datr =datr+ f'{product["Name"]}       {product["Price"]}        {product["Description"]}      {product["Quantity"]}        {product["Shop"]}\n'
            
            return str(datr)


        if not filtered_arr:
             return str("Sorry, I didn't get what you have said! You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n")
   
       
       

    else:
        return str("Sorry, I didn't get what you have said! You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product ")



    
    
    
   

    

    
    if user_message in ("time", "time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    


      

    