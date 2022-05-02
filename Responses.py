
from itertools import product
import requests

#getting all products from the api

r = requests.get('https://windowshoppingserver.herokuapp.com/product/All')
print(r)
data1 = r.json()

#function for getting all the shops
def allshops():
    base_url = 'https://windowshoppingserver.herokuapp.com/shop/All'
    shop = requests.get(base_url).json()
    sho = 'Name    phoneNumber    Location\n\n\n'

    for s in shop:
        sho =sho+ f'{s["shopName"]}    {s["phoneNumber"]}    {s["location"]} \n'

    return sho

def dataStr():
    base_url = 'https://windowshoppingserver.herokuapp.com/product/All'
    data = requests.get(base_url).json()
    # print(data)
    dat = 'name     price       description     quantity        Shop\n\n'
    
    #structuring products in table format
    for product in data:
        dat =dat+ f'{product["Name"]}       {product["Price"]}        {product["Description"]}      {product["Quantity"]}        {product["Shop"]}\n'
        print(dat)

    return dat

#An array for appending products
mother=[]
for X in data1:
    pname=X['Name']
    mother.append(pname)

#An array for appending  shops
shopMother =[]
for Y in data1:
    shopName=Y['Shop']
    shopMother.append(shopName)

#An array for defined user messages
basics=["hello","hie","hy","sup","who","help","groceries"]

#function getting user message and giving responses in the chatbot
def sample_responses(input_text):
    # get the message from the user 
    user_message = str(input_text).lower()

    #Checking whether user message is in  the basics array
    if  user_message in basics:
        if user_message in ("hello","hie","hy","sup"):
            return str("""Hi there ! am window shopping bot. How may I help you? \n You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n 3. type shop name to access products in that shop\n 4. for help type 'help'""")
        #checking if who is in user message and giving its response
        if "who" in user_message:
            return str('   I am being  created by Edward Ali and william Pharaoh ')
        #checking if help is in user message and giving its response
        if "help" in user_message:

            return str('help Line \n  You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n 3. type shop name to access products in that shop\n')
        
        
    #checking whether shops is in user message 
    if 'shops' in user_message:
        return (allshops())
     

    #Checking whether user message is not in basics array 
    # filter user input   
    if user_message not in basics:
        #An array for filtering shops 
        filteredShop_arr=[]

        #An for filtering products 
        filtered_arr=[]
        splitText=user_message.split()
        for X in splitText:
       
            #checking if product is in the array and appending to the list
            if X in mother:
                filtered_arr.extend([p for p in data1 if p['Name'] ==X])

            #checking if shop is in the array and appending to the list
            if X in shopMother:
                filteredShop_arr.extend([s for s in data1 if s['Shop'] ==X])
        
        #checking if an array list is filtered 
        if filtered_arr:
            print("filtered array is")
            print(filtered_arr)
            #sorting the filtered array list by price in ascending order 
            sortedByPrice=sorted(filtered_arr, key=lambda x: x['Price'], reverse=False)
            print("sorrted by price in ascending order")
            print(sortedByPrice)
            #getting the cheapest 3 shops
            lowestThree=sortedByPrice[:3]
            print("lowest 3")
            print(lowestThree)

           
            
            
            firstThree = lowestThree
            #structuring the cheapest three shops in a table format
            datr = 'name     price       description     quantity        Shop\n\n'
            
            #appending the cheapest three products to the formatted table
            for product in firstThree:
                datr =datr+ f'{product["Name"]}       {product["Price"]}        {product["Description"]}      {product["Quantity"]}        {product["Shop"]}\n'
            
            return str(datr)
        #checking if an array for shops is filtered  
        if filteredShop_arr:
            #stucturing the products in the shops in a table format
            dtr ='Name     quantity  price\n'
            #sorting the filtered  shop proudcts using shop name
            sortedShop=sorted(filteredShop_arr, key=lambda x: x['Shop'])
            
            #appending the sorted shop products to the structured table format
            for w in sortedShop:
        
                dtr = dtr +  f'{w["Name"]}       {w["Quantity"]}       {w["Price"]}\n'

            return (dtr)

        #checking if an array is not filtered and giving its response
        if not filtered_arr:
             return str("Sorry, what you are trying to find is not available \n You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n 3. type shop name to access products in that shop\n 4. for help type 'help' ")
   
       
       

    else:
        return str("Sorry, what you are trying to find is not available \n\n ! You can access the following services.\n 1.Available shops typing shops.\n 2.Available product by typing name of the product\n 3. type shop name to access products in that shop\n 4. for help type 'help' ")



    
    
    
   

    

    
    

    


      

    