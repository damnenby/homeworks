# homeworks

```sql
CREATE TABLE people(
id SERIAL,
name VARCHAR(255),
pwd VARCHAR(255),
email VARCHAR(255),
gender varchar(255)
);
```
 id | name | pwd | email | gender
----+------+-----+-------+--------
```sql
INSERT INTO people (name, pwd, email, gender) VALUES ('Vasya','21341234qwfsdf','mmm@gmail.com','m'),('Alex','21341234','mmm@gmail.com','m'),('Alexey','qq21341234Q','alexey@gmail.com','m'),('Helen','MarryMeeee','hell@@gmail.com','f'),('Jenny','SmakeMyb','eachup@gmail.com','f'),('Lora','burn23','tpicks@gmail.com','f') ;

 id |  name  |      pwd       |      email       | gender
----+--------+----------------+------------------+--------
  1 | Vasya  | 21341234qwfsdf | mmm@gmail.com    | m
  2 | Alex   | 21341234       | mmm@gmail.com    | m
  3 | Alexey | qq21341234Q    | alexey@gmail.com | m
  4 | Helen  | MarryMeeee     | hell@@gmail.com  | f
  5 | Jenny  | SmakeMyb       | eachup@gmail.com | f
  6 | Lora   | burn23         | tpicks@gmail.com | f
```
