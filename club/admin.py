from django.http import HttpResponse

from django.contrib import admin, messages
from django.shortcuts import render

from .models import *

@admin.register(ClubMember)
class ClubMemberAdmin(admin.ModelAdmin):

    list_display = ('name', 'age', 'expr_years_in_sk', 'joined_at')
    list_filter = ('joined_at', 'expr_years_in_sk', 'role')
    search_fields = ('name',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):

    list_display = ('id','title', 'description', 'views')
    list_filter = ('views', 'published_at', 'updated_at')
    search_fields = ('title', 'description')

    actions = ('get_maximum_views',)

    def get_maximum_views(self, request, query_set):

        maxim = query_set.order_by('-views')[0]
        self.message_user(request, f'the news with ->  id:{maxim.id}, title:{maxim.title} , number_of_views:{maxim.views}', messages.SUCCESS)
        return maxim

    get_maximum_views.short_description = 'To show max views'


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):

    list_display = ('id',)
