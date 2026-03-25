from odoo import models, fields

class AssignTask(models.TransientModel):

  _name = 'todo.assign.task'
  _description = 'assign task wizard'

  assigned_to = fields.Many2one('res.users', string='Assign To', required=True)

  def action_assign(self):
    tasks_ids =  self.env.context.get('active_ids',[])
    tasks = self.env['todo.task'].browse(tasks_ids)
    for task in tasks:
      task.assigned_to = self.assigned_to