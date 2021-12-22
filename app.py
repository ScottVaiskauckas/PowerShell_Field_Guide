from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("Learn.html")

@app.route("/links")
def links():
    return render_template("links.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/liveclip")
def live_clip():
    return render_template("liveclip.html")

@app.route("/PowerShell/1")
def intro():
    return render_template("PowerShell/Introduction.html")

@app.route("/PowerShell/2")
def start():
    return render_template("PowerShell/Start.html")

@app.route("/PowerShell/3")
def basics():
    return render_template("PowerShell/Basics.html")

@app.route("/PowerShell/4")
def datatypes():
    return render_template("PowerShell/DataTypes.html")

@app.route("/PowerShell/5")
def math():
    return render_template("PowerShell/MathOperators.html")

@app.route("/PowerShell/6")
def comparison():
    return render_template("PowerShell/ComparisonOperators.html")

@app.route("/PowerShell/7")
def variables():
    return render_template("PowerShell/Variables.html")

@app.route("/PowerShell/8")
def assignment():
    return render_template("PowerShell/AssignmentOperators.html")

@app.route("/PowerShell/9")
def logical():
    return render_template("PowerShell/LogicalOperators.html")

@app.route("/PowerShell/10")
def posh_if():
    return render_template("PowerShell/If.html")

@app.route("/PowerShell/11")
def posh_else():
    return render_template("PowerShell/Else.html")

@app.route("/PowerShell/12")
def nestedif():
    return render_template("PowerShell/NestedIf.html")

@app.route("/PowerShell/13")
def elseif():
    return render_template("PowerShell/ElseIf.html")

@app.route("/PowerShell/14")
def switch():
    return render_template("PowerShell/Switch.html")

@app.route("/PowerShell/15")
def posh_while():
    return render_template("PowerShell/While.html")

@app.route("/PowerShell/16")
def posh_for():
    return render_template("PowerShell/For.html")

@app.route("/PowerShell/17")
def arrays():
    return render_template("PowerShell/Arrays.html")

@app.route("/PowerShell/18")
def foreach():
    return render_template("PowerShell/ForEach.html")

@app.route("/PowerShell/19")
def lists():
    return render_template("PowerShell/Lists.html")

@app.route("/PowerShell/20")
def arraylists():
    return render_template("PowerShell/Arraylists.html")

@app.route("/PowerShell/21")
def hashtables():
    return render_template("PowerShell/Hashtables.html")

@app.route("/PowerShell/22")
def readhost():
    return render_template("PowerShell/ReadHost.html")

@app.route("/PowerShell/23")
def printfiles1():
    return render_template("PowerShell/PrintFiles1.html")

@app.route("/PowerShell/24")
def positional():
    return render_template("PowerShell/PositionalParams.html")

@app.route("/PowerShell/25")
def printfiles2():
    return render_template("PowerShell/PrintFiles2.html")

@app.route("/PowerShell/26")
def namedparams():
    return render_template("PowerShell/NamedParams.html")

@app.route("/PowerShell/27")
def printfiles3():
    return render_template("PowerShell/PrintFiles3.html")

@app.route("/PowerShell/28")
def functions():
    return render_template("PowerShell/Functions.html")

@app.route("/PowerShell/29")
def classes():
    return render_template("PowerShell/Classes.html")

@app.route("/PowerShell/30")
def persistance():
    return render_template("PowerShell/Persistance.html")

@app.route("/PowerShell/31")
def txt():
    return render_template("PowerShell/Txt.html")

@app.route("/PowerShell/32")
def csv():
    return render_template("PowerShell/Csv.html")

@app.route("/PowerShell/33")
def xml():
    return render_template("PowerShell/Xml.html")

@app.route("/PowerShell/34")
def msiexec():
    return render_template("PowerShell/msiexec.html")

@app.route("/PowerShell/35")
def uis():
    return render_template("PowerShell/UIs.html")

@app.route("/learn")
def learn():
    return render_template("Learn.html")

if __name__ == '__main__':
    app.run(debug = True)