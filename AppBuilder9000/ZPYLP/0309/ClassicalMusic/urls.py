from django.urls import path, include

from rest_framework import routers

from . import views


urlpatterns = [
    path('', views.ClassicalMusic_home, name="ClassicalMusic_home"),
    path('add_musician/', views.ClassicalMusic_add_musician, name="ClassicalMusic_add_musician"),
    path('add_role/', views.ClassicalMusic_add_role, name="ClassicalMusic_add_role"),
    path('add_composition/', views.ClassicalMusic_add_composition, name="ClassicalMusic_add_composition"),
    path('add_multiple_movements/', views.ClassicalMusic_add_multiple_movements, name="ClassicalMusic_add_multiple_movements"),
    path('add_release/', views.ClassicalMusic_add_release, name="ClassicalMusic_add_release"),
    path('add_tracks/', views.ClassicalMusic_add_tracks, name="ClassicalMusic_add_tracks"),
    path('add_default_data/', views.ClassicalMusic_add_default_data, name="ClassicalMusic_add_default_data"),


    path('musicians/', views.ClassicalMusic_show_musicians, name="ClassicalMusic_show_musicians"),
    path('compositions/', views.ClassicalMusic_show_compositions, name="ClassicalMusic_show_compositions"),
    path('releases/', views.ClassicalMusic_show_releases, name="ClassicalMusic_show_releases"),
    path('roles/', views.ClassicalMusic_show_roles, name="ClassicalMusic_show_roles"),

    path('musician/<int:pk>/details/', views.ClassicalMusic_details_musician, name='ClassicalMusic_details_musician'),
    path('composition/<int:pk>/details/', views.ClassicalMusic_details_composition, name='ClassicalMusic_details_composition'),
    path('release/<int:pk>/details/', views.ClassicalMusic_details_release, name='ClassicalMusic_details_release'),

    path('musician/<int:pk>/edit/', views.ClassicalMusic_edit_musician, name='ClassicalMusic_edit_musician'),
    path('role/<int:pk>/edit/', views.ClassicalMusic_edit_role, name='ClassicalMusic_edit_role'),
    path('composition/<int:pk>/edit/', views.ClassicalMusic_edit_composition, name='ClassicalMusic_edit_composition'),
    path('composition/<int:c_pk>/movement/<int:m_pk>/edit/', views.ClassicalMusic_edit_movement, name='ClassicalMusic_edit_movement'),
    path('composition/<int:pk>/add_movements/', views.ClassicalMusic_add_additional_movement, name='ClassicalMusic_add_additional_movement'),
    path('release/<int:pk>/edit/', views.ClassicalMusic_edit_release, name='ClassicalMusic_edit_release'),
    path('release/<int:pk>/edit_tracks/', views.ClassicalMusic_edit_tracks, name='ClassicalMusic_edit_tracks'),
    path('release/<int:pk>/add_track/', views.ClassicalMusic_add_additional_track, name='ClassicalMusic_add_additional_track'),

    path('musician/<int:pk>/delete/', views.ClassicalMusic_delete_musician, name='ClassicalMusic_delete_musician'),
    path('role/<int:pk>/delete/', views.ClassicalMusic_delete_role, name='ClassicalMusic_delete_role'),
    path('composition/<int:pk>/delete/', views.ClassicalMusic_delete_composition, name='ClassicalMusic_delete_composition'),
    path('release/<int:pk>/delete/', views.ClassicalMusic_delete_release, name='ClassicalMusic_delete_release'),
    path('release/<int:r_pk>/track/<int:t_pk>/delete/', views.ClassicalMusic_delete_track, name='ClassicalMusic_delete_track'),
    path('composition/<int:c_pk>/movement/<int:m_pk>/delete/', views.ClassicalMusic_delete_movement, name='ClassicalMusic_delete_movement'),

    path('musician/search/', views.ClassicalMusic_search_musician, name='ClassicalMusic_search_musician'),
    path('composition/search/', views.ClassicalMusic_search_composition, name='ClassicalMusic_search_composition'),
    path('release/search/', views.ClassicalMusic_search_release, name='ClassicalMusic_search_release'),
    path('role/search/', views.ClassicalMusic_search_role, name='ClassicalMusic_search_role'),

    path('musician/<str:MBID>/search/', views.ClassicalMusic_search_details_musician, name='ClassicalMusic_search_details_musician'),

    path('api/v1/musicians/', views.ClassicalMusic_api_musician_collection, name='ClassicalMusic_api_musician_collection'),
    path('api/v1/musicians/<int:pk>/', views.ClassicalMusic_api_musician_single, name='ClassicalMusic_api_musician_single'),
    path('api/v1/compositions/<int:pk>/', views.ClassicalMusic_api_composition_single, name='ClassicalMusic_api_composition_single'),

    path('TESTapi/v1/musicians/', views.ClassicalMusic_TEST_api_musician_collection, name='ClassicalMusic_TEST_api_musician_collection'),
    path('TESTapi/v1/musicians/1/', views.ClassicalMusic_TEST_api_musician_single, name='ClassicalMusic_TEST_api_musician_single'),
    path('TESTapi/v1/compositions/1/', views.ClassicalMusic_TEST_api_composition_single, name='ClassicalMusic_TEST_api_composition_single'),
    path('TESTapi/v1/musicians/POST', views.ClassicalMusic_TEST_api_musician_collection_POST, name='ClassicalMusic_TEST_api_musician_collection_POST'),
    path('TESTapi/v1/musicians/1/DELETE', views.ClassicalMusic_TEST_api_musician_single_DELETE, name='ClassicalMusic_TEST_api_musician_single_DELETE'),
    path('TESTapi/v1/musicians/2/EDIT', views.ClassicalMusic_TEST_api_musician_single_POST, name='ClassicalMusic_TEST_api_musician_single_POST'),
]
