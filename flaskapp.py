from flask import Flask, flash, redirect, render_template, request, session, abort
import ibm_db_dbi as dbi
from ibm_db_dbi import SQL_ATTR_DBC_SYS_NAMING, SQL_TRUE
from ibm_db_dbi import SQL_ATTR_TXN_ISOLATION, SQL_TXN_NO_COMMIT

app = Flask(__name__)

options = {
SQL_ATTR_TXN_ISOLATION: SQL_TXN_NO_COMMIT,
SQL_ATTR_DBC_SYS_NAMING: SQL_TRUE,
}
conn = dbi.connect()
conn.set_option(options)

@app.route("/")
def hello():

    cur = conn.cursor()
    query = "select * from pgfiles.supplies where supply_brand = ?"
    name = "BIC"
    cur.execute(query, (name,))


    #for row in cur:
    #    print(row[2])

    d = cur.description
    print(d[0][0])

    name = request.args.get('username')
    link = request.args.get('urllink')
    print(link)
    return render_template('index.html', name=name, rows=cur)
    #return render_template('index.html', link = link)

@app.route('/addSupply',methods=['POST'])
def add_supply():
    if not 'user' in session:
        return redirect("/login")
    else:
        cur = conn.cursor()
        sql = """INSERT INTO PGFILES.SUPPLIES (supply_brand, supply_type)
        values(?, ?)
        """

        # read the posted values from the UI
        supply_name = request.form['supply_name']
        supply_brand = request.form['supply_brand']
        supply_type = request.form['supply_type']
        in_stock = request.form['in_stock']

        errors = {}
        if supply_name == '':
            errors['supply_name'] = 'Please enter a value for supply name'
        if supply_brand == '':
            errors['supply_brand'] = 'Please enter a value for brand'

        sql = "select * from pgfiles.supplyty where supply_type = ?"
        cur.execute(sql, (supply_type,))


        #if in_stock == '':
        #    errors['supply_type'] = 'Error: must determine in stock or not'


        if not errors:
            #return 'Name: ' + supply_name + ' Brand: ' + supply_brand + ' Supply Type: ' + supply_type + ' In Stock: ' + in_stock
            #cur.execute(sql, (supply_brand, supply_type))
            #return 'Name: ' + supply_name + ' Brand: ' + supply_brand
            return render_template('formAddSupply.html', supply_types=cur)
        else:
            return render_template('formAddSupply.html', errors=errors)


@app.route("/user/<username>")
def show_user_profile ( username ):
    # show the user profile for that user

    #name = "Karen Austin"
    return render_template('index.html', name=name)
    #return 'User %s' % username

@app.route ( '/user/<urlparameter>' )
def what_does_this_do ( urlparameter ):
# What is this route supposed to do???????
    return render_template('template1.html', information=urlparameter)

@app.route("/formAddSupply")
def formAddSupply():
    if not 'user' in session:
        return redirect("/login")
    else:
    # read the posted values from the UI
        cur = conn.cursor()
        sql = "select * from pgfiles.supplyty"
        cur.execute(sql)

        return render_template('formAddSupply.html', supply_types=cur)
        #return render_template('index2.html')


@app.route ( '/login' , methods =[ 'GET' , 'POST' ])
def login():


    if request.method == 'POST' :
        username = request.form[ 'username' ]
        password = request.form[ 'password' ]
        session['user'] = username
        #return redirect( "/formAddSupply" )

        try:
            oconn = dbi.connect(user=username, password=password)
        except:
            return render_template('login.html')


        return redirect("/hello")
    else :
        return render_template( 'login.html' )

@app.route('/logout')
def logout():
    session.pop('user', None)
    session.clear()
    return redirect("/login")

if __name__ == "__main__":
    app.secret_key = 'cutcokey'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=False,host='0.0.0.0',port=9113) #where xxxx is your port number