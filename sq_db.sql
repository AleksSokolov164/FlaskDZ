CREATE TABLE IF NOT EXISTS feedback (
id integer PRIMARY KEY AUTOINCREMENT,
username text NOT NULL,
email text NOT NULL,
message text NOT NULL
);