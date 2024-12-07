from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
    xi = []
    fi = []
    fixi = []
    total_sum = 0
    mean = 0
    n = 0
    
    if request.method == "POST":
        a1 = int(request.form["data_type"])

        if a1 == 1:
            n = int(request.form["data_points"])
            for i in range(n):
                xi1 = int(request.form[f"xi{i}"])
                fi1 = int(request.form[f"fi{i}"])
                xi.append(xi1)
                fi.append(fi1)
            
            for i in range(n):
                fixi.append(xi[i] * fi[i])

            total_sum = sum(fi)
            mean = sum(fixi) / total_sum

        elif a1 == 2:
            n = int(request.form["data_points"])
            for i in range(n):
                temp_range = request.form[f"range{i}"]
                tempOfTemp = temp_range.split("-")
                xi.append((int(tempOfTemp[0]) + int(tempOfTemp[1])) / 2)
                fi1 = int(request.form[f"fi{i}"])
                fi.append(fi1)

            for i in range(n):
                fixi.append(xi[i] * fi[i])

            total_sum = sum(fi)
            mean = sum(fixi) / total_sum

        else:
            return render_template("home.html", error="Invalid choice!")

        return render_template("home.html", xi=xi, fi=fi, fixi=fixi, total_sum=total_sum, mean=mean, n=n)

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)
