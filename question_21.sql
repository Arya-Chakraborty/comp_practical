-- I
select * from stock order by stockdate;
-- II
select dcode, max(unitprice) from stock order by dcode;
-- III
select * from stock order by item desc;
-- IV
select dcode, avg(unitprice) from stock group by dcode having avg(unitprice) > 5;
-- V
select dcode, sum(qty) from stock group by dcode;