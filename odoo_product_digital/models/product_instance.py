from odoo import fields, models


class ProductInstance(models.Model):
    _name = 'odoo_product_digital.product_instance'
    _description = 'Product Instance'

    name = fields.Char(string='Instance Name', required=True)
    type = fields.Selection([
        ('physical_device', 'Physical Device'),
        ('seat_login', 'Seat/Login'),
        ('shared_resource', 'Shared Resource'),
    ], string='Type', required=True)
