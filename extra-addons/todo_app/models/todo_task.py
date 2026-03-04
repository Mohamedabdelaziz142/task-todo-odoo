from odoo import models, fields

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do'

    name = fields.Char(string='Task Name', required=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    ], string='Status', default='new')



  
    def action_new(self):
        for rec in self:
            rec.state = 'new'

    def action_in_progress(self):
        for rec in self:
            rec.write({
                'state': 'in_progress'})


    def action_completed(self):
        for rec in self:
            rec.state = 'completed'