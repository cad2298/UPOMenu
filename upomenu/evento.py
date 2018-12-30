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

class evento(osv.Model):
    _name = 'evento'
    _description = 'Eventos contratados'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'fecha':fields.date('Fecha'),
            'lugar':fields.char('Lugar'),
            'numComensales':fields.integer('Numero de comensales'),
            'numEmpleados':fields.integer('Numero de empleados'),
            'duracion':fields.integer('Duracion (minutos)'),
            'tipo':fields.selection([('boda', 'Boda'),
                                    ('bautizo', 'Bautizo'),
                                    ('comunion', 'Comunion'),
                                    ('aniversaio', 'Aniversario'),
                                    ('otro', 'Otro')],'Tipo'),
            'menu_ids':fields.many2many('menu', 'menu_evento_rel', 'evento_id', 'menu_id', 'Menus'),
            # 'personal_ids':fields.many2many('personal','personal_evento_rel','evento_id','personal_id','Personal'),
            'cliente_id':fields.many2one('cliente','Cliente'),
            'finca_id':fields.many2one('finca','Finca'),           
            
        }
