# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (http://tiny.be). All Rights Reserved
#    
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see http://www.gnu.org/licenses/.
#
##############################################################################

from osv import osv
from osv import fields

class comedor(osv.Model):

    _name = 'comedor'
    _description = 'Comedor.'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True, readonly=False),
            'ubicacion':fields.char('Ubicación',required=True),
            'email':fields.char('Email', size=64),
            'calendario_de_menus_id':fields.many2one('calendario_de_menus','Calendario'),
            'personal_ids':fields.many2many('personal','comedor_personal_rel','comedor_id','personal_id','Personal'),
            }
            
    _sql_constraints = [     ('name_uniq', 'unique (name)', 'The Name of the OpenERPModel must be unique !'),
                             ('ubicacion_uniq', 'unique (name)', 'The Name of the OpenERPModel must be unique !'),
                                  ]
    