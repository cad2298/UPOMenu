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

class plato(osv.Model):

    _name = 'plato'
    _description = 'Plato.'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True, readonly=False),
            'tipo':fields.selection([('entrante', 'Entrante'),
                                     ('platoPrincipal', 'Plato principal'),
                                     ('postre', 'Postre'),
                                     ], 'Tipo de plato'),
            'precio':fields.float('Precio', digits=(6, 2)),
            'ingrediente_ids':fields.many2many('ingrediente','plato_ingrediente_rel','plato_id','ingrediente_id','Ingredientes'),
            #'platosmenu_ids':fields.one2many('platosmenu','plato_id','Platomenu'),
        }
            
