from odoo import fields, models


class Contract(models.Model):
    _name = 'odoo_product_digital.contract'
    _description = 'Contract'

    name = fields.Char(string='Contract Reference', required=True)
    price = fields.Float(string='Price')
    sla = fields.Text(string='SLA')
    interaction_rules = fields.Text(string='Interaction Rules')
    governance = fields.Text(string='Governance')
    security = fields.Text(string='Security')
    expected_outcomes = fields.Text(string='Expected Outcomes')
    scoped_resources = fields.Text(string='Scoped Resources')
    service_offer_id = fields.Many2one('odoo_product_digital.service_offer', string='Service Offer')
