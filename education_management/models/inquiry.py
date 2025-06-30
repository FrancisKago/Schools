from odoo import models, fields


class WebsiteInquiry(models.Model):
    _name = 'education.inquiry'
    _description = 'Website Inquiry'

    name = fields.Char(required=True)
    email = fields.Char()
    message = fields.Text()
    date = fields.Datetime(default=fields.Datetime.now)
