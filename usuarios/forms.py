# CAMPO DE CADASTRO E LOGIN

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

    # Validação para não haver espaços no nome de usuário: 
    def clean_nome_cadastro(self):
        nome = self.cleaned_data.get('nome_cadastro')

        if nome:
            nome = nome.strip()
            if ' ' in nome:
                raise forms.ValidationError('Espaços não são permitidos nesse campo')
        else:
            return nome

    # Validação da igualdade da senha e sua confirmação:
    def clean_senha_2(self):
        senha_1 = self.cleaned_data.get('senha_1')
        senha_2 = self.cleaned_data.get('senha_2')
        
        if senha_1 and senha_2:
            if senha_1 != senha_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return senha_1