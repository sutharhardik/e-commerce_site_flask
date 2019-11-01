from flask import *
from project import app
from project.com.dao.ProductDAO import ProductDAO
from project.com.vo.ProductVO import ProductVO
from project.com.dao.CategoryDAO import CategoryDAO
from project.com.dao.SubcategoryDAO import SubcategoryDAO
from project.com.vo.SubcategoryVO import SubcategoryVO
from werkzeug.utils import secure_filename
import os


@app.route("/loadproduct")
def loadproduct():
    try:
        if session['loginDictrole'] == 'seller':
            categoryDAO=CategoryDAO()
            categoryDict=categoryDAO.searchCategory()


            subcategoryDAO = SubcategoryDAO()
            subcategoryDict = subcategoryDAO.searchSubcategory()

            return render_template('seller/addproduct.html',categoryDict=categoryDict)

        else:
            flash('Plese Login First ! ', 'danger')
            return redirect(url_for('Login'))
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('Login'))

@app.route("/ajaxSubcategoryProduct")
def ajaxSubcategoryProduct():
    subcategoryVO=SubcategoryVO()
    subcategoryDAO=SubcategoryDAO()

    subcategory_categoryId=request.args.get('product_categoryId')

    subcategoryVO.subcategory_categoryId = subcategory_categoryId

    ajaxSubcategoryProductDict = subcategoryDAO.ajaxSubcategoryProduct(subcategoryVO)

    print(ajaxSubcategoryProductDict)

    jsn=json.dumps(ajaxSubcategoryProductDict)

    return jsn


@app.route('/insertproduct',methods=["POST"])
def insertproduct():


    productVO=ProductVO()
    productDAO=ProductDAO()

    UPLOAD_FOLDER = r'C:\Users\RetailAdmin\PycharmProjects\hardik\project\static\adminResources\dataset'

    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    file = request.files['file']
    print(file)

    filename = secure_filename(file.filename)
    print(filename)

    filepath = os.path.join(app.config['UPLOAD_FOLDER'])
    print(filepath)

    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

    ProductVO.productpath = filepath

    productVO.product_registerId=session['loginDictId']

    print(productVO.product_registerId)

    productVO.productName=request.form["productName"]
    print(productVO.productName)

    productVO.productPrize=request.form["productPrize"]

    productVO.productDescription=request.form["productDescription"]

    productVO.productQuantity=request.form["productQuantity"]

    ProductVO.productImageName = filename

    productVO.productActiveStatus='active'

    productVO.product_categoryId = request.form['categoryId']

    print(productVO.product_categoryId)

    productVO.product_subcategoryId = request.form['subcategoryId']

    print(productVO.product_subcategoryId)

    productDAO.insertProduct(productVO)

    return redirect("/viewproduct")


@app.route('/viewproduct')
def viewProduct():

    productDAO=ProductDAO()

    data1=productDAO.search_Product()
    #data=productDAO.search_Product()
    try:
        if session['loginDictrole'] == 'admin':
            return render_template('admin/viewproduct.html', data2=data1)
        elif session['loginDictrole'] == 'seller':
            return render_template("seller/viewproduct.html", data2=data1)
    except:
        flash('Plese Login First !', 'danger')
        return redirect(url_for('Login'))



@app.route('/deleteproduct',methods=['post'])
def deleteProduct():

    productVO=ProductVO()
    productDAO=ProductDAO()

    productVO.productId=request.form['productId']

    productDAO.deleteProduct(productVO)

    return redirect('/viewproduct')


