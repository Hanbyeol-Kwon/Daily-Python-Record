use bestproducts;

-- join 활용
select r.main_category, count(*) from items i join ranking r on i.item_code=r.item_code where i.dis_price >= 100000 group by r.main_category;
-- 서브쿼리 용용
select main_category, count(*) from ranking where item_code in (select item_code from items where dis_price >= 100000) group by main_category;

-- join 활용
select r.sub_category, count(*) from ranking r join items i on r.item_code=i.item_code where i.dis_price >= 200000 group by r.sub_category;
-- 서브쿼리 활용
select sub_category, count(*) from ranking where item_code in (select item_code from items where dis_price >=200000) group by sub_category;

-- final sql
select * from items;
select * from ranking;
select r.main_category, r.sub_category, avg(dis_price), avg(discount_percent) from ranking r join items i on r.item_code=i.item_code group by r.main_category, r.sub_category;

-- 판매자별, 베스트상품 갯수, 평균할인가격, 평균할인율을 베스트상품 갯수가 높은 순으로 출력
select i.provider, count(*), avg(dis_price), avg(discount_percent) from items i join ranking r on i.item_code=r.item_code group by i.provider order by count(*) desc;

-- 각 메인 카테고리별로(서브카테고리포함) 베스트 상품 갯수가 20개 이상인 판매자/의 판매자별 평균할인가격, 평균할인율, 베스트 상품 갯수 출력
select r.main_category, i.provider, avg(i.dis_price), avg(i.discount_percent), count(*) from items i join ranking r on i.item_code=r.item_code group by r.main_category, i.provider having count(*)>=20;

-- 'items' 테이블에서 'dis_price'가 50000 이상인 상품들중, 각 'main_category'별 평균 'dis_price'와 'discount_percent' 출력
select r.main_category, avg(i.dis_price), avg(i.discount_percent) from ranking r join items i on r.item_code=i.item_code where i.dis_price>=50000 group by r.main_category;


 