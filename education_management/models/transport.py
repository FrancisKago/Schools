from odoo import models, fields


class TransportVehicle(models.Model):
    _name = 'education.transport.vehicle'
    _description = 'Transport Vehicle'

    name = fields.Char(required=True)
    license_plate = fields.Char()
    capacity = fields.Integer()


class TransportRoute(models.Model):
    _name = 'education.transport.route'
    _description = 'Transport Route'

    name = fields.Char(required=True)
    vehicle_id = fields.Many2one('education.transport.vehicle')
    note = fields.Text()


class TransportAssignment(models.Model):
    _name = 'education.transport.assignment'
    _description = 'Transport Assignment'

    student_id = fields.Many2one('student.student')
    route_id = fields.Many2one('education.transport.route')
