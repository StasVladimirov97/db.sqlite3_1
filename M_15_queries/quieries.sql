"shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp
_product"."created_at", "shopapp_product"."archived", "shopapp_product"."preview" FROM "shopapp_product" WHERE NOT "shopapp_product"."archived" ORDER BY "shopapp_p
roduct"."name" ASC, "shopapp_product"."price" ASC; args=(); alias=default

select "shopapp_product"."id", "shopapp_product"."name", "shopapp_product"."description", "shopapp_product"."price", "shopapp_product"."discount", "shopapp
_product"."created_at", "shopapp_product"."archived", "shopapp_product"."preview" from "shopapp_product" where "shopapp_product"."id" = 1 LIMIT 21; args=(1,); alia
s=default
select "shopapp_productimage"."id", "shopapp_productimage"."product_id", "shopapp_productimage"."image", "shopapp_productimage"."description" from "shopapp
_productimage" where "shopapp_productimage"."product_id" in (1); args=(1,); alias=default

select "django_session"."session_key", "django_session"."session_data", "django_session"."expire_date" from "django_session" where ("django_session"."expir
e_date" > '2023-06-19 19:40:54.681263' and "django_session"."session_key" = '3ev118643k07u1g89ym1u9iuln79yo4u') LIMIT 21; args=('2023-06-19 19:40:54.681263', '3ev1
18643k07u1g89ym1u9iuln79yo4u'); alias=default
select "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_name", "a
uth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" from "auth_user" where "auth_user"."id" = 1
LIMIT 21; args=(1,); alias=default
select "shopapp_order"."id", "shopapp_order"."delivery_address", "shopapp_order"."promocode", "shopapp_order"."created_at", "shopapp_order"."user_id", "sho
papp_order"."receipt", "auth_user"."id", "auth_user"."password", "auth_user"."last_login", "auth_user"."is_superuser", "auth_user"."username", "auth_user"."first_n
ame", "auth_user"."last_name", "auth_user"."email", "auth_user"."is_staff", "auth_user"."is_active", "auth_user"."date_joined" from "shopapp_order" inner join "aut
h_user" on ("shopapp_order"."user_id" = "auth_user"."id"); args=(); alias=default
