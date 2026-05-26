-- SELECT *
-- FROM PERSON

-- ЗМІНИ В СТРУКТУРІ ТАБЛИЦІ
-- ДОБАВИТИ НОВИЙ СТОВПЧИК ДО ТАБЛИЦІ

-- ALTER TABLE PERSON
-- ADD COLUMN BIRTHDAY DATE  --- [НАЗВА СТОВПЧИКА] [ТИП ДАНИХ]  (ЯК В CREATE TABLE)

-- -- ВИДАЛИТИ СТОВПЧИК
-- ALTER TABLE PERSON
-- DROP COLUMN BIRTHDAY


-- ЗМІНИ В ВМІСТІ ТАБЛИЦІ
-- ЗРОБИТИ ТАК ЩОБ ВСІ НАРОДИЛИСЬ 2003-05-26

-- UPDATE PERSON
-- SET BIRTHDAY = '2003-05-26'

-- -- ТІ ХТО ЖИВЕ В КИЄВІ НАРОДИЛИСЬ В 2001-02-28
-- UPDATE PERSON
-- SET BIRTHDAY = '2001-02-28'
-- WHERE CITY = 'Kyiv'


--- ЗАПИТІВ

-- З ДАТОЮ

-- ВИВЕСТИ РІК НАРОДЖЕННЯ
-- EXTRACT(YEAR FROM [СТОВПЧИК])
-- SELECT EXTRACT(YEAR FROM BIRTHDAY)
-- FROM PERSON

-- ВИВЕСТИ МІСЯЦЬ НАРОДЖЕННЯ
-- SELECT EXTRACT(MONTH FROM BIRTHDAY)
-- FROM PERSON


-- ОТРИМАТИ ВІК НА ОСНОВІ ДАТИ
-- SELECT AGE(BIRTHDAY)
-- FROM PERSON


-- -- ЛИШЕ РІК
-- SELECT EXTRACT(YEAR FROM AGE(BIRTHDAY))
-- FROM PERSON


-- ТЕКСТИ
-- РЕГУЛЯРНІ ВИРАЗИ

-- % -- БУДЬ ЯКА КІЛЬКІСТЬ БУДЬ-ЯКИХ СИМВОЛІВ

-- ВИВЕСТИ МІСТА ЯКІ ПОЧИНАЮТЬСЯ НА K

-- SELECT CITY
-- FROM PERSON
-- WHERE CITY ILIKE 'k%'  -- ILIKE НЕ ЗВЕРТАЄ УВАГУ НА РЕГІСТР

-- -- МІСТИТЬ K В СЕРЕДИНІ
-- SELECT CITY
-- FROM PERSON
-- WHERE CITY ILIKE '%K%'


-- -- ІМЯ ЛЮДИНИ ЯКА МІТИТЬ 2 ЛІТЕРИ і
-- SELECT NAME
-- FROM PERSON
-- WHERE NAME ILIKE '%I%I%'


-- -- _ -- БУДЬ-ЯКИЙ СИМВОЛ
-- -- 3 ЛІТЕРА D
-- SELECT NAME
-- FROM PERSON
-- WHERE NAME ILIKE '__D%'


-- ГРУПУВАННЯ

-- ВИВЕСТИ КІЛЬКІСТЬ ЛЮДЕЙ В КОЖНОМУ МІСТІ(ЗГРУПУВАТИ ПО МІСТАХ)
-- В SELECT МОЖНА ВИКОРИСТОВУВАТИ АБО СТОВПЧИК ДЛЯ ГРУПУВАННЯ АБО АГРЕГАТНІ ФУНКЦІЇ
-- COUNT MIN MAX AVG SUM
-- SELECT CITY, COUNT(NAME), AVG(AGE)
-- FROM PERSON
-- GROUP BY CITY  --- GROUP BY [СТОВПЧИК]

-- -- МОЖНА ДАВАТИ НАЗВИ СТОВПЧИКАМ
-- SELECT CITY, COUNT(*) AS "КІЛЬКІТЬ ЛЮДЕЙ"
-- FROM PERSON
-- GROUP BY CITY
