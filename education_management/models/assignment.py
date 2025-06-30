from odoo import models, fields


class Assignment(models.Model):
    _name = 'education.assignment'
    _description = 'Assignment'

    name = fields.Char(required=True)
    course_id = fields.Many2one('education.course')
    description = fields.Text()
    due_date = fields.Date()
