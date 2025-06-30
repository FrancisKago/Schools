from odoo import models, fields


class AttendanceRecord(models.Model):
    _name = 'education.attendance'
    _description = 'Attendance Record'

    student_id = fields.Many2one('student.student', required=True)
    course_id = fields.Many2one('education.course')
    date = fields.Date(default=fields.Date.today)
    present = fields.Boolean(default=True)
