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

def main():
    xi = []
    fi = []
    di = []
    ui = []
    fixi = []
    fidi = []
    fiui = []
    total_sum = 0
    mean = 0
    temp = []
    tbl = []
    
    a2 = int(input("1 for Direct Method\n2 for Assumed Mean Method\n3 for Step Deviation Method\n Enter choice: "))
    
    if a2 == 1:
        a3 = int(input("enter 1 for normal and 2 for ranged data: "))
        
        if a3 == 1:
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
            print(f'mean of the sum is: {mean:.4f}') 

            
            
        elif(a3 == 2):
            n = int(input("Enter number of data: "))
            for i in range (0,n):
                temp.append((input(f"Enter a {i+1} range: ")))
                tempOfTemp = temp[i].split("-")
                xi.append((int(tempOfTemp[0])+int(tempOfTemp[1]))/2)    
                tempOfTemp.clear() 
                fi.append(int(input(f'Enter frenquency of {i+1}: ')))
                
            
            for i in range (0,n):  
                fixi.append(xi[i] * fi[i])
                tbl.append([temp[i],xi[i], fi[i], fixi[i]]) 
                
            total_sum = sum(fi)
            mean = sum(fixi) / total_sum

            tbl.append(["Total"," ", total_sum, sum(fixi)])
            
            table = tabulate(
                tbl,headers=["Class","xi","fi","fixi"],tablefmt="grid",stralign="center", colalign=("center", "center", "center")
            )
            print(table)
            print(f'mean of the sum is: {mean:.4f}') 
    
        else:
            print("Enter a valid choice bhaibandh")
            
            
    elif a2 == 2:
        a3 = int(input("enter 1 for normal and 2 for ranged data: "))
        
        if a3 == 1:
            n = int(input("Enter number of data: "))
            
            for i in range (n):
                xi1 = int(input(f'Enter {i+1} data: '))
                fi1 = int(input(f'Enter frenquency of {i+1}: '))
                
                xi.append(xi1)
                fi.append(fi1)
             
            A = xi[n // 2] #assum A as center of xi
                
            for i in range (n):
                di.append(xi[i] - A)
                fidi.append(fi[i]*di[i])
                if i == n//2:
                    tbl.append([f'{xi[i]} = A',fi[i],di[i],fidi[i]])
                else:
                    tbl.append([xi[i],fi[i],di[i],fidi[i]])
                
                
            total_sum = sum(fi)
            mean = (sum(fidi) / total_sum)+A
            tbl.append(["Total", total_sum," ", sum(fidi)])

            table = tabulate(
                tbl,headers=["xi","fi","di","fidi"],tablefmt="grid",stralign="center", colalign=("center", "center", "center","center")
            )
            print(table)
            print(f'mean of the sum is: {mean:.4f}') 

        elif a3 == 2:
            n = int(input("Enter number of data: "))
            
            for i in range (n):
                temp.append((input(f"Enter a {i+1} range: ")))
                tempOfTemp = temp[i].split("-")
                xi.append((int(tempOfTemp[0])+int(tempOfTemp[1]))/2)    
                tempOfTemp.clear() 
                fi.append(int(input(f'Enter frenquency of {i+1}: ')))

            A = xi[n // 2]
            
            for i in range (n):
                di.append(xi[i] - A)
                fidi.append(di[i] * fi[i])
                if i == n//2:
                    tbl.append([temp[i],f'{xi[i]} = A',fi[i],di[i],fidi[i]])
                else:
                    tbl.append([temp[i],xi[i],fi[i],di[i],fidi[i]])
                    
            total_sum = sum(fi)
            mean = (sum(fidi) / total_sum)+A
            tbl.append(["Total"," ", total_sum," ", sum(fidi)])

            table = tabulate(
                tbl,headers=["Class","xi","fi","di","fidi"],tablefmt="grid",stralign="center", colalign=("center","center", "center", "center","center")
            )
            print(table)
            print(f'mean of the sum is: {mean:.4f}') 
        
        else:
            print("Enter a valid choice")
            
            
    elif a2 == 3:
        n = int(input("Enter numner of data: "))
        
        print(f"Enter {n} ranged datas")
        
        for i in range (n):
            temp.append((input(f"Enter a {i+1} range: ")))
            tempOfTemp = temp[i].split("-")
            c = int(tempOfTemp[1]) - int(tempOfTemp[0])
            xi.append((int(tempOfTemp[0])+int(tempOfTemp[1]))/2)    
            tempOfTemp.clear() 
            fi.append(int(input(f'Enter frenquency of {i+1}: ')))
            
        A = xi[n // 2]
            
        for i in range (n):
            ui.append((xi[i] - A)/c)
            fiui.append(ui[i] * fi[i])
            if i == n//2:
                tbl.append([temp[i],f'{xi[i]} = A',fi[i],ui[i],fiui[i]])
            else:
                tbl.append([temp[i],xi[i],fi[i],ui[i],fiui[i]])
                
        total_sum = sum(fi)
        mean = ((sum(fiui) / total_sum)*c)+A
        tbl.append(["Total"," ", total_sum," ", sum(fiui)])

        table = tabulate(
            tbl,headers=["Class","xi","fi","ui","fiui"],tablefmt="grid",stralign="center", colalign=("center","center", "center", "center","center")
        )
        
        print(table)
        print(f'mean of the sum is: {mean:.4f}')
        
    else:
        print("Enter a valid choice")
                
if __name__ == "__main__":
    main()  