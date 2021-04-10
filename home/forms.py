from django import forms


class ContactForm(forms.Form):
    """
    Contact Form for contact link
    """
    CATEGORY = (
        ('NFP Inquiry',
         'NFP Inquiry'),
        ('DIY skincare Inquiry', 'DIY skincare Inquiry'),
        ('Female health Inquiry', 'Female health Inquiry'),
        ('Other', 'Other'),
    )

    name = forms.CharField(required=True,
                           label="Name", widget=forms.TextInput())
    email = forms.EmailField(required=True,
                             label="Email", widget=forms.EmailInput())
    subject = forms.CharField(
        label="Subject",
        widget=forms.Select(choices=CATEGORY),
    )
    message = forms.CharField(
        label="Message",
        widget=forms.Textarea(attrs={
            "rows": 7,
        })
    )

    class Meta:
        fields = ['name', 'email', 'subject', 'message']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'
