from allauth.account.forms import LoginForm
class MyCustomLoginForm(LoginForm):
    
    def __int__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields.values():
            field.widget.attrs["class"] = "form-control my-3"
        