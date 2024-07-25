import flask
import read 
import random

word_list = read.word_list

word = random.choice(word_list)



app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])


def first():
    if flask.request.method == 'POST':
        global letter1
        global letter2
        global letter3
        global letter4
        global letter5
        global color1
        global color2
        global color3
        global color4
        global color5
        color1 = ''
        color2 = ''
        color3 = ''
        color4 = ''
        color5 = ''
        letter1 = flask.request.form['text1']
        letter2 = flask.request.form['text2']
        letter3 = flask.request.form['text3']
        letter4 = flask.request.form['text4']
        letter5 = flask.request.form['text5']
        
        if f'{letter1}{letter2}{letter3}{letter4}{letter5}' not in word_list:
            return flask.render_template('index.html', first=True, second=False, third=False, fourth=False, fifth=False, sixth=False)
        else:
            if letter1 in word and letter1 == word[0]:
                color1 = 'g'
            if letter1 in word and letter1 != word[0]:
                color1 = 'y'
            if letter1 not in word:
                color1 = 'b'

            if letter2 in word and letter2 == word[1]:
                color2 = 'g'
            if letter2 in word and letter2 != word[1]:
                color2 = 'y'
            if letter2 not in word:
                color2 = 'b'

            if letter3 in word and letter3 == word[2]:
                color3 = 'g'
            if letter3 in word and letter3 != word[2]:
                color3 = 'y'
            if letter3 not in word:
                color3 = 'b'

            if letter4 in word and letter4 == word[3]:
                color4 = 'g'
            if letter4 in word and letter4 != word[3]:
                color4 = 'y'
            if letter4 not in word:
                color4 = 'b'

            if letter5 in word and letter5 == word[4]:
                color5 = 'g'
            if letter5 in word and letter5 != word[4]:
                color5 = 'y'
            if letter5 not in word:
                color5 = 'b'


            return flask.redirect('/second')

    return flask.render_template('index.html', first=True, second=False, third=False, fourth=False, fifth=False, sixth=False)

@app.route('/second', methods=['GET', 'POST'])
def second():
    if flask.request.method == 'POST':
        global letter21
        global letter22
        global letter23
        global letter24
        global letter25
        global color21
        global color22
        global color23
        global color24
        global color25
        color21 = ''
        color22 = ''
        color23 = ''
        color24 = ''
        color25 = ''

        letter21 = flask.request.form['text1']
        letter22 = flask.request.form['text2']
        letter23 = flask.request.form['text3']
        letter24 = flask.request.form['text4']
        letter25 = flask.request.form['text5']

        if f'{letter21}{letter22}{letter23}{letter24}{letter25}' not in word_list:
            return flask.render_template('index.html', first=False, second=True, third=False, fourth=False, fifth=False, sixth=False, second2=True, third3=False, fourth4=False, fifth5=False, sixth6=False
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5)

        else:
        

            if letter21 in word and letter21 == word[0]:
                color21 = 'g'
            if letter21 in word and letter21 != word[0]:
                color21 = 'y'
            if letter21 not in word:
                color21 = 'b'

            if letter22 in word and letter22 == word[1]:
                color22 = 'g'
            if letter22 in word and letter22 != word[1]:
                color22 = 'y'
            if letter22 not in word:
                color22 = 'b'

            if letter23 in word and letter23 == word[2]:
                color23 = 'g'
            if letter23 in word and letter23 != word[2]:
                color23 = 'y'
            if letter23 not in word:
                color23 = 'b'

            if letter24 in word and letter24 == word[3]:
                color24 = 'g'
            if letter24 in word and letter24 != word[3]:
                color24 = 'y'
            if letter24 not in word:
                color24 = 'b'

            if letter25 in word and letter25 == word[4]:
                color25 = 'g'
            if letter25 in word and letter25 != word[4]:
                color25 = 'y'
            if letter25 not in word:
                color25 = 'b'


            return flask.redirect('/third')

    return flask.render_template('index.html', first=False, second=True, third=False, fourth=False, fifth=False, sixth=False, second2=True, third3=False, fourth4=False, fifth5=False, sixth6=False
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5)

@app.route('/third', methods=['GET', 'POST'])
def third():
    if flask.request.method == 'POST':
        global letter31
        global letter32
        global letter33
        global letter34
        global letter35
        global color31
        global color32
        global color33
        global color34
        global color35
        color31 = ''
        color32 = ''
        color33 = ''
        color34 = ''
        color35 = ''
        letter31 = flask.request.form['text1']
        letter32 = flask.request.form['text2']
        letter33 = flask.request.form['text3']
        letter34 = flask.request.form['text4']
        letter35 = flask.request.form['text5']

        if f'{letter31}{letter32}{letter33}{letter34}{letter35}' not in word_list:
            return flask.render_template('index.html', first=False, second=False, third=True, fourth=False, fifth=False, sixth=False, second2=True, third3=True,
                                 letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5, 
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,)

        else:
            if letter31 in word and letter31 == word[0]:
                color31 = 'g'
            if letter31 in word and letter31 != word[0]:
                color31 = 'y'
            if letter31 not in word:
                color31 = 'b'

            if letter32 in word and letter32 == word[1]:
                color32 = 'g'
            if letter32 in word and letter32 != word[1]:
                color32 = 'y'
            if letter32 not in word:
                color32 = 'b'

            if letter33 in word and letter33 == word[2]:
                color33 = 'g'
            if letter33 in word and letter33 != word[2]:
                color33 = 'y'
            if letter33 not in word:
                color33 = 'b'

            if letter34 in word and letter34 == word[3]:
                color34 = 'g'
            if letter34 in word and letter34 != word[3]:
                color34 = 'y'
            if letter34 not in word:
                color34 = 'b'

            if letter35 in word and letter35 == word[4]:
                color35 = 'g'
            if letter35 in word and letter35 != word[4]:
                color35 = 'y'
            if letter35 not in word:
                color35 = 'b'
            return flask.redirect('/fourth')

    return flask.render_template('index.html', first=False, second=False, third=True, fourth=False, fifth=False, sixth=False, second2=True, third3=True,
                                 letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5, 
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,)

@app.route('/fourth', methods=['GET', 'POST'])
def fourth():
    if flask.request.method == 'POST':
        global letter41
        global letter42
        global letter43
        global letter44
        global letter45
        global color41
        global color42
        global color43
        global color44
        global color45
        color41 = ''
        color42 = ''
        color43 = ''
        color44 = ''
        color45 = ''
        letter41 = flask.request.form['text1']
        letter42 = flask.request.form['text2']
        letter43 = flask.request.form['text3']
        letter44 = flask.request.form['text4']
        letter45 = flask.request.form['text5']

        if f'{letter31}{letter32}{letter33}{letter34}{letter35}' not in word_list:
            return flask.render_template('index.html', first=False, second=False, third=False, fourth=True, fifth=False, sixth=False, second2=True, third3=True, fourth4=True,
                                 letter31=letter31, letter32=letter32, letter33=letter33, letter34=letter34, letter35=letter35
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5
                                 , letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                 color31=color31, color32=color32, color33=color33, color34=color34, color35=color35,)

        else:  
            if letter41 in word and letter41 == word[0]:
                color41 = 'g'
            if letter41 in word and letter41 != word[0]:
                color41 = 'y'
            if letter41 not in word:
                color41 = 'b'

            if letter42 in word and letter42 == word[1]:
                color42 = 'g'
            if letter42 in word and letter42 != word[1]:
                color42 = 'y'
            if letter42 not in word:
                color42 = 'b'

            if letter43 in word and letter43 == word[2]:
                color43 = 'g'
            if letter43 in word and letter43 != word[2]:
                color43 = 'y'
            if letter43 not in word:
                color43 = 'b'

            if letter44 in word and letter44 == word[3]:
                color44 = 'g'
            if letter44 in word and letter44 != word[3]:
                color44 = 'y'
            if letter44 not in word:
                color44 = 'b'

            if letter45 in word and letter45 == word[4]:
                color45 = 'g'
            if letter45 in word and letter45 != word[4]:
                color45 = 'y'
            if letter45 not in word:
                color45 = 'b'
            return flask.redirect('/fifth')
    
    
    
    return flask.render_template('index.html', first=False, second=False, third=False, fourth=True, fifth=False, sixth=False, second2=True, third3=True, fourth4=True,
                                 letter31=letter31, letter32=letter32, letter33=letter33, letter34=letter34, letter35=letter35
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5
                                 , letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                 color31=color31, color32=color32, color33=color33, color34=color34, color35=color35,)


@app.route('/fifth', methods=['GET', 'POST'])
def fifth():
    if flask.request.method == 'POST':
        global letter51
        global letter52
        global letter53
        global letter54
        global letter55
        global color51
        global color52
        global color53
        global color54
        global color55
        color51 = ''
        color52 = ''
        color53 = ''
        color54 = ''
        color55 = ''
        letter51 = flask.request.form['text1']
        letter52 = flask.request.form['text2']
        letter53 = flask.request.form['text3']
        letter54 = flask.request.form['text4']
        letter55 = flask.request.form['text5']
        if f'{letter31}{letter32}{letter33}{letter34}{letter35}' not in word_list:
            return flask.render_template('index.html', first=False, second=False, third=False, fourth=False, fifth=True, sixth=False, second2=True, third3=True, fourth4=True, fifth5=True,
                                 letter41=letter41, letter42=letter42, letter43=letter43, letter44=letter44, letter45=letter45
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5, 
                                 letter31=letter31, letter32=letter32, letter33=letter33, letter34=letter34, letter35=letter35
                                 , letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                 color31=color31, color32=color32, color33=color33, color34=color34, color35=color35,
                                 color41=color41, color42=color42, color43=color43, color44=color44, color45=color45,)
        else:
            if letter51 in word and letter51 == word[0]:
                color51 = 'g'
            if letter51 in word and letter51 != word[0]:
                color51 = 'y'
            if letter51 not in word:
                color51 = 'b'

            if letter52 in word and letter52 == word[1]:
                color52 = 'g'
            if letter52 in word and letter52 != word[1]:
                color52 = 'y'
            if letter52 not in word:
                color52 = 'b'

            if letter53 in word and letter53 == word[2]:
                color53 = 'g'
            if letter53 in word and letter53 != word[2]:
                color53 = 'y'
            if letter53 not in word:
                color53 = 'b'

            if letter54 in word and letter54 == word[3]:
                color54 = 'g'
            if letter54 in word and letter54 != word[3]:
                color54 = 'y'
            if letter54 not in word:
                color54 = 'b'

            if letter55 in word and letter55 == word[4]:
                color55 = 'g'
            if letter55 in word and letter55 != word[4]:
                color55 = 'y'
            if letter55 not in word:
                color55 = 'b'

            return flask.redirect('/sixth')

    return flask.render_template('index.html', first=False, second=False, third=False, fourth=False, fifth=True, sixth=False, second2=True, third3=True, fourth4=True, fifth5=True,
                                 letter41=letter41, letter42=letter42, letter43=letter43, letter44=letter44, letter45=letter45
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5, 
                                 letter31=letter31, letter32=letter32, letter33=letter33, letter34=letter34, letter35=letter35
                                 , letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                 color31=color31, color32=color32, color33=color33, color34=color34, color35=color35,
                                 color41=color41, color42=color42, color43=color43, color44=color44, color45=color45,)

@app.route('/sixth', methods=['GET', 'POST'])
def sixth():
    return flask.render_template('index.html', first=False, second=False, third=False, fourth=False, fifth=False, sixth=True, second2=True, third3=True, fourth4=True, fifth5=True, sixth6=True,
                                 letter51=letter51, letter52=letter52, letter53=letter53, letter54=letter54, letter55=letter55
                                 , letter11=letter1, letter12=letter2, letter13=letter3, letter14=letter4, letter15=letter5
                                 , letter41=letter41, letter42=letter42, letter43=letter43, letter44=letter44, letter45=letter45,
                                 letter31=letter31, letter32=letter32, letter33=letter33, letter34=letter34, letter35=letter35
                                 , letter21=letter21, letter22=letter22, letter23=letter23, letter24=letter24, letter25=letter25,
                                 color11=color1, color12=color2, color13=color3, color14=color4, color15=color5,
                                 color21=color21, color22=color22, color23=color23, color24=color24, color25=color25,
                                 color31=color31, color32=color32, color33=color33, color34=color34, color35=color35,
                                 color41=color41, color42=color42, color43=color43, color44=color44, color45=color45,
                                 color51=color51, color52=color52, color53=color53, color54=color54, color55=color55,)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)

