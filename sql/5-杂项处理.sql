-- 排除考勤开始时间=结束时间
update t_checking_in_all set work_hour = 0
where max_check_time = min_check_time;

-- 修正部分上班时间不包括中午休息时间 补+1
update t_checking_in_all set work_hour = work_hour + 1.0
where ('12:00' < min_check_time or '12:00' > max_check_time)
and min_check_time != max_check_time;


update t_checking_in_all set work_flag = '', closed_flag = '';

-- 更新 work_flag = '未打卡'
update t_checking_in_all 
set work_flag = '未打卡'
where min_check_time is null and hd_starttime is null and weekday = '工作日' and work_flag = '';

-- 更新 work_flag = oa_type
update t_checking_in_all
set work_flag = oa_type
where (min_check_time is null or '09:00' < min_check_time) 
and mydate||' 09:00' >= hd_starttime and weekday = '工作日'
and work_flag = '';

-- 更新 work_flag = '迟到'
update t_checking_in_all
set work_flag = '迟到'
where (min_check_time is null or '09:00' < min_check_time) and 
(hd_starttime is null or mydate||' 09:00' < hd_starttime) and weekday = '工作日'
and work_flag = '';



-- 更新 closed_flag = '未打卡'
update t_checking_in_all 
set closed_flag = '未打卡'
where max_check_time is null and hd_endtime is null and weekday = '工作日' and closed_flag = '';

-- 更新 closed_flag = oa_type
update t_checking_in_all
set closed_flag = oa_type
where (max_check_time is null or '18:00' > max_check_time) 
and mydate||' 18:00' <= hd_endtime and weekday = '工作日'
and closed_flag = '';

-- 更新 closed_flag = '早退'
update t_checking_in_all
set closed_flag = '早退'
where (max_check_time is null or '18:00' > max_check_time) and 
(hd_endtime is null or mydate||' 18:00' > hd_endtime) and weekday = '工作日'
and closed_flag = '';

-- 更新未打卡的标记
update t_checking_in_all
set work_flag = '未打卡' 
where work_hour <= 0 and (oa_type = '' or oa_type is null) and min_check_time > '13:00' 
and weekday = '工作日';

update t_checking_in_all
set closed_flag = '未打卡' 
where work_hour <= 0 and (oa_type = '' or oa_type is null) and max_check_time < '12:00' 
and weekday = '工作日';