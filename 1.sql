-- СТВОРИТИ ТАБЛИЦІ

-- CREATE TABLE PERSON(
-- 	-- [НАЗВА СТОВПЧИКА] [ТИП ДИНИХ] ...
-- 	ID SERIAL,  -- ID ЦІЛЕ ЧИСЛО ВІД 1 І ЗБІЛЬШУЄТЬСЯ АВТОМАТИЧНО
-- 	NAME VARCHAR(30),  -- ТЕКСТ НЕ БІЛЬШЕ 30 СИМВОЛІВ
-- 	AGE INT,
-- 	CITY VARCHAR(20)
-- )

-- -- НАПОВНЕННЯ ТАБЛМЦІ ДАНИМИ
-- INSERT INTO PERSON(NAME, AGE, CITY)
-- VALUES
-- ('JOHN', 45, 'ODESA'),
-- ('MARY', 34, 'KHARKIV'),
-- ('SOPHIE', 27, 'POLTAVA')

-- ЗАПИТИ(ОТРИМАННЯ ІНФОРМАЦІЇ)
-- SELECT СТОВПЧИК1 СТОВПЧИК2 ...
-- FROM ТАБЛИЦЯ
-- WHERE УМОВА

-- -- ОТРИМАТИ ВСІ ДАНІ
-- SELECT ID, NAME, AGE, CITY
-- FROM PERSON;

-- -- -- ЩОБ НЕ ПЕРЕРАХОВУВАТИ ВСІ СТОВПЧИКИ МОЖНА НАПИСАТИ *
-- SELECT *
-- FROM PERSON;

-- -- ДІСТАТИ ІМ'Я ТА ВІК ЛЮДЕЙ СТАРШЕ 30
-- SELECT NAME, AGE
-- FROM PERSON
-- WHERE AGE > 30

-- -- ЛЮДИ ЯКІ ЖИВУТЬ В ПОЛТАВІ
-- SELECT *
-- FROM PERSON
-- WHERE CITY = 'POLTAVA'

-- ЛЮДИ ЯКІ ЖИВУТЬ В ОДЕСІ ТА ХАРКОВІ
SELECT *
FROM PERSON
WHERE CITY = 'ODESA' OR CITY = 'KHARKIV'
