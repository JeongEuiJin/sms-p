
from django import forms


class SmsForm(forms.Form):
    type = forms.CharField(
        max_length=20,
        # widget=forms.TextInput(
        #     attrs={
        #         'placeholder': 'sms, lms, mms',
        #     }
        # )

    )
    to = forms.CharField(
        max_length=20,
        # widget=forms.NumberInput(
        #     attrs={
        #         'placeholder': '보낼 번호입력',
        #     }
        # )

    )
    text = forms.CharField(
        max_length=50,
        # widget=forms.TextInput(
        #     attrs={
        #         'placeholder': '길이 제한 50자',
        #     }
        # )

    )
