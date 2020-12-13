from flask import Flask,request,abort
import json
import mysql.connector

app = Flask(__name__)

mydb = mysql.connector.connect(user='anonymous',
                          host='ensembldb.ensembl.org',
                          database='ensembl_website_97')

mycur = mydb.cursor()

@app.route('/genes/<lookup>',defaults={'species': None}, methods=['GET'])
@app.route('/genes/<lookup>/<species>', methods=['GET'])
def get_genes(lookup, species):

    if (len(lookup) < 3 ):
        abort(400)
    
    if species:
        sqlStr = "SELECT display_label,location,stable_id,species FROM gene_autocomplete where display_label like '%" + lookup + "%' and species = '"+species+"' limit 3"
    else:
        sqlStr = "SELECT display_label,location,stable_id,species FROM gene_autocomplete where display_label like '%" + lookup + "%' limit 3"
    
    mycur.execute(sqlStr)
    rs = mycur.fetchall()
    res = []

    for row in rs:
        rowDict = {}
        rowDict["Gene Name"]=row[0]
        rowDict["Location"]=row[1]
        rowDict["Ensembl stable ID"]=row[2]
        rowDict["Species"]=row[3]
        res.append(rowDict)

    return json.dumps(res)

@app.route('/genes', methods=['POST','PUT','PATCH'])
def post_genes():
    abort(405)


if __name__ == '__main__':
    app.run()

