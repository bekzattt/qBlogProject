from django.contrib import admin
# from models import Post, Comment
from models import *
# from qblogproj.post import PostResource
# from qblogproj.comment.api import CommentResource

# from . import models
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)

from django.contrib.auth.models import User, Group
admin.site.unregister(User)
admin.site.unregister(Group)


