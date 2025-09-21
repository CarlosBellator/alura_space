from django import forms

class LoginForm(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: João Silva'}))
    senha = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha'}))
    
class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        max_length=100,
        widget=forms.TextInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: João Silva'}))
    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget=forms.EmailInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Ex.: joaosilva@xpto.com'})
        )
    senha_1 = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha'}))
    senha_2 = forms.CharField(
        label='Confirme a Senha',
        widget=forms.PasswordInput(
            attrs={'class': 'form-control',
                   'placeholder': 'Digite sua senha novemante'}))
    
