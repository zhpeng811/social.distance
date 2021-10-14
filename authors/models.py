import uuid
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse 
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Author(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    user = models.OneToOneField(User, on_delete=models.CASCADE) # one2one with django user
    friends = models.ManyToManyField('Author', blank=True, symmetrical=True) # bidirectional/symmetrical by default, allow empty

    display_name = models.CharField(max_length=30, blank=True) # maximum 30 chars for display name
    github_url = models.URLField(null=True, blank=True) # the url to the author github profile
    url = models.URLField(editable=False) # the url to the author profile
    host = models.URLField(editable=False) # the host server node url, ours is https://social-distance-api.herokuapp.com/

    # following: Authors, added by related name, see AuthorFollowingRelation
    # followers: Authors, added by related name, see AuthorFollowingRelation

    # used by serializer
    def get_public_id(self):
        return self.url or self.id

    # used internally
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    # clean up whenever trying to validate model object
    def clean(self):
        # enforce author-user one2one
        if self.user is None:
            raise ValidationError(_('Author object has to have a User object linked.'))

        # default display_name to username
        if not self.display_name:
            self.display_name = self.user.username

    # used by serializer
    def update_fields_with_request(self, request):
        self.url = request.build_absolute_uri(self.get_absolute_url())
        self.host = request.build_absolute_uri('/') # points to the server root
        self.save()

class Follower(models.Model):
    """
    Relation that represents the current Author, A, being followed by another author, B
    followee: A
    follower_url: B's url, could be external Author object url

    we use follower_url because followers could be users from external servers.
    views that use this model will need to fetch external author objects with the url.
    """

    # Author who is being followed by the follower. corresponds to Author.follower.all()
    followee = models.ForeignKey(Author, related_name="followers", null=False, on_delete=models.CASCADE)

    # URL of Author who is following the followee
    follower_url = models.URLField()

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['followee', 'follower_url'], name='unique_follower')
        ]


class Following(models.Model):
    """
    Relation that represents the current Author, A, following another author, B
    follower: A
    followee_url: B's url, could be external Author object url
    """
    # URL of the remote author who is being followed
    followee_url = models.URLField()

    # Author who is following the remote author
    follower = models.ForeignKey(Author, related_name="following", null=False, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'followee_url'], name='unique_following')
        ]


class AuthorFriendRequest(models.Model):
    """
    Request from an author who wants to befriend/follow another author.
    Once accepted, both authors can see each others' friend posts and previous friend posts.
    """
    # author who is sending the friend/following request
    author_from = models.ForeignKey("Author", related_name="friend_requests_sent", on_delete=models.CASCADE)
    # author who is receiving the request
    author_to = models.ForeignKey("Author", related_name="friend_requests_received", on_delete=models.CASCADE)
