#################################################
## SALTPAY 2021 - Network TEAM - NIVALDO RAMOS ##
#################################################

from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime, timedelta
from flask_sqlalchemy import SQLAlchemy
import datetime

# DATABASE CONNECTION
app = Flask(__name__)
app.secret_key = "saltpay@2021"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://nivaldo:@localhost/elr'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Database Select for FORMS and DROP DOWN MENUS
# PFS
class pfs(db.Model):
    pfs_id = db.Column(db.Integer, primary_key=True)
    pfs_value = db.Column(db.String(30))
    def __init__(self, pfs_id,pfs_value):
        self.pfs_id = pfs_id
        self.pfs_value = pfs_value
#  ---> END <----

# AUTHENTICATION_ALGORITHM
class auth_list(db.Model):
    auth_id = db.Column(db.Integer, primary_key=True)
    auth_al = db.Column(db.String(30))
    def __init__(self, auth_id,auth_al):
        self.auth_id = auth_id
        self.auth_al = auth_al

#  ---> END <----

# ENCRYPTION ALGORITHM
class p1_encrypt_list(db.Model):
    p1_encryption_id = db.Column(db.Integer, primary_key=True)
    p1_encryption = db.Column(db.String(30))
    def __init__(self, p1_encryption_id,p1_encryption):
        self.p1_encryption_id = p1_encryption_id
        self.p1_encryption = p1_encryption
#  ---> END <----

# STATUS
class status_list(db.Model):
    status_id = db.Column(db.Integer, primary_key=True)
    type_status = db.Column(db.String(30))
    def __init__(self, status_id,type_status):
        self.status_id = status_id
        self.type_status = type_status
#  ---> END <----

# Database model for ELR
class ELR(db.Model):
    requestid = db.Column(db.Integer, primary_key=True)
    req_type = db.Column(db.String(100))
    firewall = db.Column(db.String(100))
    virtualsys = db.Column(db.String(100))
    status = db.Column(db.String(100))
    project = db.Column(db.String(100))
    req_name = db.Column(db.String(100))
    req_mail = db.Column(db.String(100))
    req_phone = db.Column(db.String(100))
    req_team = db.Column(db.String(100))
    company = db.Column(db.String(100))
    c_address = db.Column(db.String(100))
    c_city = db.Column(db.String(100))
    c_country = db.Column(db.String(100))
    c_name = db.Column(db.String(100))
    c_mail = db.Column(db.String(100))
    c_phone = db.Column(db.String(100))
    t_name = db.Column(db.String(100))
    t_mail = db.Column(db.String(100))
    t_phone = db.Column(db.String(100))
    t2_name = db.Column(db.String(100))
    t2_mail = db.Column(db.String(100))
    t2_phone = db.Column(db.String(100))
    justification = db.Column(db.String(100))
    saltpayservice = db.Column(db.String(100))
    r_devicemake = db.Column(db.String(100))
    r_peer = db.Column(db.String(100))
    r_network = db.Column(db.String(100))
    nat = db.Column(db.String(100))
    p1_algo = db.Column(db.String(100))
    p1_hash = db.Column(db.String(100))
    p1_pfs = db.Column(db.String(100))
    p1_lifetime = db.Column(db.String(100))
    p2_algo = db.Column(db.String(100))
    p2_hash = db.Column(db.String(100))
    p2_pfs = db.Column(db.String(100))
    p2_lifetime = db.Column(db.String(100))
    req_date = db.Column(db.DateTime, default=datetime.datetime.utcnow)

    def __init__(self, req_type, firewall, virtualsys, status, project, req_name, req_mail, req_phone,
                 req_team, company, c_address, c_city, c_country, c_name, c_mail, c_phone, t_name, t_mail, t_phone,
                 t2_name, t2_mail, t2_phone, justification, saltpayservice, r_devicemake, r_peer, r_network, nat,
                 p1_algo, p1_hash, p1_pfs, p1_lifetime, p2_algo, p2_hash, p2_pfs, p2_lifetime):
        self.req_type = req_type
        self.firewall = firewall
        self.virtualsys = virtualsys
        self.status = status
        self.project = project
        self.req_name = req_name
        self.req_mail = req_mail
        self.req_phone = req_phone
        self.req_team = req_team
        self.company = company
        self.c_address = c_address
        self.c_city = c_city
        self.c_country = c_country
        self.c_name = c_name
        self.c_mail = c_mail
        self.c_phone = c_phone
        self.t_name = t_name
        self.t_mail = t_mail
        self.t_phone = t_phone
        self.t2_name = t2_name
        self.t2_mail = t2_mail
        self.t2_phone = t2_phone
        self.justification = justification
        self.saltpayservice = saltpayservice
        self.r_devicemake = r_devicemake
        self.r_peer = r_peer
        self.r_network = r_network
        self.nat = nat
        self.p1_algo = p1_algo
        self.p1_hash = p1_hash
        self.p1_pfs = p1_pfs
        self.p1_lifetime = p1_lifetime
        self.p2_algo = p2_algo
        self.p2_hash = p2_hash
        self.p2_pfs = p2_pfs
        self.p2_lifetime = p2_lifetime

#ROUTE TO MAIN DASHBOARD

@app.route('/')
def Index():
    all_data = ELR.query.all()
    status_list_data = status_list.query.all()
    phase1_crypto = p1_encrypt_list.query.all()
    auth_list_data = auth_list.query.all()
    pfs_list_data = pfs.query.all()
    return render_template("index.html", linkrequest=all_data, status_list=status_list_data, p1_encrypt_list_data=phase1_crypto, auth_list_=auth_list_data, pfs_list_=pfs_list_data)
#  ---> END <----

#ROUTE TO CREATE ENTRY
@app.route('/insert', methods=['POST'])
def insert():
    if request.method == 'POST':
        req_type = request.form['req_type']
        firewall = request.form['firewall']
        virtualsys = request.form['virtualsys']
        status = request.form['status']
        project = request.form['project']
        req_name = request.form['req_name']
        req_mail = request.form['req_mail']
        req_phone = request.form['req_phone']
        req_team = request.form['req_team']
        company = request.form['company']
        c_address = request.form['c_address']
        c_city = request.form['c_city']
        c_country = request.form['c_country']
        c_name = request.form['c_name']
        c_mail = request.form['c_mail']
        c_phone = request.form['c_phone']
        t_name = request.form['t_name']
        t_mail = request.form['t_mail']
        t_phone = request.form['t_phone']
        t2_name = request.form['t2_name']
        t2_mail = request.form['t2_mail']
        t2_phone = request.form['t2_phone']
        justification = request.form['justification']
        saltpayservice = request.form['saltpayservice']
        r_devicemake = request.form['r_devicemake']
        r_peer = request.form['r_peer']
        r_network = request.form['r_network']
        nat = request.form['nat']
        p1_algo = request.form['p1_algo']
        p1_hash = request.form['p1_hash']
        p1_pfs = request.form['p1_pfs']
        p1_lifetime = request.form['p1_lifetime']
        p2_algo = request.form['p2_algo']
        p2_hash = request.form['p2_hash']
        p2_pfs = request.form['p2_pfs']
        p2_lifetime = request.form['p2_lifetime']

        my_data = ELR(req_type, firewall, virtualsys, status, project, req_name, req_mail, req_phone,
                      req_team, company, c_address, c_city, c_country, c_name, c_mail, c_phone, t_name, t_mail, t_phone,
                      t2_name, t2_mail, t2_phone, justification, saltpayservice, r_devicemake, r_peer, r_network, nat,
                      p1_algo, p1_hash, p1_pfs, p1_lifetime, p2_algo, p2_hash, p2_pfs, p2_lifetime)
        db.session.add(my_data)
        db.session.commit()


        flash("ELR Requested Successfully")

        return redirect(url_for('Index'))
#  ---> END <----

# ROUTE TO UPDATE REGISTERS
@app.route('/update', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        my_data = ELR.query.get(request.form.get('requestid'))
        my_data.req_type = request.form['req_type']
        my_data.firewall = request.form['firewall']
        my_data.status = request.form['status']
        my_data.project = request.form['project']
        my_data.req_name = request.form['req_name']
        my_data.req_mail = request.form['req_mail']
        my_data.req_phone = request.form['req_phone']
        my_data.req_team = request.form['req_team']
        my_data.company = request.form['company']
        my_data.c_address = request.form['c_address']
        my_data.c_city = request.form['c_city']
        my_data.c_country = request.form['c_country']
        my_data.c_name = request.form['c_name']
        my_data.c_mail = request.form['c_mail']
        my_data.c_phone = request.form['c_phone']
        my_data.t_name = request.form['t_name']
        my_data.t_mail = request.form['t_mail']
        my_data.t_phone = request.form['t_phone']
        my_data.t2_name = request.form['t2_name']
        my_data.t2_mail = request.form['t2_mail']
        my_data.t2_phone = request.form['t2_phone']
        my_data.justification = request.form['justification']
        my_data.saltpayservice = request.form['saltpayservice']
        my_data.r_devicemake = request.form['r_devicemake']
        my_data.r_peer = request.form['r_peer']
        my_data.r_network = request.form['r_network']
        my_data.nat = request.form['nat']
        my_data.p1_algo = request.form['p1_algo']
        my_data.p1_hash = request.form['p1_hash']
        my_data.p1_pfs = request.form['p1_pfs']
        my_data.p1_lifetime = request.form['p1_lifetime']
        my_data.p2_algo = request.form['p2_algo']
        my_data.p2_hash = request.form['p2_hash']
        my_data.p2_pfs = request.form['p2_pfs']
        my_data.p2_lifetime = request.form['p2_lifetime']

        db.session.commit()
        flash("Request Updated Successfully")

        return redirect(url_for('Index'))
#  ---> END <---- ROUTE TO UPDATE REGISTERS


# ROUTE TO DELETE REGISTER
@app.route('/delete/<requestid>/', methods=['GET', 'POST'])
def delete(requestid):
    my_data = ELR.query.get(requestid)
    db.session.delete(my_data)
    db.session.commit()
    flash("Request Deleted Successfully")

    return redirect(url_for('Index'))
# #  ---> END <---- ROUTE TO DELETE REGISTER

if __name__ == "__main__":
    app.run(debug=True)
