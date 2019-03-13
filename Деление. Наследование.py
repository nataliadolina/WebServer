from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/div_mod', methods=['POST', 'GET'])
def div_mod():
    if request.method == 'GET':
        return render_template('division_base.html')

    elif request.method == 'POST':
        n1 = request.form['delimoe']
        n2 = request.form['delitel']
        if not n1.isdigit() or not n2.isdigit():
            return render_template('div_mod.html', text='некорректные данные')
        if n2 == '0':
            return render_template('div_mod.html', text='нельзя делить на ноль')
        t1, t2 = float(n1), float(n2)
        if t1 % t2 == 0:
            return render_template('div_mod.html', text=n1 + ' делится без остатка на ' + n2)
        else:
            return render_template('div_mod.html', text=n1 + ' не делится без остатка на ' + n2)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
