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
    ,name TEXT
    ,manaCost TEXT
    ,cmc INTEGER
    ,colors TEXT
    ,card_type TEXT
    ,supertypes TEXT
    ,types TEXT
    ,subtypes TEXT
    ,rarity TEXT
    ,artist TEXT
    ,power INTEGER
    ,toughness INTEGER
    ,multiverseid INTEGER
);

CREATE TABLE price (
    id INTEGER PRIMARY KEY
    ,card_id INTEGER
    ,price_type INTEGER    /* 0: paper, 1: mtgo */
    ,price_datetime DATETIME
    ,price  FLOAT
;


CREATE TABLE mtgset_card (
    mtgset_id INTEGER
    , card_id INTEGER
);

