from flask import Flask, render_template, request

index_file = "index.html"

app = Flask(__name__)

@app.route("/")
def index():
    return render_template(index_file)

@app.route("/convert-length", methods=["POST"])
def convert_length():
    lengthFrom = request.form["lengthFrom"]
    lengthTo = request.form["lengthTo"]
    lengthInput = int(request.form["lengthInput"])
    
    if lengthFrom == 'millimeter':
        if lengthTo == 'centimeter':
            converted = (lengthInput / 10)
        elif lengthTo == 'meter':
            converted = (lengthInput / 1000)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 1,000,000)
        elif lengthTo == 'inch':
            converted = (lengthInput / 25.4)
        elif lengthTo == 'foot':
            converted = (lengthInput / 304.8)
        elif lengthTo == 'yard':
            converted = (lengthInput / 914.4)
        elif lengthTo == 'mile':
            converted = (lengthInput / 1,609,344)
        else:
            return str(lengthInput)
        
    elif lengthFrom == 'centimeter':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 10)
        elif lengthTo == 'meter':
            converted = (lengthInput / 10)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 100,000)
        elif lengthTo == 'inch':
            converted = (lengthInput / 2.54)
        elif lengthTo == 'foot':
            converted = (lengthInput / 30.48)
        elif lengthTo == 'yard':
            converted = (lengthInput / 91.44)
        elif lengthTo == 'mile':
            converted = (lengthInput / 160,934.4)
        else:
            return str(lengthInput)
        
    elif lengthFrom == 'meter':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 1000)
        elif lengthTo == 'centimeter':
            converted = (lengthInput / 100)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 1000)
        elif lengthTo == 'inch':
            converted = (lengthInput / 0.0254)
        elif lengthTo == 'foot':
            converted = (lengthInput * 3.28084)
        elif lengthTo == 'yard':
            converted = (lengthInput * 1.09361)
        elif lengthTo == 'mile':
            converted = (lengthInput / 1609.344)
        else:
            return str(lengthInput)
        
    elif lengthFrom == 'kilometer':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 1,000,000)
        elif lengthTo == 'centimeter':
            converted = (lengthInput / 100,000)
        elif lengthTo == 'meter':
            converted = (lengthInput * 1000)
        elif lengthTo == 'inch':
            converted = (lengthInput * 39,370.1)
        elif lengthTo == 'foot':
            converted = (lengthInput * 3280.84)
        elif lengthTo == 'yard':
            converted = (lengthInput * 1093.61)
        elif lengthTo == 'mile':
            converted = (lengthInput / 1.609344)
        else:
            return str(lengthInput)
        
    elif lengthFrom == 'inch':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 25.4)
        elif lengthTo == 'centimeter':
            converted = (lengthInput * 2.54)
        elif lengthTo == 'meter':
            converted = (lengthInput * 0.0254)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 39,370.1)
        elif lengthTo == 'foot':
            converted = (lengthInput / 12)
        elif lengthTo == 'yard':
            converted = (lengthInput / 36)
        elif lengthTo == 'mile':
            converted = (lengthInput / 63,360)
        else:
            return str(lengthInput)
        
    elif lengthFrom == 'foot':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 304.8)
        elif lengthTo == 'centimeter':
            converted = (lengthInput * 30.48)
        elif lengthTo == 'meter':
            converted = (lengthInput * 0.3048)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 3280.84)
        elif lengthTo == 'inch':
            converted = (lengthInput * 12)
        elif lengthTo == 'yard':
            converted = (lengthInput / 3)
        elif lengthTo == 'mile':
            converted = (lengthInput / 5280)
        else:
            return str(lengthInput)
    
    elif lengthFrom == 'yard':
        if lengthTo == 'millimeter':
            converted = (lengthInput * 914.4)
        elif lengthTo == 'centimeter':
            converted = (lengthInput * 91.44)
        elif lengthTo == 'meter':
            converted = (lengthInput * 0.9144)
        elif lengthTo == 'kilometer':
            converted = (lengthInput / 1093.61)
        elif lengthTo == 'inch':
            converted = (lengthInput * 36)
        elif lengthTo == 'foot':
            converted = (lengthInput * 3)
        elif lengthTo == 'mile':
            converted = (lengthInput / 1760)
        else:
            return str(lengthInput)
    else:
        return "yeah bruv"

    return f'{str(converted)}'


@app.route("/convert-weight", methods=["POST"])
def convert_weight():
    weightFrom = request.form["weightFrom"]
    weightTo = request.form["weightTo"]
    weightInput = int(request.form["weightInput"])

    if weightFrom == 'milligram':
        if weightTo == 'gram':
            converted = (weightInput / 1000)
        elif weightTo == 'kilogram':
            converted = (weightInput / 1,000,000)
        elif weightTo == 'ounce':
            converted = (weightInput / 28,349.5)
        elif weightTo == 'pound':
            converted = (weightInput / 453,592)
        else:
            return str(weightInput)
        
    elif weightFrom == 'gram':
        if weightTo == 'milligram':
            converted = (weightInput * 1000)
        elif weightTo == 'kilogram':
            converted = (weightInput / 1,000)
        elif weightTo == 'ounce':
            converted = (weightInput / 28.3495)
        elif weightTo == 'pound':
            converted = (weightInput / 453.592)
        else:
            return str(weightInput)
        
    elif weightFrom == 'kilogram':
        if weightTo == 'milligram':
            converted = (weightInput * 1,000,000)
        elif weightTo == 'gram':
            converted = (weightInput * 1,000)
        elif weightTo == 'ounce':
            converted = (weightInput * 35.274)
        elif weightTo == 'pound':
            converted = (weightInput * 2.20462)
        else:
            return str(weightInput)

    elif weightFrom == 'ounce':
        if weightTo == 'milligram':
            converted = (weightInput * 28,349.5)
        elif weightTo == 'gram':
            converted = (weightInput * 28.3495)
        elif weightTo == 'kilogram':
            converted = (weightInput / 35.274)
        elif weightTo == 'pound':
            converted = (weightInput / 16)
        else:
            return str(weightInput)
        
    elif weightFrom == 'pound':
        if weightTo == 'milligram':
            converted = (weightInput * 453,592)
        elif weightTo == 'gram':
            converted = (weightInput * 453.592)
        elif weightTo == 'kilogram':
            converted = (weightInput / 2.20462)
        elif weightTo == 'ounce':
            converted = (weightInput * 16)
        else:
            return str(weightInput)
        
    else:
        return "yeah bruv"

    return f'{str(converted)}'

@app.route("/convert-temperature", methods=["POST"])
def convert_temperature():
    tempFrom = request.form["tempFrom"]
    tempTo = request.form["tempTo"]
    tempInput = int(request.form["tempInput"])

    if tempFrom == 'celcius':
        if tempTo == 'fahrenheit':
            converted = ((tempInput * 9/5) + 32)
        elif tempTo == 'kelvin':
            converted = (tempInput + 273.15)
        else:
            return str(tempInput)
        
    elif tempFrom == 'fahrenheit':
        if tempTo == 'celcius':
            converted = ((tempInput - 32) * 5/9)
        elif tempTo == 'kelvin':
            converted = ((tempInput - 32) * 5/9 + 273.15)
        else:
            return str(tempInput)
        
    elif tempFrom == 'kelvin':
        if tempTo == 'celcius':
            converted = (tempInput - 273.15)
        elif tempTo == 'fahrenheit':
            converted = ((tempInput - 273.15) * 9/5 - + 32)
        else:
            return str(tempInput)
    else:
        return "yeah bruv"
    
    return f'{str(converted)}'

if __name__ == "__main__":
    app.run(debug=True)