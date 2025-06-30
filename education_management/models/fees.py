from odoo import models, fields


class FeesRecord(models.Model):
    _name = 'education.fees'
    _description = 'Fees Record'

    student_id = fields.Many2one('student.student')
    amount = fields.Float(required=True)
    date = fields.Date(default=fields.Date.today)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('paid', 'Paid'),
    ], default='draft')
