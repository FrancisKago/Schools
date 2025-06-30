from odoo import models, fields


class CounselingSession(models.Model):
    _name = 'education.counseling'
    _description = 'Counseling Session'

    student_id = fields.Many2one('student.student')
    counselor_id = fields.Many2one('res.users')
    date = fields.Date(default=fields.Date.today)
    notes = fields.Text()
