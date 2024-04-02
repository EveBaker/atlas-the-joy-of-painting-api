CREATE DATABASE JoyOfPaintingDB;

USE JoyOfPaintingDB;

CREATE TABLE Episodes (
    episode_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(225) NOT NULL,
    season INT NOT NULL,
    air_date DATE NOT NULL
);

CREATE TABLE Colors (
    color_id INT AUTO_INCREMENT PRIMARY key,
    color_name VARCHAR(50) NOT NULL
);

CREATE TABLE Subjects (
    subject_id INT AUTO_INCREMENT PRIMARY KEY,
    sunbject_name VARCHAR(50) NOT NULL
);

CREATE TABLE Episode_Colors (
    episode_id INT,
    color_id INT,
    FOREIGN KEY (episode_id) REFERENCES Episodes(episode_id),
    FOREIGN KEY (color_name) REFERENCES Colors(color_id)
);

CREATE TABLE Episode_subjects (
    episode_id INT,
    subject_id INT,
    FOREIGN KEY (episode_id) REFERENCES Episodes(episode_id),
    FOREIGN KEY (subject_id) REFERENCES Subjects(subject_id)
);