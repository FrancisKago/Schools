from odoo import models, fields


class LibraryBook(models.Model):
    _name = 'education.library.book'
    _description = 'Library Book'

    name = fields.Char(required=True)
    author = fields.Char()
    isbn = fields.Char()


class LibraryLoan(models.Model):
    _name = 'education.library.loan'
    _description = 'Library Loan'

    book_id = fields.Many2one('education.library.book')
    student_id = fields.Many2one('student.student')
    date_borrow = fields.Date(default=fields.Date.today)
    date_return = fields.Date()
