from django.urls import path
from main.views import show_main, add_order_entry, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user, edit_order, delete_order, add_order_entry_ajax, create_mood_flutter

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('add_order_entry/', add_order_entry, name='add_order_entry'),
    path('add-order-entry-ajax', add_order_entry_ajax, name='add_order_entry_ajax'),
    path('edit-order/<uuid:id>', edit_order, name='edit_order'),
    path('delete/<uuid:id>', delete_order, name='delete_order'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('create-flutter/', create_mood_flutter, name='create_mood_flutter'),
]