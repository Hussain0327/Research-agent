from __future__ import annotations

import logging
import smtplib
from email.message import EmailMessage
from typing import Iterable

from .config import Settings


logger = logging.getLogger(__name__)


def send_email(settings: Settings, subject: str, html: str, to_addrs: Iterable[str]) -> None:
    if not (settings.smtp_host and settings.smtp_username and settings.smtp_password and settings.smtp_from):
        raise RuntimeError("SMTP settings incomplete: set SMTP host, username, password, and from address")

    msg = EmailMessage()
    msg["From"] = settings.smtp_from
    msg["To"] = ", ".join(to_addrs)
    msg["Subject"] = subject
    msg.set_content("This is an HTML newsletter. Please use an HTML-enabled client.")
    msg.add_alternative(html, subtype="html")

    logger.info("Sending email to %s via %s", to_addrs, settings.smtp_host)
    with smtplib.SMTP(settings.smtp_host, settings.smtp_port) as smtp:
        smtp.starttls()
        smtp.login(settings.smtp_username, settings.smtp_password)
        smtp.send_message(msg)

