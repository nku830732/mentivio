from django.contrib import admin
from django.contrib.admin.views.main import SEARCH_VAR
from django.utils.html import format_html
from django.contrib.admin.filters import ListFilter
from blog.models import Career_Oppotunitie,Common_strategie,Common_strategieTag,Career_OppotunitieTag,Career_Oppotunitie_Comment,Oppotunitie_Comment_Reply,strategyQuesition,strategyQuesitionReply,blogAds,adsTag
# Register your models here.
class Common_strategieTagAdmin(admin.StackedInline):
    model= Common_strategieTag
class adsTagAdmin(admin.StackedInline):
    model= adsTag
class strategyQuesitionReplyAdmin(admin.StackedInline):
    model=strategyQuesitionReply
class Career_OppotunitieTagAdmin(admin.StackedInline):
    model= Career_OppotunitieTag
class Career_Oppotunitie_CommentAdmin(admin.StackedInline):
    model= Career_Oppotunitie_Comment
class Oppotunitie_Comment_ReplyAdmin(admin.StackedInline):
    model= Oppotunitie_Comment_Reply
class Common_strategieAdmin(admin.ModelAdmin):
    inlines = [Common_strategieTagAdmin]
    list_display =('title', 'suggested_by', 'exam')
class Common_opportunitieAdmin(admin.ModelAdmin):
    inlines = [Career_OppotunitieTagAdmin]
    list_display =('name','suggested_by','exam_to_qualify')
class Career_Oppotunitie_CommentAdmin(admin.ModelAdmin):
    list_display = ('sr_no','user', 'time')
    list_filter = ['time']
    inlines = [Oppotunitie_Comment_ReplyAdmin]
class strategyQuesitionAdmin(admin.ModelAdmin):
    inlines = [strategyQuesitionReplyAdmin]
    list_display = ('user', 'time')
    list_filter = ('time',)  
class blogAdsAdmin(admin.ModelAdmin): 
       list_display=('title', 'time')
       list_filter = ('time',)
       inlines = [adsTagAdmin]
admin.site.register(Common_strategie, Common_strategieAdmin)
admin.site.register(Career_Oppotunitie,Common_opportunitieAdmin)
admin.site.register(Career_Oppotunitie_Comment,Career_Oppotunitie_CommentAdmin)
admin.site.register(strategyQuesition,strategyQuesitionAdmin)
admin.site.register(blogAds, blogAdsAdmin)
