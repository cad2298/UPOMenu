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

class menu(osv.Model):

    _name = 'menu'
    _description = 'Menus.'
    
    def _num_eventos(self, cr, uid, ids, field, arg, context=None):
        res = {} 

        # Recorre todas los menus y calcula el número de eventos asociados
        for menu in self.browse(cr, uid, ids, context=context):
            res[menu.id] = len(menu.evento_ids)
        return    res
    
    _columns = {
            'name':fields.char('Nombre', size=64, required=True, readonly=False, Translate=False),
            
            'price': fields.integer('Precio'),
            'evento_ids':fields.many2many('evento', 'evento_menu_rel', 'menu_id', 'evento_id', 'Eventos'),
            'platosmenu_ids':fields.one2many('platosmenu', 'menu_id', 'Platos del menu'),
            'bebidasmenu_ids':fields.one2many('bebidasmenu', 'menu_id', 'Bebidas del menu'),
            'calendario_de_menus_id':fields.many2one('calendario_de_menus', 'Calendario de menus'),
            'state':fields.selection([('nuevo', 'Nuevo'), ('completado', 'Completado'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], 'Estado'),
            'uso':fields.function(_num_eventos, type='integer', string='Ocupacion total', store  = True)
    }
    _defaults = {'state':'nuevo'}
    
        
    def _check_price(self, cr, uid, ids): 
        
        for clase in self.browse(cr, uid, ids):
            if clase.price <= 0:
                return False
        return True
    
    
    def _check_name(self, cr, uid, ids):
        for clase in self.browse(cr, uid, ids):
            myString = clase.name
            if myString and myString.strip():
        # myString is not None AND myString is not empty or blank
                return False
        return True
        
    _constraints = [(_check_price, 'El precio no puede ser nulo', ['price']),
                    # (_check_name, 'Nombre no válido', ['name']),
                    ]
    
    _sql_constraints = [('name_uniq', 'unique (name)', 'El nombre del menu ya existe'),
                      ]  
