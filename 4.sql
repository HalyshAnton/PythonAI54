-- таблиця груп студентів

-- CREATE TABLE GROUPS(
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR(20)
-- )

-- INSERT INTO GROUPS (NAME) VALUES
-- ('CS-101'),
-- ('CS-102'),
-- ('CS-201'),
-- ('DS-101'),
-- ('AI-101');


-- ТАБЛИЦІ СТУДЕНТІВ

-- CREATE TABLE STUDENTS(
-- 	ID SERIAL PRIMARY KEY,
-- 	NAME VARCHAR(50),
-- 	AGE INT,
-- 	-- ІНФОРМАЦІЯ ПРО ГРУПУ ДЕ НАВЧАЄТЬСЯ СТУДЕНТ
-- 	GROUP_ID INT,
-- 	-- ВКАЗУЄМО ЗВ'ЯЗОК З ІНШОЮ ТАБЛИЦЕЮ
-- 	-- ЗОВНІШНІЙ КЛЮЧ
-- 	-- FOREIGN KEY (НАШ СТОВПЧИК) REFERENCES ІНША_ТАБЛИЦЯ(ID)
-- 	FOREIGN KEY (GROUP_ID) REFERENCES GROUPS(ID)
-- )


-- INSERT INTO STUDENTS (NAME, AGE, GROUP_ID) VALUES
-- ('Ivan Petrenko', 18, 1),
-- ('Oleh Shevchenko', 19, 1),
-- ('Maria Kovalenko', 18, 2),
-- ('Anna Tkachenko', 20, 2),
-- ('Dmytro Bondar', 21, 3),
-- ('Sofia Melnyk', 19, 3),
-- ('Andrii Koval', 22, 4),
-- ('Iryna Lysenko', 18, 4),
-- ('Viktor Marchenko', 20, 5),
-- ('Olena Sydorenko', 19, 5),

-- ('Taras Shevchuk', 18, 1),
-- ('Kateryna Hrytsenko', 21, 2),
-- ('Yaroslav Kuts', 22, 3),
-- ('Natalia Romanenko', 19, 4),
-- ('Bohdan Filipov', 20, 5),

-- ('Alina Zaitseva', 18, 1),
-- ('Maksym Danyliuk', 21, 2),
-- ('Veronika Ostapchuk', 20, 3),
-- ('Pavlo Savchuk', 19, 4),
-- ('Diana Moroz', 22, 5);

-- -- УТОЧНЕННЯ З ЯКОЇ ТАБЛИЦІ СТОВПЧИК
-- -- [ТАБЛИЦЯ].[СТОВПЧИК]
-- SELECT G.NAME
-- FROM GROUPS G -- СКОРОЧЕННЯ ДЛЯ НАЗВИ ТАБЛИЦІ


-- ОБ'ЄДНАННЯ ТАБЛИЦЬ
-- ВИВЕСТИ СТУДЕНТІВ ТА ЇХНІ ГРУПИ
-- [ТАБЛИЦЯ 1] JOIN [ТАБЛИЦЯ 2] ON [УМОВА] JOIN [ТАБЛИЦЯ 3] ON [УМОВА] ...
SELECT *
FROM GROUPS G JOIN STUDENTS S ON S.GROUP_ID = G.ID
