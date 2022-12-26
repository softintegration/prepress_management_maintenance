# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import UserError


class PrepressCuttingDie(models.Model):
    _inherit = 'prepress.cutting.die'

    equipment_ids = fields.Many2many('maintenance.equipment','prepress_cutting_die_equipment_rel',string='Equipments',
                                     states={'draft': [('readonly', False)]}, readonly=True)