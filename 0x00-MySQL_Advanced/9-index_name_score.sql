-- this SQL script creates an index base of the first name and score of user
CREATE INDEX idx_name_first_score ON names (name(1), score);
