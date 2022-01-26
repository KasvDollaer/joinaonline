from django.conf.urls import include, url
from django.conf import settings
from django.conf.urls.static import static


from . import views

app_name = 'ecommerce' # This will be like this: {% url 'ecommerce:detail' item.id %} on our templates. 
urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^money_refund/', views.moneyrefund, name='comingsoon'),
	url(r'^vendors/', views.vendors, name='index.html'),
	url(r'^career/', views.career, name='coming_soon'),
	url(r'^shipping_info/', views.shippinginfo, name='comingsoon'),
	url(r'^open_dispute/', views.opendispute, name='comingsoon'),
	url(r'^rules_and_terms/', views.rulesandterms, name='comingsoon'),
	url(r'^fing_a_store/', views.findastore, name='comingsoon'),
	url(r'^samsung/', views.Samsung, name='comingsoon'),
	url(r'^sony/', views.Sony, name='comingsoon'),
	url(r'^categories/electronics/', views.categories_electronics, name='electronics'),
	url(r'^LG/', views.LG, name='comingsoon'),
	url(r'^Philips/', views.Philips, name='comingsoon'),
	url(r'^fing_a_store/', views.findastore, name='contact'),
	url(r'^products/$', views.products, name='products'),
	url(r'^product/(?P<product_id>[0-9]+)/$', views.single_product, name='single_product'),
	url(r'^about/$', views.about, name='about'),
	url(r'^contact/$', views.contact, name='contact'),
	url(r'^cart/$', views.cart, name='cart'),
  
    url(r'^success', views.success, name = 'success'),
	url(r'^checkout/$', views.checkout, name='checkout'),
	url(r'^get_category/(?P<category_slug>\D+)/$', views.get_category, name='get_category'),
    
    url(r'^categories/', include([
        url(r'^electronics/$', views.categories_electronics, name='categories_electronics'),
        url(r'^food/$', views.categories_food, name='categories_food'),
        url(r'^women/$', views.categories_women, name='categories_women'),
        url(r'^home-kitchen/$', views.categories_homeKitchen, name='categories_women')
    ])),
    
   
    url(r'^vendors/', include([
        url(r'^index/$', views.vendors, name='vendors'),
        url(r'^search/$', views.search, name='search'),
        url(r'^stockorder/$', views.stockorder, name='stockorder')
    ])),
	

	url(r'^user/', include([
        url(r'^login/$', views.user_login, name='user_login'),
		url(r'^register/$', views.user_register, name='user_register'),
		url(r'^account/$', views.user_account, name='user_account'),
        url(r'^index/$', views.user_index, name='user_index'),
		url(r'^products/$', views.user_products, name='user_products'),
		url(r'^view_products/$', views.user_products, name='user_products'),
		url(r'^product/create/$', views.user_product_create, name='user_product_create'),
		url(r'^product/update/(?P<product_id>[0-9]+)/$', views.user_product_update, name='user_product_update'),
		url(r'^product/update/set-featured-image/$', views.set_featured_image),
		url(r'^product/update/unset-image/$', views.unset_image),
		url(r'^product/unset-product/$', views.unset_product),
		url(r'^logout/$', views.logout),
    ])),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
