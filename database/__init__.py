from pymongo import MongoClient

# สร้าง Connection
con = MongoClient("localhost", 27017)

# เชื่อมต่อกับฐานข้อมูลชื่อ company
db = con.get_database("company")

# # สร้าง Collection ชื่อ employees
# emyployee_obj = emyployee_db.employees
