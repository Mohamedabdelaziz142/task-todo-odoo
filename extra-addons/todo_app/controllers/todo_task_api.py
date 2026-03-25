from odoo import http
from odoo.http import request 
import json
import math


class TodoTaskApi(http.Controller):

  #formating the resposes
    def valid_response(self, data, status, pagination_information=None):
      response_body = {
          'message': 'successful',
          'data': data
      }
      if pagination_information: 
          response_body['pagination_information'] = pagination_information
          
      return request.make_json_response(response_body, status = status)

    def invalid_response(self, error, status):
        response_body = {
            'error': error,
        }
        return request.make_json_response(response_body, status = status)
    
    # create endpoint
    @http.route('/api/tasks/create', type='http', auth = 'user',methods=['POST'] ,csrf=False)
    def create_task(self):
      try:
        args = request.httprequest.data.decode()
        if not args:
          return self.invalid_response('Request body is required', 400)
        vals = json.loads(args)
        res = request.env['todo.task'].sudo().create(vals)
        return  self.valid_response({'id': res.id, 'name': res.name}, 200)
        
      except Exception as error:
        return self.invalid_response(str(error),400)
    
    # reading list of tasks with pagination endpint
    @http.route('/api/tasks', type='http', auth = 'user',methods=['GET'] ,csrf=False)
    def read_tasks_list(self):
      try:
          tasks_domain = []

          try:
              limit = min(int(request.params.get('limit', 5)), 100)
              page  = max(int(request.params.get('page',  1)),   1)
          except ValueError:
              return self.invalid_response('limit and page must be valid integers', 400)

          offset = (page - 1) * limit

          state_val = request.params.get('state')
          if state_val:
              tasks_domain = [('state', '=', state_val)]

          tasks_ids = request.env['todo.task'].sudo().search(tasks_domain, offset=offset, limit=limit, order='id')
          tasks_count = request.env['todo.task'].sudo().search_count(tasks_domain)

          if not tasks_ids:
              return self.invalid_response('There are no records', 404)

          return self.valid_response([{
              'id': rec.id,
              'name': rec.name,
              'assigned_to': rec.assigned_to.name if rec.assigned_to else "",
              'due_date': str(rec.due_date) if rec.due_date else "",
              'state': rec.state,
          } for rec in tasks_ids], pagination_information={
              'page': page,
              'limit': limit,
              'pages': math.ceil(tasks_count / limit),
              'count': tasks_count,
          }, status=200)

      except Exception as error:
          return self.invalid_response(str(error), 400)

  # reading a singe task endpoint
    @http.route('/api/tasks/<int:task_id>', type='http', auth = 'user',methods=['GET'] ,csrf=False)
    def read_task(self, task_id):
        try:
            task_rec = request.env['todo.task'].sudo().browse(task_id)
            if not task_rec.exists():
                return self.invalid_response('ID does not exist', 404)

            return self.valid_response({
                'id': task_rec.id,
                'name': task_rec.name,
                'ref': task_rec.ref or "",
                'description': task_rec.description or "",
                'assigned_to': task_rec.assigned_to.name if task_rec.assigned_to else "",
                'state':task_rec.state,
                'due_date': str(task_rec.due_date) if task_rec.due_date else "",
            }, status=200, pagination_information=None)
        except Exception as error:
            return self.invalid_response(str(error), 400)

  # update task endpoint   
    @http.route('/api/tasks/<int:task_id>', type='http', auth = 'user',methods=['PUT'] ,csrf=False)
    def update_task(self, task_id):
        try:
            task_rec = request.env['todo.task'].sudo().browse(task_id)
            if not task_rec.exists():
                return self.invalid_response('ID does not exist', 404)
            args = request.httprequest.data.decode()
            if not args:
                return self.invalid_response('Request body is required', 400)
            vals = json.loads(args)
            task_rec.write(vals)
            return self.valid_response({
                'id': task_rec.id,
                'name': task_rec.name,
            }, status=200, pagination_information=None)
        except Exception as error:
            return self.invalid_response(str(error), 403)

  # delete endpioint
    @http.route('/api/tasks/<int:task_id>/delete', type='http', auth = 'user',methods=['DELETE'] ,csrf=False)
    def delete_task(self, task_id):
        try:
            task_rec = request.env['todo.task'].sudo().browse(task_id)
            if not task_rec.exists():
                return self.invalid_response('ID does not exist', 404)
            task_rec.unlink()
            return self.valid_response({'message': 'Task deleted successfully'}, status=200, pagination_information=None)
        except Exception as error:
            return self.invalid_response(str(error), 400)
              
