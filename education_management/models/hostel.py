from odoo import models, fields


class HostelRoom(models.Model):
    _name = 'education.hostel.room'
    _description = 'Hostel Room'

    name = fields.Char(required=True)
    capacity = fields.Integer()


class HostelAssignment(models.Model):
    _name = 'education.hostel.assignment'
    _description = 'Hostel Assignment'

    student_id = fields.Many2one('student.student')
    room_id = fields.Many2one('education.hostel.room')
    date_from = fields.Date()
    date_to = fields.Date()
