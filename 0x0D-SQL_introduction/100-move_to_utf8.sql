-- script that converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci)
-- Database, table -> first_table and field name in first_table are all converted to UTF8

-- Convert the hbtn_0c_0 database to UTF8MB4
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Convert the first_table table to UTF8MB4
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4
    COLLATE utf8mb4_unicode_ci;

-- Convert the name field in first_table to UTF8MB4
ALTER TABLE first_table
    MODIFY COLUMN name VARCHAR(256) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
