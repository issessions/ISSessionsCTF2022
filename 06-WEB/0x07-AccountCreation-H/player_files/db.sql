-- Creating users table
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    privilege INTEGER NOT NULL
);

#TODO actually run these scripts and add the admin user lol
INSERT INTO users ("admin","theadminpass",10);
INSERT INTO users ("notadminuser","notadminpass",1);




