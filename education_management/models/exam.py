from odoo import models, fields


class Exam(models.Model):
    _name = 'education.exam'
    _description = 'Exam'

    name = fields.Char(required=True)
    course_id = fields.Many2one('education.course')
    date = fields.Date()


class ExamResult(models.Model):
    _name = 'education.exam.result'
    _description = 'Exam Result'

    exam_id = fields.Many2one('education.exam')
    student_id = fields.Many2one('student.student')
    score = fields.Float()
