from django import forms


class DonorSearch(forms.Form):
    blood_group_s_choice = (
        ("empty" , "Select Blood group or Plasma"),
        ("a+ plasma" , "A+ PLASMA"),
        ("a- plasma" , "A- PLASMA"),
        ("b+ plasma" , "B+ PLASMA"),
        ("b- plasma" , "B- PLASMA"),
        ("o+ plasma" , "O+ PLASMA"),
        ("o- plasma" , "O- PLASMA"),
        ("ab+ plasma" , "AB+ PLASMA"),
        ("ab- plasma" , "AB- PLASMA"),
        ("a+" , "A+"),
        ("a-" , "A-"),
        ("b+" , "B+"),
        ("b-" , "B-"),
        ("o+" , "O+"),
        ("o-" , "O-"),
        ("ab+" , "AB+"),
        ("ab-" , "AB-"),
    )
    select_blood_group = forms.ChoiceField(
        choices=blood_group_s_choice,
        widget=forms.Select(
            attrs={'class':'form-control',
            'required':'True',
            },
            ),
    )

    select_location = forms.CharField(
        widget=forms.TextInput(
            attrs={'class':'form-control',
            'required':'True', 
            'placeholder':'where do you need?. e.g. Mysuru'
            }
        ),
    )
    

