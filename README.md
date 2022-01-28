# homeworks

```sql
CREATE TABLE people(
id SERIAL,
name VARCHAR(255),
pwd VARCHAR(255),
email VARCHAR(255),
gender varchar(255)
);


 id | name | pwd | email | gender
----+------+-----+-------+--------

```
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
```sql

SELECT concat ('This is ', name, ', ', CASE gender WHEN 'm' THEN 'he' WHEN 'f' THEN 'she' END, ' has email', email) as info FROM people;

                     info
----------------------------------------------
 This is Vasya, he has emailmmm@gmail.com
 This is Alex, he has emailmmm@gmail.com
 This is Alexey, he has emailalexey@gmail.com
 This is Helen, she has emailhell@@gmail.com
 This is Jenny, she has emaileachup@gmail.com
 This is Lora, she has emailtpicks@gmail.com
```
```sql
select concat ('We have ', count(name), CASE gender WHEN 'm' then ' boys!' WHEN 'f' THEN ' girls!' END) as "Gender information:" from people group by gender;

 Gender information:
---------------------
 We have 3 boys!
 We have 3 girls!

```

```sql
select name, (select count(*) as words from word where (word.vocabulary_id = vocabulary.id)) from vocabulary;

  name   | words
---------+-------
 animals |    10
 school  |    10
 nature  |    10
 human   |    10
 SF      |    10
(5 ёЄЁюъ)

```
