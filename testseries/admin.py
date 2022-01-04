from django.contrib import admin
from django.utils.html import format_html
from django.contrib.admin.filters import ListFilter
from course.models import Prerequisite
from testseries.models import QuizCourse, Quiz,Quesition,quizTag,quizPrerequisite, UserResponses, quizPayment, UserquizCourse,quizAttempt
# Register your models here.
class QuizAdmin(admin.StackedInline):
    model = Quiz
class QuizAdminQues(admin.StackedInline):
    model = Quesition
class QuizAdminPre(admin.StackedInline):
    model = quizPrerequisite
class QuizAdmintag(admin.StackedInline):
    model = quizTag
class QuizCourseAdmin(admin.ModelAdmin):
    inlines = [QuizAdmin]
    list_display = ['title','exam', 'designed_by', 'get_price', 'get_discount', 'no_of_quizes']
    list_filter = ("discount" , 'active','no_of_quizes')
    def get_discount(self , course):
        return f'{course.discount} %'
    
    def get_price(self , course):
        return f'₹ {course.price}'
    get_discount.short_description= "Discount"
    get_price.short_description = "Price"
class QuesitionAdmin(admin.StackedInline):
    model = Quesition
class QuizTagAdmin(admin.StackedInline):
    model = quizTag
class UserResponsesAdmin(admin.ModelAdmin):
    list_display = ['question','User','time', 'status']
class QuizAdmin(admin.ModelAdmin):
    inlines = [QuesitionAdmin,QuizTagAdmin,QuizAdminPre]
    list_display = ["name", "type","no_of_quesitions",'is_preview']
    list_filter = ('is_preview', 'is_timed')
admin.site.register(QuizCourse, QuizCourseAdmin)
admin.site.register(Quiz,QuizAdmin)
admin.site.register(UserResponses, UserResponsesAdmin)
class quizPaymentAdmin(admin.ModelAdmin):
    model = quizPayment   
    list_display = [ "order_id" , 'get_user' , 'get_course' , 'status'] 
    list_filter = ["status" , 'course']

    def get_user(self , payment):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{payment.user.id}'>{payment.user}</a>")
    

    def get_course(self , payment):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{payment.course.id}'>{payment.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"
class UserquizCourseAdminModel(admin.ModelAdmin):
    model = UserquizCourse   
    list_display = ['click' , 'get_user' , 'get_course'] 
    list_filter = ['course']

    def get_user(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/auth/user/{usercourse.user.id}'>{usercourse.user}</a>")
    
    def click(self , usercourse):
        return "Click to Open"
    

    def get_course(self , usercourse):
        return format_html(f"<a target='_blank' href='/admin/courses/course/{usercourse.course.id}'>{usercourse.course}</a>")

    get_course.short_description = "Course"
    get_user.short_description = "User"
class quizAttemptModel(admin.ModelAdmin):
    list_display = ['user', 'quiz']
    list_filter= ['user','quiz','time']
admin.site.register(quizPayment, quizPaymentAdmin)    
admin.site.register(UserquizCourse, UserquizCourseAdminModel)    
admin.site.register(quizAttempt, quizAttemptModel)