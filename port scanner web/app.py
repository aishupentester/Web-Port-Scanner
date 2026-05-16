from flask import Flask, render_template, request
import socket

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():

    open_ports = []

    if request.method == 'POST':

        target = request.form['target']

        ports = [21, 22, 23, 25, 53, 80, 110, 443]

        for port in ports:

            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            s.settimeout(1)

            result = s.connect_ex((target, port))

            if result == 0:
                open_ports.append(port)

            s.close()

        return render_template(
            'index.html',
            target=target,
            open_ports=open_ports
        )

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)