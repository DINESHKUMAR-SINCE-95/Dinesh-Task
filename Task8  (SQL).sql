-- Create IMDB database
CREATE DATABASE IMDB;
USE IMDB;

-- Create Movies table
CREATE TABLE Movies (
    movie_id INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    release_year YEAR,
    PRIMARY KEY (movie_id)
);

-- Create Media table
CREATE TABLE Media (
    media_id INT AUTO_INCREMENT,
    movie_id INT,
    type ENUM('Video', 'Image') NOT NULL,
    url VARCHAR(255) NOT NULL,
    PRIMARY KEY (media_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id)
);

-- Create Genres table
CREATE TABLE Genres (
    genre_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (genre_id)
);

-- Create Movie_Genres junction table
CREATE TABLE Movie_Genres (
    movie_id INT,
    genre_id INT,
    PRIMARY KEY (movie_id, genre_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (genre_id) REFERENCES Genres(genre_id)
);

-- Create Users table
CREATE TABLE Users (
    user_id INT AUTO_INCREMENT,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    PRIMARY KEY (user_id)
);

-- Create Reviews table
CREATE TABLE Reviews (
    review_id INT AUTO_INCREMENT,
    movie_id INT,
    user_id INT,
    rating INT CHECK (rating >= 1 AND rating <= 10),
    review_text TEXT,
    PRIMARY KEY (review_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Create Artists table
CREATE TABLE Artists (
    artist_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (artist_id)
);

-- Create Skills table
CREATE TABLE Skills (
    skill_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (skill_id)
);

-- Create Artist_Skills junction table
CREATE TABLE Artist_Skills (
    artist_id INT,
    skill_id INT,
    PRIMARY KEY (artist_id, skill_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
    FOREIGN KEY (skill_id) REFERENCES Skills(skill_id)
);

-- Create Roles table
CREATE TABLE Roles (
    role_id INT AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL,
    PRIMARY KEY (role_id)
);

-- Create Movie_Artist_Roles junction table
CREATE TABLE Movie_Artist_Roles (
    movie_id INT,
    artist_id INT,
    role_id INT,
    PRIMARY KEY (movie_id, artist_id, role_id),
    FOREIGN KEY (movie_id) REFERENCES Movies(movie_id),
    FOREIGN KEY (artist_id) REFERENCES Artists(artist_id),
    FOREIGN KEY (role_id) REFERENCES Roles(role_id)
);

-- Insert sample data

-- Insert into Movies
INSERT INTO Movies (title, release_year) VALUES ('Inception', 2010), ('The Dark Knight', 2008);

-- Insert into Media
INSERT INTO Media (movie_id, type, url) VALUES (1, 'Video', 'http://example.com/inception_trailer.mp4'), (1, 'Image', 'http://example.com/inception_poster.jpg');

-- Insert into Genres
INSERT INTO Genres (name) VALUES ('Sci-Fi'), ('Action');

-- Insert into Movie_Genres
INSERT INTO Movie_Genres (movie_id, genre_id) VALUES (1, 1), (1, 2), (2, 2);

-- Insert into Users
INSERT INTO Users (username, email) VALUES ('user1', 'user1@example.com'), ('user2', 'user2@example.com');

-- Insert into Reviews
INSERT INTO Reviews (movie_id, user_id, rating, review_text) VALUES (1, 1, 9, 'Amazing movie!'), (2, 2, 8, 'Great action sequences.');

-- Insert into Artists
INSERT INTO Artists (name) VALUES ('Leonardo DiCaprio'), ('Christian Bale');

-- Insert into Skills
INSERT INTO Skills (name) VALUES ('Acting'), ('Directing');

-- Insert into Artist_Skills
INSERT INTO Artist_Skills (artist_id, skill_id) VALUES (1, 1), (2, 1);

-- Insert into Roles
INSERT INTO Roles (name) VALUES ('Actor'), ('Director');

-- Insert into Movie_Artist_Roles
INSERT INTO Movie_Artist_Roles (movie_id, artist_id, role_id) VALUES (1, 1, 1), (2, 2, 1);
