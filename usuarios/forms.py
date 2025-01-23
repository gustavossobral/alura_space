from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        required=True,
        label='Nome de Login',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: Gustavo Sobral',
            }
        ),
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite a sua senha',
            }
        ),
    )

class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        required=True,
        label='Nome de Cadastro',
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: Gustavo Sobral',
            }
        ),
    )
    email = forms.EmailField(
        required=True,
        label='Email',
        max_length=100,
        widget=forms.EmailInput(
            attrs={
                'class':'form-control',
                'placeholder':'Ex.: gtvsbrl@xpto.com',
            }
        ),
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite a sua senha',
            }
        ),
    )
    senha_2 = forms.CharField(
        label='Confirme a sua senha',
        required=True,
        max_length=50,
        widget=forms.PasswordInput(
            attrs={
                'class':'form-control',
                'placeholder':'Digite novamente a sua senha',
            }
        ),
    )