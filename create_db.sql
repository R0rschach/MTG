DROP TABLE IF EXISTS mtgset;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS mtgset_card;


CREATE TABLE mtgset (
    id INTEGER PRIMARY KEY
    ,code TEXT
    ,release_date DATETIME
    ,name TEXT
    ,set_type TEXT
);

CREATE TABLE card (
    id INTEGER PRIMARY KEY
);

CREATE TABLE mtgset_card (
    mtgset_id INTEGER
    , card_id INTEGER
);

