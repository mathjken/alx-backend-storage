-- this SQL script creates a stored procedure AddBonus
-- that adds a new correction for a student.
--@author Ogu Johnkennedy
DROP PROCEDURE IF EXISTS AddBonus;
DELIMITER |
CREATE PROCEDURE AddBonus (
    IN user_id int,
    IN project_name varchar(255),
    IN score int
)
BEGIN
    INSERT INTO projects (name)
    SELECT project_name FROM DUAL

    IF NOT EXISTS (SELECT * FROM projects WHERE name = project_name);
    	INSERT INTO corrections (user_id, project_id, score)
    END IF;
	VALUES (user_id, (SELECT id FROM projects WHERE name = project_name), score);
END;
|
