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
    cfi = []
    total_sum = 0
    mean = 0
    temp = []
    tbl = []
    
    print("Welcome to StatMan!")
    a1 = int(input("1 for Mean\n2 for Median\n3 for Mode\nEnter your choice: "))
    print()
    
    if a1 == 1:
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
    
    elif a1 == 2:
        a2 = int(input("1 for simple data\n2 for simple data with frequency\n3 for ranged data\nEnter your choice: "))
        
        if a2 == 1:
            n = int(input("Enter number of data: "))
            
            for i in range (n):
                xi1 = int(input(f'Enter {i+1} data: '))
                xi.append(xi1)
            
            if n % 2 == 0:
                print(f"Median of the sum is: {(xi[n//2] + xi[(n//2)+1])/2}")
            else:
                print(f"Median of the sum is: {xi[n//2]}")
                
        elif a2 == 2:
            n = int(input("Enter number of data: "))
            
            for i in range (n):
                xi1 = int(input(f'Enter {i+1} data: '))
                fi1 = int(input(f'Enter frenquency of {i+1}: '))
                
                xi.append(xi1)
                fi.append(fi1)
            
            combined = list(zip(xi,fi))
            
            combined.sort()
            
            sort_xi , sort_fi = zip(*combined) #unzip the list
            
            xi = list(sort_xi)
            fi = list(sort_fi)
            temp = 0
            
            for i in fi:
                temp += i
                cfi.append(temp)
                
            for i in range (n):
                tbl.append([xi[i],fi[i],cfi[i]])
            
            temp = sum(fi)//2
            tempi = 0
            
            for i in range (len(cfi)):
                if cfi[i]>temp:
                    tempi = i
                    break

            table = tabulate(
                tbl,headers=["xi","fi","cfi"],tablefmt="grid",stralign="center", colalign=("center", "center","center")
            )
            print(table)
            print(f'Median of the sum is: {xi[tempi]}')
            
        elif a2 == 3:
            n = int(input("Enter numner of data: "))
            
            print(f"Enter {n} ranged datas")
            
            tempForCfi = 0
            for i in range (n):
                temp.append((input(f"Enter a {i+1} range: ")))
                tempOfTemp = temp[i].split("-")
                c = int(tempOfTemp[1]) - int(tempOfTemp[0])
                xi.append((int(tempOfTemp[0])+int(tempOfTemp[1]))/2)    
                tempOfTemp.clear() 
                fi.append(int(input(f'Enter frenquency of {i+1}: ')))
                tempForCfi+=fi[i]
                cfi.append(tempForCfi)
                tbl.append([temp[i],fi[i],cfi[i]])
                
            nByTwo = sum(fi)//2
            tempi = 0
            while True:
                if nByTwo <= cfi[tempi]:
                    break
                tempi+=1
                
            f = fi[tempi]
            if tempi == 0:
                F = 0
            else:
                F = cfi[tempi-1]
            
            L = temp[tempi].split("-")
            
            median = int(L[0]) + (((nByTwo-F)/f)*c)
            
            table = tabulate(
                tbl,headers=["Class","fi","cfi"],tablefmt="grid",stralign="center", colalign=("center", "center","center")
            ) 
            print(table)
            print(f"Median of the sum is {median}")                       
if __name__ == "__main__":
    main()  


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





