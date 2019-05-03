from flask import Flask, render_template, redirect, url_for, request
import subprocess, os, signal
app = Flask(__name__)

@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        text = request.form.get("input")
        text2 = text.split('\n')

        with open("Main.java", "w+") as f:
            for i in text2:
                f.write(i)
            f.close()

        proc = subprocess.Popen(['javac', 'Main.java'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = proc.communicate()[0].decode("utf-8")

        if output == "":
            proc1 = subprocess.Popen(['java', 'Main'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = proc1.communicate()[0].decode("utf-8")

        return render_template("java.html", out=output, input1=text)
    return render_template("java.html")


@app.route("/Cpp.html", methods=['POST', 'GET'])
def cpp():
    if request.method == 'POST':
        text = request.form.get("input")
        text2 = text.split('\n')

        with open("co.cpp", "w+") as f:
            for i in text2:
                f.write(i)
            f.close()

        proc = subprocess.Popen(['g++', 'co.cpp'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = proc.communicate()[0].decode("utf-8")
        if output == "":
            proc1 = subprocess.Popen(['','./a.out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = proc1.communicate()[0].decode("utf-8")

        return render_template("Cpp.html", out=output, input1=text)
    return render_template("Cpp.html")

@app.route("/C.html", methods=['POST', 'GET'])
def clan():
    if request.method == 'POST':
        text = request.form.get("input")
        text2 = text.split('\n')

        with open("test.c", "w+") as f:
            for i in text2:
                f.write(i)
            f.close()

        proc = subprocess.Popen(['gcc', 'test.c'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = proc.communicate()[0].decode("utf-8")

        if output == "":
            proc1 = subprocess.Popen(['./a.out'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            output = proc1.communicate()[0].decode("utf-8")

        return render_template("C.html", out=output, input1=text)
    return render_template("C.html")


@app.route("/python.html", methods=['POST', 'GET'])
def python():
    if request.method == 'POST':
        text = request.form.get("input")
        text2 = text.split('\n')

        with open("sample.py", "w+") as f:
            for i in text2:
                f.write(i)
            f.close()

        proc = subprocess.Popen(['python', 'sample.py'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        output = proc.communicate()[0].decode("utf-8")

        return render_template("python.html", out=output, input1=text)
    return render_template("python.html")

if __name__ == "__main__":
    app.run(host="10.7.6.85", port=9000, debug = True )
    app.config['TEMPLATES_AUTO_RELOAD'] = True