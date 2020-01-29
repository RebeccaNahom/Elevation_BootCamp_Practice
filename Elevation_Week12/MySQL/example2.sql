USE sql_intro; 

-- CREATE TABLE Deity(
--     id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
--     name VARCHAR(50),
--     mythology VARCHAR(20),
--     main_power VARCHAR(50),
--     coolness INT,
--     creation_date INT
-- )

-- INSERT INTO Deity VALUES(null, "Ares", "Greek", "War", 2, "-1");
-- INSERT INTO Deity VALUES(null, "Attis", "Greek", "Vegetation", 1, "1000");
-- INSERT INTO Deity VALUES(null, "Triton", "Greek", "Trident", 11, "1400");
-- INSERT INTO Deity VALUES(null, "Eros", "Greek", "Love", 100, "-3400");
-- INSERT INTO Deity VALUES(null, "Hephaestus", "Greek", "Fire", null, null);

SELECT * FROM Deity ORDER BY coolness DESC


-- SELECT name, main_power
-- FROM Deity
-- WHERE name like "f%"