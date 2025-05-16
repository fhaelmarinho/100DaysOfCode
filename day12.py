from flask import Flask, render_template, request

app = Flask (__name__, template_folder='playlist_com_letras/templates')

@app.route('/', methods=['GET','POST'])
def index():
    lyrics = ""
    if request.method == 'POST':
        music = request.form['music']
        artist = request.form['artist']
        lyrics = f"Lyrics para {music} of the {artist}"
        return
    render_template('index.html', lyrics=lyrics)
    
    if __name__ == '__main__':
        app.run(debug=True)