from odoo import models, fields


class TeacherEvaluation(models.Model):
    _name = 'education.evaluation'
    _description = 'Teacher Evaluation'

    teacher_id = fields.Many2one('res.users')
    date = fields.Date(default=fields.Date.today)
    rating = fields.Float()
    notes = fields.Text()
