from django.urls import path
from .views import CourseRetrieveUpdateDestroy, TeacherRetrieveUpdateDestroy, StudentRetrieveUpdateDestroy
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenVerifyView

urlpatterns = [
    path('api/course-retrieve/', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve'),
    path('api/teacher-retrieve/', TeacherRetrieveUpdateDestroy.as_view(), name='teacher-retrieve'),
    path('api/student-retrieve/', StudentRetrieveUpdateDestroy.as_view(), name='student-retrieve'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
