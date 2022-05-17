from database import con


# เชื่อมต่อกับฐานข้อมูลชื่อ company
db = con.get_database("company")

# สร้าง Collection ชื่อ employees
emyployee_obj = db.employees
