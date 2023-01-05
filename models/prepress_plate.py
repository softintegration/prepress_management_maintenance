# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PrepressPlate(models.Model):
    _inherit = 'prepress.plate'

    equipment_ids = fields.Many2many('maintenance.equipment','prepress_plate_equipment_rel',string='Equipments',
                                     states={'draft': [('readonly', False)]}, readonly=True)