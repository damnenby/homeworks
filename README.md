# homeworks

```sql
CREATE TABLE people(
id SERIAL,
name VARCHAR(255),
pwd VARCHAR(255),
email VARCHAR(255),
gender varchar(255)


 id | name | pwd | email | gender
----+------+-----+-------+--------
);
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

select concat ('This is ', people.name, ', he has email ', people.email) as info from people where gender = 'm' union select concat ('This is ', people.name, ', she has email ', people.email) from people where gender = 'f';

                     info
-----------------------------------------------
 This is Alex, he has email mmm@gmail.com
 This is Alexey, he has email alexey@gmail.com
 This is Helen, she has email hell@@gmail.com
 This is Jenny, she has email eachup@gmail.com
 This is Lora, she has email tpicks@gmail.com
 This is Vasya, he has email mmm@gmail.com

```
```sql
select concat ('We have ', count(people.gender), ' boys!') as "Gender information:"from people where gender = 'm' union select concat ('We have ', count(people.gender), ' girls!') from people where gender = 'f';

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
