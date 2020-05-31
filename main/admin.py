from django.contrib import admin
from .models import Post
from .models import list
from .models import bokdae_apt
from .models import bokdae_office


admin.site.register(Post)
admin.site.register(list)
admin.site.register(bokdae_apt)
admin.site.register(bokdae_office)
