CREATE TABLE IF NOT EXISTS feedback (
id integer PRIMARY KEY AUTOINCREMENT,
username text NOT NULL,
email text NOT NULL,
message text NOT NULL
);

CREATE TABLE IF NOT EXISTS users(
id integer PRIMARY KEY AUTOINCREMENT,
name text NO NULL,
email text NO NULL,
psw text NO NULL
);