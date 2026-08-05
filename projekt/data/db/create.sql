DROP TABLE IF EXISTS changes;
DROP TABLE IF EXISTS notifications;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS categories;
DROP TABLE IF EXISTS suppliers;
DROP TABLE IF EXISTS address;

CREATE TABLE address (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    city VARCHAR(100) NOT NULL,
    street VARCHAR(120) NOT NULL,
    zip_code CHAR(6) CHECK (zip_code GLOB '[0-9][0-9]-[0-9][0-9][0-9]')
);

CREATE TABLE suppliers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    address_id INTEGER NOT NULL,
    phone CHAR(11) NOT NULL CHECK (phone GLOB '[0-9][0-9][0-9] [0-9][0-9][0-9] [0-9][0-9][0-9]'),
    email VARCHAR(255) NOT NULL CHECK (email GLOB '*?@??*.*?*'),
    FOREIGN KEY (address_id) REFERENCES address(id)
);

CREATE TABLE categories (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(25) NOT NULL
);

CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    code VARCHAR(50) UNIQUE NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    number NUMERIC(10, 2) NOT NULL,
    unit VARCHAR(25) NOT NULL,
    category_id INTEGER NOT NULL,
    supplier_id INTEGER NOT NULL,
    description TEXT,
    FOREIGN KEY (category_id) REFERENCES categories(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);

CREATE TABLE notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
  	date DATE NOT NULL,
  	time TIME NOT NULL,
  	status VARCHAR(30) NOT NULL,
    title VARCHAR(255) NOT NULL,
    description TEXT
);

CREATE TABLE archives (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER NOT NULL,
    number NUMERIC(10, 2) NOT NULL,
    supplier_id INTEGER NOT NULL,
    operation VARCHAR(20) NOT NULL,
    DATE DATE NOT NULL,
    TIME TIME NOT NULL,
    FOREIGN KEY (product_id) REFERENCES products(id),
    FOREIGN KEY (supplier_id) REFERENCES suppliers(id)
);