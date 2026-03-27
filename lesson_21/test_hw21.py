def test_shop_database(cursor_con):
    cursor, conn = cursor_con

    cursor.execute("""CREATE TABLE categories (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL);""")

    cursor.execute("""CREATE TABLE products (id SERIAL PRIMARY KEY, name VARCHAR(100) NOT NULL, description TEXT, price DECIMAL(10, 2), category_id INTEGER);""")

    cursor.execute("""INSERT INTO categories (name) VALUES ('Electronics'), ('Food');""")

    cursor.execute("""INSERT INTO products (name, description, price, category_id) VALUES 
        ('asus rog strix g18', 'Laptop 17-inch', 900, 1),
        ('sony wh-1000xm5', 'Wireless headphones', 246.90, 1),
        ('protein bar', 'Such easy 35grams of protein', 2.49, 2);""")

    conn.commit()

    cursor.execute("""SELECT p.name, p.description, p.price, c.name AS category_name FROM products p JOIN categories c ON p.category_id = c.id;""")

    results = cursor.fetchall()
    for row in results:
        print(f"Products: {row[0]} | Description: {row[1]} | Price: {row[2]} | Category: {row[3]}")