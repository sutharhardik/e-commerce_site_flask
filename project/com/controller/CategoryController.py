from flask import *
from project import app
from project.com.dao.CategoryDAO import CategoryDAO
from project.com.vo.CategoryVO import CategoryVO

@app.route("/loadcategory")
def loadCategory():
    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/addCategory.html')
        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('Login'))
    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))


@app.route("/insertcategory",methods=["POST"])
def insertCategory():
    categoryVO=CategoryVO()
    categoryDAO=CategoryDAO()

    categoryVO.categoryName=request.form["categoryName"]
    categoryVO.categoryDescription=request.form["categoryDescription"]
    categoryVO.categoryActiveStatus="active"

    categoryDAO.insertCategory(categoryVO)
    return redirect("viewcategory")

@app.route('/viewcategory')
def viewCategory():

    categoryDAO=CategoryDAO()

    data1=categoryDAO.searchCategory()

    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewcategory.html',data2 = data1)
        elif session['loginDictrole'] == 'seller':
            return render_template("seller/viewcategory.html",data2 = data1)
    except:
            flash('Plese Login First !', 'danger')
            return redirect(url_for('Login'))


@app.route('/deletecategory',methods=['post'])
def deleteCategory():

    categoryVO=CategoryVO()
    categoryDAO=CategoryDAO()

    categoryVO.categoryId=request.form['categoryId']

    categoryDAO.deleteCategory(categoryVO)

    return redirect('/viewcategory')
