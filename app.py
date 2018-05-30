from flask import Flask, session, redirect, url_for, escape, request, render_template, flash

app = Flask(__name__, template_folder='template')

# Set a secret key fo some rando bytes. Keep this really secret!
app.secret_key = b'm\x9c\xbf`\x8c\x946\x0c\xf2\xde\xec\xc8\xa6\xdfO\xe8'

#index route
@app.route('/')
def index():
    if 'username' in session:
        #return 'Logged in as %s' % escape(session['username'])
        flash('You were successfully logged in.', 'info')
        return render_template('index.html', name=session['username'])
    flash('You are not logged in.', 'error')
    return redirect(url_for('logout'))

#login route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'username' in session:
        return redirect(url_for('index'))#redirect the user to index page
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'CaioIbraim'  or request.form['password'] != 'secret' :
            error = 'Invalide credentials'
        else:
                session['username'] = request.form['username']
                return redirect(url_for('index'))
    return render_template('login.html', error=error)

#logout route
@app.route('/logout')
def logout():
    #remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('login'))

# error route
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Roda a aplicacao em: http://localhost:8085
app.run(debug=True,port=8085)
