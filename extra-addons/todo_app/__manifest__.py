{
    'name': 'To-Do List',
    'version': '1.0.0',
    'summary': 'Manage your daily tasks with ease',
    'description': 'A simple To-Do module to create, assign and track tasks.',
    'author': 'Mohamed',
    'website': 'https://example.com',
    'category': 'Tools',
    'license': 'LGPL-3',
    'depends': [
              'base',
              'mail', 
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_views.xml',
    ],
    'installable': True,
  'application': True,
}