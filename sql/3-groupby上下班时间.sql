drop table if exists t_checking_in_2;
create table t_checking_in_2 
	as select user_id, user_name, check_date, department, flag,  min(check_time) as min_check_time , max(check_time) as max_check_time from t_checking_in_1 t 
	group by user_id, user_name, check_date, department, flag;
	
drop table if exists t_checking_in_all;
create table t_checking_in_all as select d.*, c.min_check_time, '' as work_flag,  c.max_check_time , '' as closed_flag, 
	(strftime('%s', c.max_check_time) - strftime('%s', c.min_check_time) - 3600)/3600.0 as work_hour, '' oa_type, '' holiday_type, '' hd_starttime, '' hd_endtime, '' overtime, '' ot_starttime, '' ot_endtime, '' ot_hour from t_user_department d left join t_checking_in_2 c
on d.user_name = c.user_name and d.department = c.department
and d.mydate = c.check_date;