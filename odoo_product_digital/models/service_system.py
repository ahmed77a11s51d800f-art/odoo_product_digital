from odoo import fields, models


class ServiceSystem(models.Model):
    _name = 'odoo_product_digital.service_system'
    _description = 'Service System'

    name = fields.Char(string='Name', required=True)
    people = fields.Text(string='People')
    technology = fields.Text(string='Technology')
    money = fields.Text(string='Money')
    information = fields.Text(string='Information')
    competencies = fields.Text(string='Competencies')
