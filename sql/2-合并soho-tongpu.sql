drop table if exists t_checking_in_1;
create table t_checking_in_1 as select * from (
select 人员编号 as user_id, 姓名 as user_name, substr(t.'考勤时间', 0, instr(t.'考勤时间', ' ')) as check_date, substr(t.'考勤时间', instr(t.'考勤时间', ' ') + 1) as check_time, 部门 as department, 'soho' as flag from t_checking_in_soho t
union all
select 人员编号 as user_id, 姓名 as user_name, 刷卡日期 as check_date, 刷卡时间 as check_time, 部门 as department, 'tongpu' as flag from t_checking_in_tongpu
);

delete from t_checking_in_1 where user_name = '' or user_name is null;

update t_date_temp set week = '星期天', weekday='休息日'
 where week = '0' or week = '7';
update t_date_temp set week = '星期一', weekday='工作日'
 where week = '1';
update t_date_temp set week = '星期二', weekday='工作日'
 where week = '2';
update t_date_temp set week = '星期三', weekday='工作日'
 where week = '3';
update t_date_temp set week = '星期四', weekday='工作日'
 where week = '4';
update t_date_temp set week = '星期五', weekday='工作日'
 where week = '5';
update t_date_temp set week = '星期六', weekday='休息日'
 where week = '6';
 
update t_date_temp set weekday='工作日' 
 where mydate in ('2016-02-06','2016-02-14','2016-06-12', '2016-09-18', '2016-10-08', '2016-10-09');

update t_date_temp set weekday='休息日' 
 where mydate in ('2016-01-01','2016-01-02','2016-01-03','2016-02-07', '2016-02-08',
 '2016-02-09', '2016-02-10','2016-02-11', '2016-02-12', '2016-02-13', '2016-04-02',
 '2016-04-03', '2016-04-04', '2016-04-30', '2016-05-01', '2016-05-02', '2016-06-09',
 '2016-06-10', '2016-06-11','2016-09-15', '2016-09-16', '2016-09-17', '2016-10-01',
 '2016-10-02', '2016-10-03', '2016-10-04', '2016-10-05', '2016-10-06', '2016-10-07');


drop table if exists t_user_department;
create table t_user_department as select * from (
select distinct department, user_name  from t_checking_in_1
),  t_date_temp;

update t_checking_in_1 
	set check_date = replace(check_date, '/', '-0') where length(check_date) = 8;
update t_checking_in_1 
	set check_date = substr(check_date, 1,4)||'-0'||substr(check_date,6,1)||'-'||substr(check_date,8) where length(check_date) = 9 and substr(check_date, 7,1) = '/';
update t_checking_in_1 
	set check_date = substr(check_date, 1,4)||'-'||substr(check_date,6,2)||'-0'||substr(check_date,9) where length(check_date) = 9 and substr(check_date, 8,1) = '/';
update t_checking_in_1 
	set check_time = '0'||check_time where length(check_time) = 7;
