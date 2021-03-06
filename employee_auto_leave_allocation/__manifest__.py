# -*- coding: utf-8 -*-
{
    'name': "Employee Automatically Leave Allocation",
    'summary': """
       """,
    'version': '12.0.1.0.0',
    'author': "AktivSoftware",
    'website': "http://www.aktivsoftware.com",
    'category': 'Human Resources',
    'description': """
        This application controls the leave schedule of your company.
        And Allocate Leaves to newly added Employee.
    """,
    'depends': [
        'hr_holidays', 'hr'],

    'data': [
        'views/res_config_settings_views.xml',
        'views/hr_employee_views.xml'],

    'images': [
        'static/description/banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': False
}
