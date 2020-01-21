from django import forms

class testimoniform(forms.Form):
    nama= forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={
                'placeholder':'Masukan nama',
            }
        ))
    email= forms.EmailField(
         widget=forms.TextInput(
            attrs={
                'placeholder':'Masukan email kamu',
            }
        )
    )
    deskripsi= forms.CharField(
        max_length=30,
        widget=forms.Textarea(
            attrs={
                'placeholder':'Masukan deskripsi',
            }
        ))
    