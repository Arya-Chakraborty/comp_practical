-- table creation
create table club(coach_id integer primary key, coach_name varchar(20) not null, age integer, sports varchar(20), pay int, check(pay>300));
-- (a)
select coach_name from club where coach_name like "A%" and coach_name like "%H";
-- (b)
select sports, sum(pay) from club where sports = "swimming" group by sports;
-- (c)
select coach_name, age from club order by age desc;
-- (d)
update club set pay = 1.1*pay;
(e)
alter table club drop primary key;
alter table club add primary key (coach_name);
-- (f)
delete from club where sports="swimming";
-- (g)
alter table club add gender varchar(10);