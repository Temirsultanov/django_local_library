from django.contrib import admin

# Register your models here.
from .models import Author, Genre, Book, BookInstance, Language



admin.site.register(Genre)
admin.site.register(Language)
class BookInline(admin.StackedInline):
    model = Book
    extra = 0
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [('first_name', 'last_name'), 'date_of_birth', 'date_of_death']
    inlines = [BookInline]
admin.site.register(Author, AuthorAdmin)
class BookInstanceInline(admin.TabularInline):
    model = BookInstance
    extra = 0
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]
@admin.register(BookInstance)
class BookInstanseAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'due_back', 'id')
    list_filter = ('status', 'due_back')
    fieldsets = (
        ('Content', {
            'fields' : ('book', 'id', 'imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back','borrower')
        }),
    )
