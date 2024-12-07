# from flask import Flask, render_template

# app = Flask(__name__)

# @app.route("/")
# def home(): 
#     return render_template("home.html")



# if __name__ == "__main__":
#     app.run(debug=True)

def main():
    l1 = []
    l2 = []
    fixi = []
    total_sum = 0
    mean = 0
    a1 = int(input("enter 1 for normal and 2 for rang data: "))
    
    if a1 == 1:
        n = int(input("Enter number of data: "))
        for i in range (0,n):
            xi1 = int(input(f'Enter {i+1} data: '))
            fi1 = int(input(f'Enter frenquency of {i+1}: '))
            l1.append(xi1)
            l2.append(fi1)
        
        for i in range (0,n):
            fixi.append(l1[i] * l2[i])
            
        total_sum = sum(l2)
        mean = sum(fixi)/total_sum
        
        
        print("| xi  |  fi | fixi|")
        print("|-----|-----|-----|")
        for i in range (0,n):
            
            print(f'|  {l1[i]}  |  {l2[i]}  |  {fixi[i]}  |')
            print("|-----|-----|-----|")
        print(f'|  {total_sum}  |     |  {sum(fixi)  }')
        
    elif(a1 == 2):
        n = int(input("Enter number of data: "))
        
            
    print(f'mean of the sum is {mean}')

if __name__ == "__main__":
    main()
    