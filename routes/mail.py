from infrastructure.runtime import Runtime


class MailRoutes:
    @staticmethod
    def inbox() -> str:
        return f"{Runtime.base_url()}/mail/inbox"

    @staticmethod
    def email(email_id: str) -> str:
        return f"{Runtime.base_url()}/mail/inbox/{email_id}"