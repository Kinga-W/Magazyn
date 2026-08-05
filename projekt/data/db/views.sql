DROP VIEW IF EXISTS products_table;
CREATE VIEW products_table AS
SELECT pr.id, pr.name, code, price, number, unit, cg.nazwa category, sp.name supplier, description FROM products pr
JOIN categories cg ON cg.id = pr.category_id
JOIN suppliers sp ON sp.id = pr.supplier_id
ORDER BY pr.id;

DROP VIEW IF EXISTS change_history;
CREATE VIEW change_history AS
SELECT date, time, pr.name product_name, ch.number, operation, sp.name supplier FROM changes ch
JOIN products pr ON pr.id = ch.product_id
JOIN suppliers sp ON sp.id = ch.supplier_id
ORDER BY date, time;