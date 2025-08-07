from odoo import fields, models


class ServiceOffer(models.Model):
    _name = 'odoo_product_digital.service_offer'
    _description = 'Service Offer'

    name = fields.Char(string='Name', required=True)
    capabilities = fields.Text(string='Capabilities')
    proposed_value = fields.Text(string='Proposed Value')
    catalog_entry = fields.Text(string='Catalog Entry')
    interaction_types = fields.Text(string='Interaction Types')
    expectations = fields.Text(string='Expectations')
    costs = fields.Float(string='Costs')
    sla = fields.Text(string='SLA')
    security = fields.Text(string='Security')
    consumption_rates = fields.Text(string='Consumption Rates')
