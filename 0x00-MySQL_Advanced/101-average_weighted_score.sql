-- This SQL script creates a stored procedure ComputeAverageWeightedScoreForUsers that computes and store the average weighted score for all students
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
    UPDATE users AS Us, 
        (SELECT Us.id, SUM(score * weight) / SUM(weight) AS we_ag 
        FROM users AS Us 
        JOIN corrections as C ON Us.id=C.user_id 
        JOIN projects AS Pj ON C.project_id=Pj.id 
        GROUP BY Us.id)
    AS WA
    SET Us.average_score = WA.we_ag 
    WHERE Us.id=WA.id;
END
$$
DELIMITER ;
