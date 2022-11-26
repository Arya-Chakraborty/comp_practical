-- creation of table
create table Product(pid varchar(20) primary key, product varchar(20), number_of_items integer, total_price integer, check(total_price<100000));
-- (h)
select product from Product where product like "%R";
-- (i)
select product from Product where number_of_items < 50;
-- (j)
select product, total_price from Product order by total_price desc;
-- (k)
alter table Product drop primary key;
alter table Product add primary key (product);
-- (l)
update Product set number_of_items = 1.1 * number_of_items;
-- (m)
delete from Product where total_price < 5000;
-- (n)
alter table Product add date_of_manufacture date;