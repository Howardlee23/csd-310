
/* Howard Hardnett
SQL Insert Statements
May 14, 2022
Module 12 Assignment

mysql -u root -p */

-- Create whatabook_user and grant them all privileges to the whatabook database 
CREATE USER 'whatabook_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'MySQL8IsGreat!';

-- Grant all privileges to the whatabook database to user whatabook_user on localhost 
GRANT ALL PRIVILEGES ON whatabook.* TO'whatabook_user'@'localhost';

-- CREATE USER TABLE --
CREATE TABLE user (
    user_id         INT             NOT NULL        AUTO_INCREMENT,
    first_name      VARCHAR(75)     NOT NULL,
    last_name       VARCHAR(75)     NOT NULL,
    PRIMARY KEY(user_id)
);	

-- CREATE BOOKS TABLE  --
CREATE TABLE book (
    book_id     INT                 NOT NULL        AUTO_INCREMENT,
    book_name   VARCHAR(200)        NOT NULL,
    details      VARCHAR(500)        NOT NULL,
    author     VARCHAR(200),
    PRIMARY KEY(book_id)
);

-- CREATE WISHLIST TABLE --
CREATE TABLE wishlist (
    wishlist_id     INT  primary key           NOT NULL        AUTO_INCREMENT,
    user_id         INT             NOT NULL,
    book_id         INT             NOT NULL,
    CONSTRAINT fk_users
    FOREIGN KEY (user_id)
        REFERENCES users(user_id),
    CONSTRAINT fk_books
    FOREIGN KEY (book_id)
        REFERENCES books(book_id)
); 

-- CREATE STORE TABLE -- 
CREATE TABLE store (
    store_id    INT                 NOT NULL        AUTO_INCREMENT,
    locale      VARCHAR(500)        NOT NULL,
    PRIMARY KEY(store_id)
);

-- INSERT STORE VALUES -- 
INSERT INTO store(store_id,locale)
    VALUES(1001,'5801 S 98th Street Blowback Town, Jakku');
    
-- INSERT USER VALUES --
INSERT INTO user(first_name, last_name)
    VALUES('Iris', 'Kyle');

INSERT INTO user(first_name, last_name)
    VALUES('Ronnie', 'Coleman');

INSERT INTO user(first_name, last_name)
    VALUES('Michael', 'Scott');

-- INSERT BOOK VALUES -- 

INSERT INTO book(book_name, details, author) 
    VALUES("The bad Seed", "This is about a bad seed. A baaaaad seed. Find out how bad.", "Jory John");

INSERT INTO book(book_name, details, author) 
    VALUES("Super Simple Biology", "Bring biology to life with this book!!", "DK");

INSERT INTO book(book_name, details, author) 
    VALUES("Physics Activity Booky", "Expose young children ot the joys of Physics", "Jenny Jacoby");

INSERT INTO book(book_name, details, author) 
    VALUES("The Couch Potato", "The couch potato never leaves his couch but now it is forced to becuase the power is out. Could this help or hurt the potato?", "Jory John");

INSERT INTO book(book_name, details, author) 
    VALUES("One Lost Soul", "A chilling British detective crime thriller.", "J M Dalgliesh");

INSERT INTO book(book_name, details, author) 
    VALUES("Ripple Effect", "One shot. One kill. A simple plan. A simple operation that puts Bear Loagn and Jack Noble in the crosshairs of a traitor.", "L.T. Ryan");

INSERT INTO book(book_name, details, author) 
    VALUES("Blowback", "Riley Bear Logan return in Blowback. He is framed for murder but is offered a way out. If he does a little job first.","L.T. Ryan");

INSERT INTO book(book_name, details, author) 
    VALUES("French Bread Cooking", "Cook tasty French breads at home with easy and gunuine recipes.", "Della Hunt");

INSERT INTO book(book_name, author) 
    VALUES("Rangers Apprentice: The Ruins of Gorlan", "A story of heros and villains that has become an international phenomenon.", "John Flanagan");


-- INSERT 1 BOOK IN EACH USER ACCOUNT -- 
INSERT INTO wishlist(user_id,book_id)
	VALUES(1,8);
    
    INSERT INTO wishlist(user_id,book_id)
	VALUES(2,5);
    
    INSERT INTO wishlist(user_id,book_id)
	VALUES(3,1);
    