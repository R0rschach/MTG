DROP TABLE IF EXISTS mtgset;
DROP TABLE IF EXISTS card;
DROP TABLE IF EXISTS mtgset_card;


CREATE TABLE mtgset (
    id INTEGER PRIMARY KEY
    ,code TEXT
    ,release_date DATETIME
    ,name TEXT              /* Magic Json Set Name */
    ,tcg_alias TEXT         /* TCG Player Set Name */
    ,goldfish_alias TEXT    /* MTGO Goldfish Set Name */
    ,set_type TEXT
    ,card_count INTEGER
    ,is_block BOOLEAN
    ,is_standard BOOLEAN
    ,is_modern BOOLEAN
);

CREATE TABLE card (
    id INTEGER PRIMARY KEY
);

CREATE TABLE mtgset_card (
    mtgset_id INTEGER
    , card_id INTEGER
);

