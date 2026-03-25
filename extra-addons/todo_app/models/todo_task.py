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
    is_late = fields.Boolean(string='Is Late')
    ref = fields.Char(string='Sequence', readonly=True, default='New')
    state = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
        ('close', 'Close')
    ], string='Status', default='new')

    @api.model
    def create(self,vals):
        if vals.get('ref', 'New') == 'New':
          vals['ref'] = self.env['ir.sequence'].next_by_code('todo.task')
        return super(TodoTask, self).create(vals)
    
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
            
  
    def check_due_dates(self):
        today = fields.Date.today()
        task_ids = self.search([])
        for rec in task_ids:
            if rec.due_date and rec.due_date < today and rec.state not in ('completed', 'close'):
                rec.message_post(body="Task is overdue!", subtype_xmlid='mail.mt_warning')
                rec.is_late = True
            else:
                rec.is_late = False

    def action_open_assign_wizard(self):
      return {
        'type': 'ir.actions.act_window',
        'name': 'Assign Tasks',
        'res_model': 'todo.assign.task',
        'view_mode': 'form',
        'target': 'new',
      }
    def write(self, vals):
        for rec in self:
          if rec.state in ('close', 'completed') and 'state' not in vals:
               raise ValidationError("Cannot update a completed or closed task!")
        return super(TodoTask, self).write(vals)         
      
class TodoLines(models.Model):
    _name = 'todo.lines'
    _description = 'To Do Lines'

    task_id = fields.Many2one('todo.task', string='Task')    
    description = fields.Text(string='Description')
    time_spent = fields.Float(string='Time Spent (hours)')
      
      
  
