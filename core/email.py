from djoser import email


class PasswordResetEmail(email.PasswordResetEmail):
    template_name = "core/email/password_reset.html"
