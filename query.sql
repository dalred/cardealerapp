UPDATE car_models
SET country_id = (abs(random()) % (9 - 1) + 1)
where country_id is NOT NULL;


WITH const AS (SELECT datetime(strftime('%s', '2000-01-01 00:00:00') +
                abs(random() % (strftime('%s', '2000-01-31 23:59:59') -
                                strftime('%s', '2020-01-01 00:00:00'))
                   ),
                'unixepoch') AS test)
INSERT INTO cars(model_id, year) SELECT id,test from car_models, const;


UPDATE cars
SET model_id = (abs(random()) % (101 - 1) + 1)
where model_id is NOT NULL;

UPDATE cars
SET price = ROUND((abs(random()) % (2022 - 1) + 1)/ CAST(9 AS REAL),2)
where price is NOT NULL;

INSERT INTO dealers(name, phone, email, address) SELECT last_name,phone_number,email,city from person;


UPDATE car_models
SET brand = 'Honda'
where brand is NULL;

UPDATE cars
SET dealer_id = (abs(random()) % (21 - 1) + 1)
where dealer_id is NULL;