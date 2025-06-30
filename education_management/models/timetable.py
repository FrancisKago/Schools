from odoo import models, fields


class TimetableRoom(models.Model):
    _name = 'education.timetable.room'
    _description = 'Timetable Room'

    name = fields.Char(required=True)
    capacity = fields.Integer()


class TimetableSlot(models.Model):
    _name = 'education.timetable.slot'
    _description = 'Timetable Slot'

    name = fields.Char(required=True)
    start_time = fields.Float()
    end_time = fields.Float()


class TimetableSchedule(models.Model):
    _name = 'education.timetable.schedule'
    _description = 'Timetable Schedule'

    room_id = fields.Many2one('education.timetable.room')
    slot_id = fields.Many2one('education.timetable.slot')
    course_id = fields.Many2one('education.course')
    teacher_id = fields.Many2one('res.users')
