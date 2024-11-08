menu ={
  'pasta':50,
  'pizza':100,
  'burger':150,
  'frenchfries':65,
  'noodles':80
}  

print("welcome to PYTHON restuarant:")
print("pasta:Rs50\npizza:Rs100\nburger:Rs150\nfrenchfries:Rs65\nnoodles:Rs80")
item_1=input("the item you want to order:")
order_total =0
if item_1 in menu :
  order_total += menu[item_1]
  print(f"your item {item_1} has been added")
else:
  print(f" your item {item_1} is not available yet!")
another_order=input("do you want to order something else? (yes/n0)")  
if another_order == "yes":
  item_2=input("enter your second item:")
  if item_2 in menu:
    order_total +=menu[item_2]
    print(f"item {item_2} has been added to order")
  else:
    print(f" your item {item_2} is not available yet!")
another_orderrr=input("do you want to order something else? (yes/n0)")  
if another_orderrr == "yes":
  item_3=input("enter your third item:")
  if item_3 in menu:
    order_total +=menu[item_3]
    print(f"item {item_3} has been added to order")
  else:
    print(f" your item {item_3} is not available yet!")      
print(f" the total amount of items to pay is {order_total}")    


