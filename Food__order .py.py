print("welcome To ADITYA'S FOOD CORNER")
print("_______________________________")
print("1. Burger - Rs. 80")
print("2. pizza - Rs. 150")
print("3. chicken masala - Rs. 200")


choice = input("choose your food(1-3):")


if choice == "1":
     print("you selected Burger")
     price = 80

               
elif choice == "2":
     print("you selected pizza")
     price = 150

     
elif choice == "3":
    print("you selected chicken masala")
    price = 200

    
else:
    print("invalid choice")
    price = 0
          

quantity = int(input("enter quantity:"))

subtotal = price * quantity
gst = subtotal * 5 /100
final__bill = subtotal + gst

print("food price : Rs.", subtotal)
print("GST (5%): Rs.", gst)
print("Final bill: Rs.", final__bill)
