-- Clear existing data (optional: uncomment if you want to reset)
-- TRUNCATE TABLE products RESTART IDENTITY CASCADE;
-- TRUNCATE TABLE categories RESTART IDENTITY CASCADE;

-- Insert 15 categories
INSERT INTO categories (name, description, sort_order, is_active)
VALUES
('Electronics', 'Electronic gadgets and devices', 1, 1),
('Home Appliances', 'Appliances for household use', 2, 1),
('Furniture', 'Home and office furniture', 3, 1),
('Books', 'Educational and entertainment books', 4, 1),
('Fashion', 'Clothing and accessories', 5, 1),
('Toys', 'Toys and games for kids', 6, 1),
('Sports', 'Sports and fitness equipment', 7, 1),
('Groceries', 'Daily household groceries', 8, 1),
('Beauty', 'Beauty and personal care items', 9, 1),
('Automobile', 'Car and bike accessories', 10, 1),
('Stationery', 'Office and school stationery', 11, 1),
('Garden', 'Gardening and outdoor tools', 12, 1),
('Pets', 'Pet food and accessories', 13, 1),
('Music', 'Musical instruments and gear', 14, 1),
('Healthcare', 'Medical and wellness products', 15, 1);

-- Insert 100 products (approx. 6–8 per category)
INSERT INTO products (name, description, category, price, quantity)
VALUES
('Smartphone X1', 'High-performance smartphone with OLED display', 1, 49999, 30),
('Laptop Pro 15', 'Lightweight laptop for professionals', 1, 89999, 15),
('Bluetooth Headphones', 'Noise-cancelling over-ear headphones', 1, 7999, 50),
('Smartwatch Z', 'Fitness smartwatch with GPS', 1, 10999, 40),
('Portable Speaker', 'Waterproof Bluetooth speaker', 1, 4999, 60),

('Air Conditioner 1.5T', 'Energy-efficient split AC', 2, 35999, 10),
('Washing Machine 7kg', 'Fully automatic washing machine', 2, 24999, 8),
('Microwave Oven', 'Convection microwave with grill', 2, 15999, 12),
('Refrigerator 260L', 'Double-door frost-free fridge', 2, 27999, 9),
('Vacuum Cleaner', 'High suction power vacuum cleaner', 2, 8999, 20),

('Office Chair', 'Ergonomic mesh office chair', 3, 8999, 25),
('Wooden Table', 'Solid oak dining table', 3, 15999, 10),
('Bookshelf 5-Tier', 'Compact bookshelf for home use', 3, 4999, 18),
('Sofa Set 3+1+1', 'Comfortable living room sofa set', 3, 45999, 5),
('Bed Queen Size', 'Queen-sized bed with storage', 3, 25999, 7),

('Novel - The Great Escape', 'Thrilling adventure novel', 4, 399, 120),
('Programming in Python', 'Comprehensive guide to Python', 4, 699, 80),
('History of India', 'Detailed account of Indian history', 4, 599, 100),
('Kids Story Book', 'Collection of bedtime stories', 4, 299, 150),
('Science Encyclopedia', 'Knowledge book for students', 4, 999, 60),

('Mens Cotton Shirt', 'Slim-fit casual shirt', 5, 1299, 200),
('Women Denim Jeans', 'Stretchable blue denim jeans', 5, 1599, 150),
('Leather Wallet', 'Classic brown leather wallet', 5, 899, 100),
('Sneakers White', 'Comfortable casual sneakers', 5, 2499, 120),
('Women Kurti', 'Ethnic wear for women', 5, 1299, 100),

('Building Blocks Set', '100-piece creative blocks', 6, 499, 200),
('Remote Car', 'Rechargeable toy car', 6, 899, 150),
('Puzzle Game', '500-piece jigsaw puzzle', 6, 599, 180),
('Soft Teddy Bear', 'Cuddly plush toy', 6, 799, 100),
('Board Game', 'Classic strategy board game', 6, 999, 120),

('Cricket Bat', 'Professional English willow bat', 7, 4999, 40),
('Football', 'FIFA-approved size 5 football', 7, 999, 80),
('Yoga Mat', 'Non-slip fitness mat', 7, 499, 100),
('Dumbbell Set 10kg', 'Adjustable dumbbell set', 7, 2999, 50),
('Tennis Racket', 'Lightweight graphite racket', 7, 2499, 60),

('Rice 10kg', 'Premium basmati rice', 8, 899, 100),
('Cooking Oil 5L', 'Refined sunflower oil', 8, 799, 80),
('Detergent Powder 3kg', 'Effective stain remover', 8, 499, 60),
('Toothpaste 200g', 'Herbal toothpaste', 8, 99, 200),
('Instant Noodles Pack', 'Spicy masala flavor', 8, 49, 300),

('Face Wash', 'Oil-control face wash', 9, 199, 150),
('Shampoo 650ml', 'Anti-dandruff shampoo', 9, 399, 100),
('Perfume Set', 'Fragrance combo pack', 9, 999, 80),
('Moisturizer 200ml', 'Daily skin care cream', 9, 299, 120),
('Lip Balm', 'Hydrating lip care', 9, 149, 150),

('Car Vacuum Cleaner', 'Compact car vacuum cleaner', 10, 1999, 50),
('Helmet', 'ISI certified helmet', 10, 1499, 60),
('Bike Cover', 'All-weather protection cover', 10, 499, 100),
('Car Perfume', 'Long-lasting fragrance', 10, 299, 150),
('Tire Inflator', 'Portable electric inflator', 10, 2499, 40),

('Notebook A5', 'Soft-bound ruled notebook', 11, 99, 500),
('Ball Pen', 'Pack of 10 blue pens', 11, 149, 300),
('Highlighter Set', 'Pack of 5 neon highlighters', 11, 199, 150),
('Marker', 'Permanent black marker', 11, 49, 250),
('Diary 2025', 'Hard-bound daily planner', 11, 299, 100),

('Garden Hose 10m', 'Durable garden hose', 12, 899, 40),
('Flower Pot Set', 'Pack of 6 ceramic pots', 12, 999, 50),
('Lawn Mower', 'Electric grass cutter', 12, 4999, 15),
('Fertilizer Mix', 'Organic plant nutrients', 12, 399, 80),
('Gardening Gloves', 'Protective gloves', 12, 199, 100),

('Dog Food 10kg', 'Nutritional dry dog food', 13, 1599, 60),
('Cat Toy Set', 'Interactive play set', 13, 499, 80),
('Pet Shampoo', 'Gentle cleansing formula', 13, 299, 70),
('Bird Cage', 'Spacious cage for small birds', 13, 999, 30),
('Dog Leash', 'Durable nylon leash', 13, 399, 100),

('Guitar Acoustic', 'Beginner 6-string guitar', 14, 4999, 20),
('Drum Sticks', 'Pair of professional sticks', 14, 299, 50),
('Keyboard 61-Keys', 'Electronic musical keyboard', 14, 8999, 10),
('Microphone', 'USB condenser mic', 14, 1999, 25),
('Violin', 'Full-size wooden violin', 14, 6999, 12),

('Digital Thermometer', 'Accurate body temperature reader', 15, 299, 100),
('Blood Pressure Monitor', 'Automatic BP monitor', 15, 1999, 30),
('Glucometer', 'Blood sugar testing device', 15, 1499, 40),
('First Aid Kit', 'Complete home first aid box', 15, 999, 60),
('Vitamin C Tablets', 'Immunity booster supplement', 15, 399, 120);
