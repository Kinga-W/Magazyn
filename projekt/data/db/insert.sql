INSERT INTO address (id, city, street, zip_code) VALUES
(1, 'Warszawa', 'Marszałkowska 12/5', '00-124'),
(2, 'Kraków', 'Floriańska 45', '31-019'),
(3, 'Gdańsk', 'Długa 23/12', '80-828'),
(4, 'Wrocław', 'Oławska 67', '50-123'),
(5, 'Poznań', 'Święty Marcin 89/3', '61-809'),
(6, 'Łódź', 'Piotrkowska 102/7', '90-001'),
(7, 'Katowice', '3 Maja 34', '40-096'),
(8, 'Szczecin', 'Bohaterów Warszawy 56/9', '70-370');

INSERT INTO categories (id, name) VALUES
(1, 'Elektronika'),
(2, 'AGD'),
(3, 'Oprogramowanie'),
(4, 'Meble biurowe'),
(5, 'Artykuły papiernicze'),
(6, 'Akcesoria komputerowe'),
(7, 'Telefony'),
(8, 'TV i audio');

INSERT INTO suppliers (id, name, address_id, phone, email) VALUES
(1, 'TechCorp Polska', 1, '123 456 789', 'contact@techcorp.pl'),
(2, 'ElektroMax', 2, '234 567 890', 'info@elektromax.com'),
(3, 'OfficeWorld', 3, '345 678 901', 'office@officeworld.eu'),
(4, 'SoftTech Solutions', 4, '456 789 012', 'support@softtech.net'),
(5, 'HomeComfort', 5, '567 890 123', 'sales@homecomfort.com'),
(6, 'CompMaster', 6, '678 901 234', 'help@compmaster.pl'),
(7, 'MobileExpert', 7, '789 012 345', 'contact@mobileexpert.eu'),
(8, 'AudioVideo Pro', 8, '890 123 456', 'info@avpro.com');

INSERT INTO products (id, name, code, price, number, unit, category_id, supplier_id, description) VALUES
(1, 'Laptop HP Pavilion 15', '5901234567890', 3499.99, 15, 'sztuki', 1, 1, '15,6" FHD, i5-1135G7, 8GB RAM, 512GB SSD'),
(2, 'Smartfon Xiaomi Redmi Note 12', '5909876543210', 1299.00, 32, 'sztuki', 7, 2, '6.67" AMOLED, 6GB RAM, 128GB, 48MP'),
(3, 'Monitor Dell 27" P2722H', '5901122334455', 1399.00, 8, 'sztuki', 1, 3, 'IPS Full HD, HDMI/DP, pivot'),
(4, 'System Windows 11 Pro', '5905566778899', 799.00, 50, 'sztuki', 3, 4, 'OEM wersja 64-bit'),
(5, 'Krzesło biurowe ergonomiczne', '5903344556677', 599.00, 12, 'sztuki', 4, 5, 'Podłokietniki, regulacja wysokości'),
(6, 'Drukarka laserowa Brother HL-L2350DW', '5907788990011', 899.00, 6, 'sztuki', 1, 6, 'Duplex, WiFi, 30ppm'),
(7, 'Słuchawki bezprzewodowe JBL Tune 510BT', '5902233445566', 199.00, 25, 'sztuki', 8, 7, 'Bluetooth, 40mm, 30h playback'),
(8, 'Telewizor LG 55" OLED C2', '5906677889900', 5499.00, 5, 'sztuki', 8, 8, '4K HDR, Smart TV, HDMI 2.1'),
(9, 'Mikrofalówka Samsung ME83KR', '5904455667788', 699.00, 10, 'sztuki', 2, 2, '23L, 800W, grill'),
(10, 'Tablet Samsung Galaxy Tab S8', '5908899001122', 3499.00, 7, 'sztuki', 1, 2, '11" 120Hz, S Pen, 8GB RAM'),
(11, 'Klawiatura mechaniczna Logitech G Pro', '5903344556678', 499.00, 18, 'sztuki', 6, 6, 'Switch GX Blue, RGB'),
(12, 'Mysz gamingowa Razer DeathAdder V2', '5907788990012', 299.00, 22, 'sztuki', 6, 6, '20K DPI, 8 przycisków'),
(13, 'Router TP-Link Archer AX55', '5901122334456', 499.00, 9, 'sztuki', 1, 1, 'WiFi 6, 5 portów Gigabit'),
(14, 'Dysk SSD Samsung 1TB 980 Pro', '5905566778890', 599.00, 14, 'sztuki', 6, 2, 'PCIe 4.0 NVMe, 7000MB/s'),
(15, 'Smartwatch Huawei Watch GT 3', '5902233445567', 799.00, 11, 'sztuki', 1, 7, '46mm, 2 tyg. bateria, SpO2'),
(16, 'Lodówka Bosch KGN39VL35', '5906677889901', 3499.00, 4, 'sztuki', 2, 5, 'No Frost, 388L, klasa A++'),
(17, 'Kamera GoPro Hero 11 Black', '5904455667789', 2599.00, 3, 'sztuki', 1, 1, '5.3K60, HyperSmooth 5.0'),
(18, 'System macOS Ventura', '5908899001123', 699.00, 30, 'sztuki', 3, 4, 'Licencja na 1 komputer'),
(19, 'Głośnik JBL Charge 5', '5903344556679', 699.00, 8, 'sztuki', 8, 7, 'Bluetooth, waterproof, 20h play'),
(20, 'Biurko regulowane elektrycznie', '5907788990013', 1299.00, 5, 'sztuki', 4, 5, '140x70cm, pamięć pozycji');

INSERT INTO notifications (id, date, time, status, title, description) VALUES
(1, '2025-05-15', '08:30:00', 'przeczytane', 'Nowe dostawy', 'W przyszłym tygodniu spodziewamy się nowych dostaw laptopów i monitorów'),
(2, date('now'), time('now'), 'nowe', 'Promocje majowe', 'W maju obniżki na wybrane artykuły biurowe i elektronikę'),
(3, '2025-05-10', '14:15:00', 'przeczytane', 'Zmiana godzin pracy', 'W czerwcu magazyn będzie czynny w godzinach 7:00-19:00'),
(4, date('now'), time('now'), 'nowe', 'Aktualizacja systemu', 'W nocy z 20 na 21 maja planowana jest aktualizacja systemu magazynowego');

INSERT INTO archives (id, product_id, number, supplier_id, operation, date, time) VALUES
-- Dostawy (number > 0)
(1, 1, 10, 1, 'dostawa', '2025-05-01', '09:15:00'),
(2, 3, 8, 3, 'dostawa', '2025-05-03', '11:20:00'),
(3, 4, 20, 4, 'dostawa', '2025-05-04', '10:00:00'),
(4, 6, 6, 6, 'dostawa', '2025-05-06', '13:10:00'),
(5, 7, 15, 7, 'dostawa', '2025-05-07', '09:30:00'),
(6, 9, 10, 2, 'dostawa', '2025-05-09', '10:45:00'),
(7, 10, 7, 2, 'dostawa', '2025-05-10', '11:30:00'),
(8, 12, 10, 6, 'dostawa', '2025-05-12', '09:00:00'),
(9, 13, 5, 1, 'dostawa', '2025-05-13', '12:30:00'),
(10, 15, 8, 7, 'dostawa', '2025-05-15', '10:20:00'),
-- Wydania (number < 0)
(11, 2, -5, 2, 'wydanie', '2025-05-02', '14:30:00'),
(12, 5, -2, 5, 'wydanie', '2025-05-05', '16:45:00'),
(13, 8, -1, 8, 'wydanie', '2025-05-08', '15:20:00'),
(14, 11, -3, 6, 'wydanie', '2025-05-11', '14:15:00'),
(15, 14, -4, 2, 'wydanie', '2025-05-14', '16:00:00');
