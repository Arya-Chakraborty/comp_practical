-- I
select * from prepaid where connection in ["Jio", "Vodafone"];
-- II
select distinct connection from prepaid;
-- III
select connection, max(plan) from prepaid group by connection;
-- IV
select model, count(model) from prepaid group by model;
-- V
select * from prepaid where custname like "%k";
