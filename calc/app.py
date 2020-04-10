from flask import Flask, request
import operations

app = Flask(__name__)


@app.route('/add')
def add1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operations.add(a, b)
    return f"{res}"


@app.route('/sub')
def sub1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operations.sub(a, b)
    return f"{res}"


@app.route('/mult')
def mult1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operations.mult(a, b)
    return f"{res}"


@app.route('/div')
def div1():
    a = int(request.args["a"])
    b = int(request.args["b"])
    res = operations.div(a, b)
    return f"{res}"


operators2 = {
    "add": operations.add,
    "sub": operations.sub,
    "mult": operations.mult,
    "div": operations.div,
}


@app.route("/math/<oper>")
def do_math(oper):
    """Do math on a and b."""

    a = int(request.args.get("a"))
    b = int(request.args.get("b"))
    res = operators2[oper](a, b)

    return str(res)
