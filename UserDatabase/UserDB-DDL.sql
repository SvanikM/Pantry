CREATE DATABASE PantryDB;

USE PantryDB;

DROP TABLE INGREDIENTS;
DROP TABLE USERS;

#Allows a single user to create multiple accounts for separate kitchen/pantry locations
CREATE TABLE USERS(
    Email CHAR(30) NOT NULL,
    UserName VARCHAR(30) NOT NULL,
    Password VARCHAR(20) NOT NULL,
    CONSTRAINT USERS_PK PRIMARY KEY (Email, UserName),
    CONSTRAINT PASS_LEN_CK CHECK(CHAR_LENGTH(Password) > 10)
);

#Ingredient Unit + Ingredient Quantity are used to specify between 3 gallons vs 3 quarts of milk
CREATE TABLE INGREDIENTS(
    Email CHAR(30) NOT NULL,
    UserName VARCHAR(30) NOT NULL,
    IngredientName CHAR(20) NOT NULL,
    IngredientQuantity NUMERIC(6,2) NOT NULL,
    IngredientUnit CHAR(10),
    CONSTRAINT INGREDIENTS_PK PRIMARY KEY (Email, Username, IngredientName),
    CONSTRAINT INGREDIENTS_FK FOREIGN KEY (Email, UserName) REFERENCES USERS (Email, UserName),
    CONSTRAINT QUANT_POS_CK CHECK(IngredientQuantity >= 0)
);

