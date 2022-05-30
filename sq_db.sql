CREATE TABLE IF NOT EXISTS events (
id integer PRIMARY KEY AUTOINCREMENT,
event_time time NOT NULL,
event_date date NOT NULL,
event text NOT NULL
)