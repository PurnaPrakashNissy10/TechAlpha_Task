from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)


def generate_password(length, use_uppercase, use_numbers, use_special):
    characters = string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_numbers:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))
    return password


@app.route('/', methods=['GET', 'POST'])
def index():
    password = ''
    if request.method == 'POST':
        length = int(request.form.get('length', 12))
        use_uppercase = 'uppercase' in request.form
        use_numbers = 'numbers' in request.form
        use_special = 'special' in request.form
        password = generate_password(length, use_uppercase, use_numbers, use_special)
    return render_template('index.html', password=password)


if __name__ == '__main__':
    app.run(debug=True)
