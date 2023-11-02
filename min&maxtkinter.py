from tkinter import *
root = Tk()
root.geometry("500x500")
root.title("Sales Application")

month = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December")
months_window = Label(root,text = month)

##print(months_window)

profits = [20000, 45000, 78000, 97000, 12000, 456000, 65000, 54000, 10000, 30000, 70000, 90000]
profits_window = Label(root, text = profits)
##print(profits_window)

max_profit_window = Label(root)
min_profit_window = Label(root)


def findMaxProfits():
    max_profit = max(profits)
    max_profit_index = profits.index(max_profit)
    print(max_profit)
    print(max_profit_index)

    max_profit_month = month[max_profit_index]
    print(max_profit_month)
    print("The maximum profit of " +str(max_profit)+ " was recorded in the month of " + str(max_profit_month))
    

    max_profit_window["text"] = "Maximum profit of " + str(max_profit) + " was recorded in the month of " + str(max_profit_month)


def things():
    print("The maximum profit of " +str(max_profit)+ " was recorded in the month of " + str(max_profit_month)+" and, the minimun profit of " +str(min_profit)+ " was recorded in the month of " + str(min_profit_month))  
    months_window["text"] = "Months: " + str(month)
    profits_window["text"] = "Profits: " + str(profits)
    
def findMinProfits():
    min_profit = min(profits)
    min_profit_index = profits.index(min_profit)
    ##print(min_profit_index)

    min_profit_month = month[min_profit_index]
    ##print(min_profit_month)
    ##print("The minimun profit of " +str(min_profit)+ " was recorded in the month of " + str(min_profit_month))

    
    min_profit_window["text"] = "Minimum profit of " + str(min_profit) + " was recorded in the month of " + str(min_profit_month)
    
max_profit_show = Button(root, text="Show the Max Profitable Month",command = findMaxProfits)
max_profit_show.place(relx= 0.5, rely = 0.3, anchor=CENTER)

min_profit_show = Button(root, text="Show the Min Profitable Month", command = findMinProfits)
min_profit_show.place(relx= 0.5, rely = 0.5, anchor=CENTER)

months_window.place(relx= 0.5, rely=0.1, anchor=CENTER)
profits_window.place(relx= 0.5,rely=0.2, anchor=CENTER)
max_profit_window.place(relx=0.5,rely=0.4, anchor=CENTER)
min_profit_window.place(relx=0.5,rely=0.6, anchor=CENTER)

root.mainloop()
