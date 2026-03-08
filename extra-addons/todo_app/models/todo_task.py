from odoo import models, fields, api
from odoo.exceptions import ValidationError

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To Do'
    _inherit = 'mail.thread'

    name = fields.Char(string='Task Name', required=True)
    assigned_to = fields.Many2one('res.users', string='Assigned To')
    description = fields.Text(string='Description')
    due_date = fields.Date(string='Due Date')
    estimated_time = fields.Float(string='Estimated Time (hours)')
    line_ids = fields.One2many('todo.lines', 'task_id', string='Task Lines')
    total_time = fields.Float(string='Total Time (hours)', compute='_compute_total_time')
    active = fields.Boolean(string='Active', default=True)
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('close', 'Close')
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


    def action_close(self):
        for rec in self:
            rec.state = 'close'

    @api.depends('line_ids.time_spent')  
    def _compute_total_time(self):
        for rec in self:
            rec.total_time = sum(rec.line_ids.mapped('time_spent'))

    @api.constrains('line_ids', 'estimated_time')
    def _check_time(self):
        for rec in self:        
            if rec.total_time > rec.estimated_time:
                raise ValidationError("Total time spent cannot exceed estimated time.")
            

class TodoLines(models.Model):
    _name = 'todo.lines'
    _description = 'To Do Lines'

    task_id = fields.Many2one('todo.task', string='Task')    
    description = fields.Text(string='Description')
    time_spent = fields.Float(string='Time Spent (hours)')
      
      
  
