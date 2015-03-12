from tastypie.resources import ModelResource
from qblogproj.post.models import *
from tastypie.authorization import Authorization
from tastypie import fields


class PostResource(ModelResource):
    text = fields.CharField(attribute="text", use_in="list")
    is_public = fields.BooleanField(attribute="is_public", null = True, use_in="detail")
    # comments = fields.ToManyField("qblogproj.api.CommentResource", related_name='post', full=True)
    comments = fields.ToManyField("qblogproj.post.api.CommentResource", full=True, null=True, attribute=lambda bundle: Comment.objects.filter(post=bundle.obj), use_in='detail')

    class Meta:
        queryset = Post.objects.all()
        resource_name = 'post'
        authorization = Authorization()
        always_return_data = True


class CommentResource(ModelResource):
    text = fields.CharField(attribute="text", use_in="list")
    post = fields.ToOneField(PostResource, 'post')
    class Meta:
        queryset = Comment.objects.all()
        resource_name = 'comment'
        authorization = Authorization()
        always_return_data = True
