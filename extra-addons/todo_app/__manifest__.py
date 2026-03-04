{
    'name': 'To-Do List',
    'version': '1.0.0',
    'summary': 'A short description of what your module does',
    'description': 'A longer description if needed.',
    'author': 'Mohamed',
    'website': 'https://example.com',
    'category': 'Tools',
    'license': 'LGPL-3',
    'depends': [
              'base', 
                ],
    'data': [
        'security/ir.model.access.csv',
        'views/base_menu.xml',
        'views/todo_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            ]
    },
    'installable': True,
  'application': True,
}