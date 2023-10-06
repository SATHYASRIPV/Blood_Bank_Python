drop_if_exists = """DROP TABLE IF EXISTS sathya.Blood_Bank;"""
create = """CREATE TABLE IF NOT EXISTS blood_Bank(
    ID int NOT NULL AUTO_INCREMENT,
    NAME char(50),
    MOBILE char(10) NOT NULL,
    BLOOD_GROUP char(3) NOT NULL,
    GENDER char,
    AGE int NOT NULL,
    PLACE char(50) NOT NULL,
    CHECK (AGE>=18),
    PRIMARY KEY (ID)
    );"""
select = "SELECT * FROM blood_Bank;"
def insert():
    return "INSERT INTO blood_bank (NAME,MOBILE,BLOOD_GROUP,GENDER,AGE,PLACE)"
def delete():
    return """DELETE FROM blood_bank
    WHERE ID = replace_id;"""
def if_exist():
    return "SHOW TABLES;"
    

