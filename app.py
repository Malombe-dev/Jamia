from flask import*
import pymysql
app = Flask (__name__)

@app.route('/')
def homepage():
#  connect to db
    connection = pymysql.connect(host='localhost', user='root', password='', database='Jamia LTD')
    sql =  " select * from products where product_category = 'phones' " 
    sql1 =  " select * from products where product_category = 'Electronics' " 
    sql2 =  " select * from products where product_category = 'Makeup' " 
    sql3 =  " select * from products where product_category = 'Footwear' " 
    sql4 =  " select * from products where product_category = 'clothes' " 
    sql5 =  " select * from products where product_category = 'shoes' " 
    # you need to have a cursor 
    # used to excecute above sql 
    cursor = connection.cursor() 
    cursor1 = connection.cursor() 
    cursor2 = connection.cursor() 
    cursor3 = connection.cursor() 
    cursor4 = connection.cursor() 
    cursor5 = connection.cursor() 
    # excecute
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    cursor4.execute(sql4)
    cursor5.execute(sql5)
    # fetchall the p[hones rows]
    phones = cursor.fetchall()
    # FETCH ELECTRONICS 
    Electronics = cursor1.fetchall()
    # fetch make up
    Makeup = cursor2.fetchall()
    # fetch footware 
    Footwear = cursor3.fetchall()
    # fetch clothes 
    clothes = cursor4.fetchall()
    # fetch shoes
    shoes = cursor5.fetchall()



    return render_template('index.html',phones = phones, Electronics = Electronics , Makeup = Makeup, Footwear = Footwear , clothes = clothes , shoes = shoes)
# route  for a sinle item


@app.route('/single/<product_id>')
def  single(product_id):

    # conection to db
    connection = pymysql.connect(host='localhost', user='root', password='', database='Jamia LTD')

    # create sql query %s= place holder
    sql = "select* from products where product_id = %s  "
    # create cursor 

    cursor = connection.cursor()
    # excecute cursor 
    cursor.execute(sql ,product_id)
    # get single product
    product = cursor.fetchone()


    return render_template ("single.html" , product = product)

# upload products route

@app.route("/upload", methods = ['POST' , 'GET'])
def upload ():
    if request.method == 'POST': 
        # user can add the product 
       product_name = request.form ['product_name']
       product_desc = request.form ['product_desc']
       product_cost = request.form ['product_cost']
       product_category = request.form ['product_category']
       product_image_name = request.files ['product_image_name']
    #    fetchfile
       product_image_name.save('static/images/' + product_image_name.filename)
    #    connect to db
       connection = pymysql.connect(host='localhost', user='root', password='', database='Jamia LTD')
    #    create a cursor 
       cursor = connection.cursor()
       sql = "insert into products (Product_name, product_desc,product_cost, product_category,product_image_name) values (%s, %s, %s,%s,%s)"

       data = (product_name,product_desc,product_cost,product_category,product_image_name.filename)
    #    excecute 
       cursor.execute(sql, data)
    #    save changes 
       connection.commit()
    

       return render_template ('/upload.html', message = "Product added successfully")
    else:
      return render_template ('/upload.html' , error = "Please add a product")


#  fashio Route 
    # helps you to see all the fasghions 
@app.route ('/fashion')
def fashion():
        #  connect to db
    connection = pymysql.connect(host='localhost', user='root', password='', database='Jamia LTD')
    sql =  " select * from products where product_category = 'dresses' " 
    sql1 =  " select * from products where product_category = 'handbags' " 
    sql2 =  " select * from products where product_category = 'belt' " 
    sql3 =  " select * from products where product_category = 'cap' " 
    sql4 =  " select * from products where product_category = 'socks' " 

    # you need to have a cursor 
    # used to excecute above sql 
    cursor = connection.cursor() 
    cursor1 = connection.cursor() 
    cursor2 = connection.cursor() 
    cursor3 = connection.cursor() 
    cursor4 = connection.cursor() 
   
    # excecute
    cursor.execute(sql)
    cursor1.execute(sql1)
    cursor2.execute(sql2)
    cursor3.execute(sql3)
    cursor4.execute(sql4)
   

    dresses = cursor.fetchall()
 
    handbags = cursor1.fetchall()

    belt = cursor2.fetchall()

    cap = cursor3.fetchall()

    socks = cursor4.fetchall()

        

    return render_template ('fashion.html', dresses = dresses, handbags = handbags, belt  = belt, cap = cap, socks = socks)

# upload fashion 
@app.route("/uploadfashion", methods = ['POST' , 'GET'])
def uploadfashion ():
    if request.method == 'POST': 
        # user can add the product 
       product_name = request.form ['product_name']
       product_desc = request.form ['product_desc']
       product_cost = request.form ['product_cost']
       product_category = request.form ['product_category']
       product_image_name = request.files ['product_image_name']
    #    fetchfile
       product_image_name.save('static/images/' + product_image_name.filename)
    #    connect to db
       connection = pymysql.connect(host='localhost', user='root', password='', database='Jamia LTD')
    #    create a cursor 
       cursor = connection.cursor()
       sql = "insert into products (Product_name, product_desc,product_cost, product_category,product_image_name) values (%s, %s, %s,%s,%s)"

       data = (product_name,product_desc,product_cost,product_category,product_image_name.filename)
    #    excecute 
       cursor.execute(sql, data)
    #    save changes 
       connection.commit()
    

       return render_template ('/uploadfashion.html', message = "Fashion added successfully")
    else:
      return render_template ('/uploadfashion.html' , error = "Please add a Fashion")

# user registration
    
@app.route('/about')
def About():
    return "this is about page "


@app.route('/register')
def Register ():
    return " this is register page "

@app.route('/login')
def Login():
    return "login page"

@app.route('/logout')
def Logout():
    return "logout page"

if __name__ == '__main__':
    app.run(debug=True,port= 3000)