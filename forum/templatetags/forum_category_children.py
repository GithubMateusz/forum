from django import template

register = template.Library()


@register.inclusion_tag('forum/category_children.html')
def forum_category_children(category):
    children = category.children.all()
    return {'children': children}

