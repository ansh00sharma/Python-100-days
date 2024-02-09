from flask import Flask

app = Flask(__name__)

correct_num = 8

# def correct_decorator(function):
#     def wrapper():
#         '<div style= "color:green;">' + function() + '</div>'
#     return wrapper


def correct_guessed():
    correct_gif = "https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif"
    return '<h2 style= "color:green;">You Guessed it Correct ! </h2> ' \
           f'<img src = "{correct_gif}">'

def less_guessed():
    lesser_gif = "https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif"
    return '<h2 style= "color:red;" >Too Low ! Try Again  </h2> ' \
           f'<img src = "{lesser_gif}">'


def greater_guessed():
    greater_gif = "https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif"
    return '<h2 style= "color:purple;">Too High, Try Again </h2> ' \
           f'<img src = "{greater_gif}">'

@app.route('/')
def first():
    root_gif = "https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif"
    return '<h2>Guess the Correct Number ! </h2> ' \
           f'<img src = "{root_gif}">'

@app.route('/<num>')
def check_number(num):
    if  int(num) == correct_num:
        return correct_guessed()
        
    elif  int(num) < correct_num:
        return less_guessed()

    else:
        return greater_guessed()

if __name__ == "__main__":
    app.run(debug=True)