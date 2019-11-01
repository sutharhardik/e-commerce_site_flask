from flask import *
from project import app
from project.com.dao.SubcategoryDAO import SubcategoryDAO
from project.com.vo.SubcategoryVO import SubcategoryVO
from project.com.dao.CategoryDAO import CategoryDAO
from project.com.vo.CategoryVO import CategoryVO

@app.route("/loadsubcategory")
def loadSubcategory():
    try:
        if session['loginDictrole'] == 'admin':
            categoryDAO=CategoryDAO()
            categoryDict=categoryDAO.searchCategory()
            print(categoryDict)
            return render_template('admin/addSubcategory.html',categoryDict=categoryDict)

        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('Login'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('Login'))


@app.route("/insertsubcategory",methods=["POST"])
def insertSubcategory():
    subcategoryVO=SubcategoryVO()
    subcategoryDAO=SubcategoryDAO()
    categoryVO = CategoryVO()
    categoryDAO = CategoryDAO()
    subcategoryVO.subcategoryName=request.form['subcategoryName']
    subcategoryVO.subcategoryDescription=request.form['subcategoryDescription']
    subcategoryVO.subcategoryActiveStatus="active"
    print (request.form["categoryId"])
    subcategoryVO.subcategory_categoryId = request.form['categoryId']
    subcategoryDAO.insertSubcategory(subcategoryVO)
    return redirect("/viewsubcategory")

@app.route('/viewsubcategory')
def viewSubcategory():

    subcategoryDAO=SubcategoryDAO()

    data1=subcategoryDAO.searchSubcategory()
    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewsubcategory.html',data2 = data1)
        elif session['loginDictrole'] == 'seller':
            return render_template('seller/viewsubcategory.html',data2 = data1)

    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))




@app.route('/deletesubcategory',methods=['post'])
def deleteSubcategory():

    subcategoryVO=SubcategoryVO()
    subcategoryDAO=SubcategoryDAO()

    subcategoryVO.subcategoryId=request.form['subcategoryId']

    subcategoryDAO.deleteSubcategory(subcategoryVO)

    return redirect('/viewsubcategory')

