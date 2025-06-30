from odoo import models, fields


class Course(models.Model):
    _name = 'education.course'
    _description = 'Course'

    name = fields.Char(required=True)
    code = fields.Char()
    description = fields.Text()


class CourseSubject(models.Model):
    _name = 'education.subject'
    _description = 'Subject'

    name = fields.Char(required=True)
    course_id = fields.Many2one('education.course', ondelete='cascade')
