-- create view to count the images
create view v_total_images_per_category as
select 
_id,
sum(case when category_images = 'images_interior' then 1 else 0 end) 'images_interior',
sum(case when category_images = 'images_exterior' then 1 else 0 end) 'images_exterior',
sum(case when category_images = 'images_floorplan' then 1 else 0 end) 'images_floorplan',
sum(case when category_images = 'images_360' then 1 else 0 end) 'images_360',
sum(case when category_images = 'images_developer' then 1 else 0 end) 'images_developer',
sum(case when category_images = 'images_banner' then 1 else 0 end) 'images_banner',
sum(case when category_images = 'images_brochure' then 1 else 0 end) 'images_brochure',
sum(case when category_images = 'video_link' then 1 else 0 end) 'video_link'
from complex_images where source = 'complex'
group by _id;

-- create view to calculate the point
create view v_point_images_per_category  as
select que.*, 
(que.images_interior+que.images_exterior+que.images_360+que.video_link+que.images_developer+que.images_banner+que.images_brochure) as 'total_point'
from
(
select
_id,  
case when images_interior = 0 then 0 when images_interior between 1 and 2 then 5 when images_interior between 3 and 4 then 7 else 10 end as 'images_interior',
case when images_exterior = 0 then 0 when images_exterior between 1 and 2 then 3 when images_exterior between 3 and 4 then 5 else 10 end as 'images_exterior',
case when images_360 = 0 then 0 when images_360 between 1 and 2 then 7 else 10 end as 'images_360',
case when video_link = 0 then 0 else 10 end as 'video_link',
case when images_developer = 0 then 0 when images_developer between 1 and 2 then 5 when images_developer between 3 and 4 then 7 else 10 end as 'images_developer',
case when images_banner = 0 then 0 else 10 end as 'images_banner',
case when images_brochure = 0 then 0 when images_brochure between 1 and 2 then 7 else 10 end as 'images_brochure'
from v_total_images_per_category 
) que;

-- ranking the complex
select c.*, IFNULL(v.total_point,0) as 'total_point' from complex c
left join v_point_images_per_category v on c._id = v._id
order by v.total_point desc, c.name asc;