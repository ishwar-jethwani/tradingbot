from allauth.account.adapter import DefaultAccountAdapter


class CustomAccountAdapter(DefaultAccountAdapter):
    "This Is Adapter for user saving with additional fields"
    def save_user(self, request, user, form, commit=False):
        user = super().save_user(request, user, form, commit)
        data = form.cleaned_data
        user.first_name = data.get("first_name") 
        user.last_name = data.get("last_name")
        user.is_verified = data.get("is_verified")
        user.save()
        return user