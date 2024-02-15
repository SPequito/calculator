import tkinter as tk

calc = ""
##create the panel 
root = tk.Tk()

# insert data on my fielText
def add_to_cal(symbol):
    global calc

    calc += str(symbol) 
    result.delete(1.0, "end")
    result.insert(1.0, calc)
    
# function that going to do the read the field and do the calculation be carful using eval function because is not a secured method  people can inject code but for this exercise is ok   
def result_calculation():
        global calc
        
        try:
            calc = str(eval(calc))
            result.delete(1.0, "end")
            result.insert(1.0, calc)
        except:
            clear_all_data()
            #result.delete(1.0, "error")
            result.insert(1.0, "error")
            
# function  that clear all data        
def  clear_all_data():
    global calc
    calc = ""
    result.delete(1.0, "end")
    
 # function  that clear one by one start at the end    
def  clear_one_by_one():
     global calc  
     
     calc = calc[:-1]
     result.delete("end-2c")

     print(calc)   

#create the panel 
root.geometry("300x275")

result = tk.Text(root, height=2,width=16, font=("Arial", 24))
result.grid(columnspan= 6)

#create botton

bt_1 = tk.Button(root, text=("1"), command=lambda : add_to_cal(1), width=5, font=("Arial", 14))
bt_1.grid(row=2,column=1)

bt_2 = tk.Button(root, text=("2"), command=lambda : add_to_cal(2), width=5, font=("Arial", 14))
bt_2.grid(row=2,column=2)

bt_3 = tk.Button(root, text=("3"), command=lambda : add_to_cal(3), width=5, font=("Arial", 14))
bt_3.grid(row=2,column=3)

bt_4 = tk.Button(root, text=("4"), command=lambda : add_to_cal(4), width=5, font=("Arial", 14))
bt_4.grid(row=3,column=1)

bt_5 = tk.Button(root, text=("5"), command=lambda : add_to_cal(5), width=5, font=("Arial", 14))
bt_5.grid(row=3,column=2)

bt_6 = tk.Button(root, text=("6"), command=lambda : add_to_cal(6), width=5, font=("Arial", 14))
bt_6.grid(row=3,column=3)

bt_7 = tk.Button(root, text=("7"), command=lambda : add_to_cal(7), width=5, font=("Arial", 14))
bt_7.grid(row=4,column=1)

bt_8 = tk.Button(root, text=("8"), command=lambda : add_to_cal(8), width=5, font=("Arial", 14))
bt_8.grid(row=4,column=2)

bt_9 = tk.Button(root, text=("9"), command=lambda : add_to_cal(9), width=5, font=("Arial", 14))
bt_9.grid(row=4,column=3)

bt_0 = tk.Button(root, text=("0"), command=lambda : add_to_cal(0), width=5, font=("Arial", 14))
bt_0.grid(row=5,column=1)

bt_plus = tk.Button(root, text=("+"), command=lambda : add_to_cal("+"), width=5, font=("Arial", 14))
bt_plus.grid(row=2,column=4)

bt_minus = tk.Button(root, text=("-"), command=lambda : add_to_cal("-"), width=5, font=("Arial", 14))
bt_minus.grid(row=3,column=4)

bt_dot = tk.Button(root, text=("."), command=lambda : add_to_cal("."), width=5, font=("Arial", 14))
bt_dot.grid(row=6,column=3)

bt_mult = tk.Button(root, text=("x"), command=lambda : add_to_cal("*"), width=5, font=("Arial", 14))
bt_mult.grid(row=4,column=4)

bt_div = tk.Button(root, text=("/"), command=lambda : add_to_cal("/"), width=5, font=("Arial", 14))
bt_div.grid(row=5,column=4)

bt_result = tk.Button(root, text=("="), command= result_calculation, width=5, font=("Arial", 14))
bt_result.grid(row=6,column=4)

bt_clear_all = tk.Button(root, text=("C"), command=clear_all_data, width=5, font=("Arial", 14))
bt_clear_all.grid(row=5,column=2)

bt_clear_one = tk.Button(root, text=("c"),command=clear_one_by_one, width=5, font=("Arial", 14))
bt_clear_one.grid(row=5,column=3)

bt_right_parentheses = tk.Button(root, text=(")"),command=lambda : add_to_cal(")"), width=5, font=("Arial", 14))
bt_right_parentheses.grid(row=6,column=2)

bt_left_parentheses = tk.Button(root, text=("("),command=lambda : add_to_cal("("), width=5, font=("Arial", 14))
bt_left_parentheses.grid(row=6,column=1)

#close panel
root.mainloop()