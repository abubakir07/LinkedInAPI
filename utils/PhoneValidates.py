from django.core.validators import RegexValidator


phone_regex = RegexValidator(
        regex=r"^\+996\d{9}$",
        message="Phone number must be entered in the format: '+996123456789'."
    )