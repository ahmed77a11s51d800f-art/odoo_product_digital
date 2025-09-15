from odoo import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    service_offer_ids = fields.One2many(
        'odoo_product_digital.service_offer', 'product_tmpl_id', string='Service Offers')
