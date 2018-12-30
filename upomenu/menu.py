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
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=False, readonly=False, Translate=False),
            'price':fields.integer('Precio'),
            'evento_ids':fields.many2many('evento', 'evento_menu_rel', 'menu_id', 'evento_id', 'Eventos'),
            'platosmenu_ids':fields.one2many('platosmenu', 'menu_id', 'Platos del menu'),
            'bebidasmenu_ids':fields.one2many('bebidasmenu', 'menu_id', 'Bebidas del menu'),
            'calendario_de_menus_id':fields.many2one('calendario_de_menus', 'Calendario de menus'),
            'state':fields.selection([('nuevo', 'Nuevo'), ('aprobado', 'Aprobado'), ('rechazado', 'Rechazado')], 'Estados'),
    }
    _defaults = {'state':'nuevo'}
        
