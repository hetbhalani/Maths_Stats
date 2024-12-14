# from flask import Flask, render_template, request
# from tabulate import tabulate

# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
# def main():
#     xi = []
#     fi = []
#     fixi = []
#     total_sum = 0
#     mean = 0
#     n = 0
    
#     if request.method == "POST":
#         a1 = int(request.form["data_type"])

#         if a1 == 1:
#             n = int(request.form["data_points"])
#             for i in range(n):
#                 xi1 = int(request.form[f"xi{i}"])
#                 fi1 = int(request.form[f"fi{i}"])
#                 xi.append(xi1)
#                 fi.append(fi1)
            
#             for i in range(n):
#                 fixi.append(xi[i] * fi[i])

#             total_sum = sum(fi)
#             mean = sum(fixi) / total_sum

#         elif a1 == 2:
#             n = int(request.form["data_points"])
#             for i in range(n):
#                 temp_range = request.form[f"range{i}"]
#                 tempOfTemp = temp_range.split("-")
#                 xi.append((int(tempOfTemp[0]) + int(tempOfTemp[1])) / 2)
#                 fi1 = int(request.form[f"fi{i}"])
#                 fi.append(fi1)

#             for i in range(n):
#                 fixi.append(xi[i] * fi[i])

#             total_sum = sum(fi)
#             mean = sum(fixi) / total_sum

#         else:
#             return render_template("home.html", error="Invalid choice!")

#         return render_template("home.html", xi=xi, fi=fi, fixi=fixi, total_sum=total_sum, mean=mean, n=n)

#     return render_template("home.html")


# if __name__ == "__main__":
#     app.run(debug=True)






from flask import Flask, render_template, request
from tabulate import tabulate


# app = Flask(__name__)

# @app.route("/", methods=["GET", "POST"])
def main():
    xi = []
    fi = []
    fixi = []
    total_sum = 0
    mean = 0
    temp = []
    tbl = []
    
    
    a1 = int(input("enter 1 for normal and 2 for rang data: "))
    
    if a1 == 1:
        n = int(input("Enter number of data: "))
        for i in range (0,n):
            xi1 = int(input(f'Enter {i+1} data: '))
            fi1 = int(input(f'Enter frenquency of {i+1}: '))
            xi.append(xi1)
            fi.append(fi1)
        
        for i in range (0,n):  
            fixi.append(xi[i] * fi[i])
            tbl.append([xi[i], fi[i], fixi[i]])  
        total_sum = sum(fi)
        mean = sum(fixi) / total_sum

        tbl.append(["Total", total_sum, sum(fixi)])
        table = tabulate(
            tbl,headers=["xi","fi","fixi"],tablefmt="grid",stralign="center", colalign=("center", "center", "center")
        )
        print(table)
        print(f'mean of the sum is: {mean}') 

        
        
    elif(a1 == 2):
        n = int(input("Enter number of data: "))
        for i in range (0,n):
            temp.append((input(f"Enter a {i+1} range: ")))
            tempOfTemp = temp[i].split("-")
            xi.append((int(tempOfTemp[0])+int(tempOfTemp[1]))/2)    
            tempOfTemp.clear() 
            fi.append(int(input(f'Enter frenquency of {i+1}: ')))
            
        
        for i in range (0,n):  
            fixi.append(xi[i] * fi[i])
            tbl.append([temp[i], fi[i], fixi[i]])  
        total_sum = sum(fi)
        mean = sum(fixi) / total_sum

        tbl.append(["Total", total_sum, sum(fixi)])
        
        table = tabulate(
            tbl,headers=["xi","fi","fixi"],tablefmt="grid",stralign="center", colalign=("center", "center", "center")
        )
        print(table)
        print(f'mean of the sum is: {mean}') 

        
    else:
        print("Enter a valid choice bhaibandh")
                
        

if __name__ == "__main__":
    main()  