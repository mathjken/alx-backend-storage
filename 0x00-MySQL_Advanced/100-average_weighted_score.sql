-- This SQL script creates a stored procedure ComputeAverageWeightedScoreForUser that computes and store the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER $$
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE w_avg_score FLOAT;
    SET w_avg_score = (SELECT SUM(score * weight) / SUM(weight) 
                        FROM users AS Us 
                        JOIN corrections as Cr ON Us.id=Cr.user_id 
                        JOIN projects AS Pj ON Cr.project_id=Pj.id 
                        WHERE Us.id=user_id);
    UPDATE users SET average_score = w_avg_score WHERE id=user_id;
END
$$
DELIMITER ;
