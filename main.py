# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home(): 
#     return render_template("home.html")



# if __name__ == "__main__":
#     app.run(debug=True)

def main():
    xi = []
    fi = []
    fixi = []
    total_sum = 0
    mean = 0
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
            
        total_sum = sum(fi)
        mean = sum(fixi)/total_sum
        
        
        print("| xi  |  fi | fixi|")
        print("|-----|-----|-----|")
        for i in range (0,n):
            
            print(f'|  {xi[i]}  |  {fi[i]}  |  {fixi[i]}  |')
            print("|-----|-----|-----|")
        print(f'|  {total_sum}  |     |  {sum(fixi)  }')
        
        
    elif(a1 == 2):
        n = int(input("Enter number of data: "))
        for i in range (0,n):
            temp = (input(f"Enter a {i+1} range: ").split("-"))
            xi.append((temp[0]+temp[1])/2)    
            temp.clear() 
            fi1 = int(input(f'Enter frenquency of {i+1}: '))
            fi.append(fi1[i])
            
        for i in range (0,n):
            fixi.append(xi[i] * fi[i])
            
            
    print(f'mean of the sum is {mean}')

if __name__ == "__main__":
    main()
    