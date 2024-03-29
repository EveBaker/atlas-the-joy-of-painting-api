-- Create epiesodes table
CREATE TABLE epiesodes (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(225),
    air_date DATE,
    subject_matter VARCHAR(225),
    color_palette VARCHAR(225),
);

-- Create colors table
CREATE TABLE colors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    color_name VARCHAR(50),
    hex_code VARCHAR(10)
);