from __future__ import unicode_literals

from sentry.plugins.bases.notify import NotifyPlugin
from twilio.rest import Client


class TwilioPlugin(NotifyPlugin):
    author = 'Luis Nell'
    author_url = 'https://github.com/originell/sentry-twilio'
    version = '1.0'
    resource_links = [
        ('Bug Tracker', 'https://github.com/originell/sentry-twilio/issues'),
        ('Source', 'https://github.com/originell/sentry-twilio'),
    ]
    title = 'Twilio'
    conf_key = 'twilio'
    conf_title = title
    slug = 'twilio'
    description = 'Send notifications via Twilio Programmable SMS.'

    def is_configured(self, project):
        return (bool(self.get_option('account_sid', project))
                and bool(self.get_option('auth_token', project))
                and bool(self.get_option('phone_number', project)))

    def get_config(self, **kwargs):
        return [
            {
                'name': 'account_sid',
                'label': 'Account SID',
                'type': 'string',
                'placeholder': 'e.g. AA0000eeee0000000cc00000b00eeccc00',
                'required': True,
                'help': 'Your Twilio Account SID.',
            },
            {
                'name': 'auth_token',
                'label': 'Auth Token',
                'type': 'secret',
                'placeholder': 'e.g. AA0000eeee0000000cc00000b00eeccc00',
                'required': True,
                'help': 'Your Twilio Auth Token.',
            },
            {
                'name': 'phone_number',
                'label': 'SMS Number',
                'type': 'string',
                'placeholder': 'e.g. +10110010001',
                'required': True,
                'help': 'Your Twilio Phone Number with Programmable SMS support.',
            },
            {
                'name': 'recipients',
                'label': 'Recipients',
                'type': 'string',
                'placeholder': 'e.g. +10110011010, +436660000,...',
                'required': True,
                'help': ('A comma separated list of notification recipient\'s'
                         'phone numbers. Note that if you have a Twilio Trial'
                         'Account, these numbers need to be verified first.'),
            },
        ]

    def notify_users(self, group, event, fail_silently=False):
        project = group.project
        if not self.is_configured(project):
            return

        twilio_account_sid = (self.get_option('account_sid', project) or '').strip()
        twilio_auth_token = (self.get_option('auth_token', project) or '').strip()
        twilio_number = (self.get_option('phone_number', project) or '').strip()
        twilio_recipients = [recp.strip() for recp in
                             (self.get_option('recipients', project) or '').split(',')]

        twilio_client = Client(twilio_account_sid, twilio_auth_token)
        msg = event.message_short.encode('utf-8')
        for recp in twilio_recipients:
            twilio_client.messages.create(body=msg, to=recp, from_=twilio_number)
