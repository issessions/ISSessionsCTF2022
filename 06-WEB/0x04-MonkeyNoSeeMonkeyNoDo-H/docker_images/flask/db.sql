-- Creating users table
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);

-- Inserting temporary flag into users table
INSERT INTO users (username, password) VALUES ("flag", "iisblind");

-- Creating blog entries table
CREATE TABLE IF NOT EXISTS entries (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    date TEXT NOT NULL,
    type TEXT NOT NULL,
    rating INTEGER NOT NULL,
    image TEXT NOT NULL,
    description TEXT DEFAULT "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."
);

-- Inserting blog entries
INSERT INTO entries (title, date, type, rating, image) VALUES ("Fresh Coconut Water", "2019-02-16", "Drinks", 8, "coconut-water.jpg");
INSERT INTO entries (title, date, type, rating, image) VALUES ("Coconut Chocolate", "2017-06-21", "Food", 7, "coconut-chocolate.jpg");
INSERT INTO entries (title, date, type, rating, image) VALUES ("Coconut Macaroons", "2020-11-13", "Food", 9, "coconut-macaroons.jpeg");
INSERT INTO entries (title, date, type, rating, image) VALUES ("Coconut Cake", "2017-04-23", "Food", 5, "coconut-cake.jpg");
INSERT INTO entries (title, date, type, rating, image) VALUES ("Coconut Milk", "2021-12-07", "Drinks", 4, "coconut-milk.jpg");
INSERT INTO entries (title, date, type, rating, image) VALUES ("Coconut Ice Cream", "2020-08-07", "Food", 9, "coconut-icecream.jpeg");


