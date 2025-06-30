from odoo import models, fields


class SchoolEvent(models.Model):
    _name = 'education.event'
    _description = 'School Event'

    name = fields.Char(required=True)
    start_date = fields.Date()
    end_date = fields.Date()
    description = fields.Text()
