from os import readlink
from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def checkerboard():
    return render_template("index.html", x = 8, y = 8, color1 ="red", color2 = "black") # Return the string 'Hello World!' as a response

@app.route('/<int:x>/<int:y>/')
def dimensionsOnly(x, y):
    return render_template("index.html", x = int(x), y = int(y), color1 = "red", color2 = "black")

@app.route('/<int:x>/<int:y>/<color1>/<color2>')
def colorsAndDimensions(x, y, color1, color2):
    return render_template("index.html", x = int(x), y = int(y), color1 = color1, color2 = color2)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

