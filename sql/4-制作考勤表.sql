update t_checking_in_all set hd_starttime = '', hd_endtime = '', oa_type='', holiday_type = '';


--更新外出流程
update t_checking_in_all
set hd_starttime =  (select o.'外出日期'|| ' '|| o.'外出时间' from t_outing o where user_name = o.'外出人员' and mydate >= o.'外出日期' and mydate <= o.'返回日期')
where exists (select o.'外出日期' from t_outing o where user_name = o.'外出人员' and mydate >= o.'外出日期' and mydate <= o.'返回日期');

update t_checking_in_all
set hd_endtime   =  (select o.'返回日期'|| ' '|| o.'返回时间' from t_outing o where user_name = o.'外出人员' and mydate >= o.'外出日期' and mydate <= o.'返回日期')
where exists (select o.'外出日期' from t_outing o where user_name = o.'外出人员' and mydate >= o.'外出日期' and mydate <= o.'返回日期');

update t_checking_in_all
set oa_type = "外出流程" 
where exists (select o.'外出日期' from t_outing o where user_name = o.'外出人员' and mydate >= o.'外出日期' and mydate <= o.'返回日期');

--更新出差流程
update t_checking_in_all
set hd_starttime =  (select o.'开始日期'|| ' '|| o.'开始时间' from t_outing2 o where user_name = o.'申请人' and mydate >= o.'开始日期' and mydate <= o.'结束日期')
where exists (select o.'开始日期' from t_outing2 o where user_name = o.'申请人' and mydate >= o.'开始日期' and mydate <= o.'结束日期');

update t_checking_in_all
set hd_endtime   =  (select o.'结束日期'|| ' '|| o.'结束时间' from t_outing2 o where user_name = o.'申请人' and mydate >= o.'开始日期' and mydate <= o.'结束日期')
where exists (select o.'开始日期' from t_outing2 o where user_name = o.'申请人' and mydate >= o.'开始日期' and mydate <= o.'结束日期');

update t_checking_in_all
set oa_type = "出差流程" where exists (select o.'开始日期' from t_outing2 o where user_name = o.'申请人' and mydate >= o.'开始日期' and mydate <= o.'结束日期');


--更新请假流程
update t_checking_in_all
set hd_starttime =  (select h.'开始日期'|| ' '|| h.'开始时间' from t_user_holiday h where mydate >= h.'开始日期' and mydate <= h.'结束日期' and user_name = h.'请假人')
where hd_starttime = '' or hd_starttime is null;

update t_checking_in_all
set hd_endtime   =  (select h.'结束日期'||' '||h.'结束时间' from t_user_holiday h where mydate >= h.'开始日期' and mydate <= h.'结束日期' and user_name = h.'请假人')
where hd_endtime = '' or hd_endtime is null;

update t_checking_in_all
set holiday_type = (select h.'请假类型' from t_user_holiday h where mydate >= h.'开始日期' and mydate <= h.'结束日期' and user_name = h.'请假人')
where exists (select h.'请假类型' from t_user_holiday h where mydate >= h.'开始日期' and mydate <= h.'结束日期' and user_name = h.'请假人');

update t_checking_in_all
set oa_type = "请假流程" where exists (select h.'请假类型' from t_user_holiday h where mydate >= h.'开始日期' and mydate <= h.'结束日期' and user_name = h.'请假人');

--更新加班
update t_checking_in_all
set ot_starttime   =  (select o.'加班开始日期'||' '||o.'加班开始时间' from t_overtime o where user_name = o.'申请人' and mydate >= o.'加班开始日期' and mydate <= o.'加班结束日期');

update t_checking_in_all
set ot_endtime   =  (select o.'加班结束日期'||' '||o.'加班结束时间' from t_overtime o where user_name = o.'申请人' and mydate >= o.'加班开始日期' and mydate <= o.'加班结束日期');

update t_checking_in_all
set ot_hour   =  (select o.'加班时长' from t_overtime o where user_name = o.'申请人' and mydate >= o.'加班开始日期' and mydate <= o.'加班结束日期');

update t_checking_in_all
set overtime = "加班申请" where overtime = '' and ot_starttime !='';