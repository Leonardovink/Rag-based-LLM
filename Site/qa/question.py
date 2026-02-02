from django import forms

class QuestionForm(forms.Form):
    question = forms.CharField(
        label="Ask a question",
        max_length=500,
        widget=forms.Textarea(attrs={
            "rows": 3,
            "placeholder": "Type your question here..."
        })
    )
