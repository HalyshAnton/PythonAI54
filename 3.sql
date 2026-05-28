-- ТАБЛИЦЯ ЗІ СТУДЕНТАМИ
-- CREATE TABLE [НАЗВА ТАБЛИЦІ] (...)


CREATE TABLE STUDENT(
	ID SERIAL PRIMARY KEY,   -- УНІКАЛЬНИЙ ІДЕНТИФІКАТОР
	NAME VARCHAR(50) UNIQUE,  -- ЗНАЧЕННЯ В СТОВПЧИКУ МАЮТЬ БУТИ УНІКАЛЬНІ
	AGE INT NOT NULL,  -- НЕМОЖЕ БУТИ ПОРОЖНІМ
	COURSE VARCHAR(30) DEFAULT 'PYTHON+AI',   -- ЗНАЧЕННЯ ЗА ЗАМОВЧУВАННЯМ
	BIRTHDAY DATE CHECK(BIRTHDAY < CURRENT_DATE) -- УМОВАМА ЯКІЙ ПОВИННІ ВІДПОВІДАТИ УСІ ДАНІ(ДАТА НАРОДЖЕННЯ МАЄ БУТИ МЕНШОЮ ЗА ТЕПЕРІШНЮ ДАТУ)\
	PREMIUM INT UNIQUE NOT NULL CHECK(PREMIUM >= 0)
)


INSERT INTO STUDENT (NAME, AGE, COURSE, BIRTHDAY)
VALUES
('Anton2', 16, 'PYTHON+AI', '2030-03-15')
