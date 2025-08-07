from flask import Flask, request, render_template
from glottal_parser import GlottalParser

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    glyph_input = ''
    if request.method == 'POST':
        glyph_input = request.form.get('glyph', '')
        parser = GlottalParser()
        result = parser.parse(glyph_input)
    return render_template('index.html', result=result, glyph=glyph_input)

if __name__ == '__main__':
    app.run(debug=True)
