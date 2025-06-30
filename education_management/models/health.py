from odoo import models, fields


class HealthRecord(models.Model):
    _name = 'education.health'
    _description = 'Health Record'

    student_id = fields.Many2one('student.student')
    description = fields.Text()
    date = fields.Date(default=fields.Date.today)
