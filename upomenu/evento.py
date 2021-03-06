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
from datetime import datetime
from dateutil import parser

class evento(osv.Model):
    _name = 'evento'
    _description = 'Eventos contratados'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'price':fields.integer('Precio'),
            'fecha':fields.datetime('Fecha inicio', default=datetime.now()),
            'duracion':fields.float('Duracion (horas)'),
            'lugar':fields.char('Lugar'),
            'numComensales':fields.integer('Numero de comensales'),
            'numEmpleados':fields.integer('Numero de empleados'),
            'tipo':fields.selection([('boda', 'Boda'),
                                    ('bautizo', 'Bautizo'),
                                    ('comunion', 'Comunion'),
                                    ('aniversaio', 'Aniversario'),
                                    ('otro', 'Otro')], 'Tipo'),
            'menu_ids':fields.many2many('menu', 'menu_evento_rel', 'evento_id', 'menu_id', 'Menus'),
            'personal_ids':fields.many2many('personal', 'personal_evento_rel', 'evento_id', 'personal_id', 'Personal'),
            'cliente_id':fields.many2one('cliente', 'Cliente'),
            'finca_id':fields.many2one('finca', 'Finca'),
            'state':fields.selection([('nuevo', 'Nuevo'), ('presupuesto', 'Realizar presupuesto'), ('negociacion', 'Negociación'), ('pendiente', 'Pendiente de pago'),
                                      ('pagado', 'Pagado'), ('devolucion', 'Devolución del pago'), ('realizado', 'Realizado'), ('cancelado', 'Cancelado')], 'Estado'),
        }
    
    _defaults = {'state':'nuevo'}
    _sql_constraints = [('name_uniq', 'unique (name)', 'El nombre de la clase ya existe')]
    
    def reset_data(self,cr,uid,ids,context=None):
        resultado = self
        resultado.write(cr,uid,ids,{'price':'0'}, context=None)
        resultado.write(cr,uid,ids,{'fecha':datetime.now()}, context=None)
        resultado.write(cr,uid,ids,{'duracion':'1'}, context=None)
        resultado.write(cr,uid,ids,{'lugar':''}, context=None)
        resultado.write(cr,uid,ids,{'numComensales':'0'}, context=None)
        resultado.write(cr,uid,ids,{'numEmpleados':'0'}, context=None)
        resultado.write(cr,uid,ids,{'tipo':''}, context=None)
        resultado.write(cr,uid,ids,{'state':'nuevo'}, context=None)
        resultado.write(cr,uid,ids,{'menu_ids':[ (5,  ) ]}, context=None)
        resultado.write(cr,uid,ids,{'personal_ids':[ (5,  ) ]}, context=None)
        resultado.write(cr,uid,ids,{'cliente_id':''}, context=None)
        resultado.write(cr,uid,ids,{'finca_id':''}, context=None)
        return resultado
    
    def _check_date_start(self, cr, uid, ids):
        for evento in self.browse(cr, uid, ids):
            if not evento:
                if parser.parse(evento.fecha) < datetime.now():
                    return False
        return True
    
    def _check_price(self, cr, uid, ids): 
        for evento in self.browse(cr, uid, ids):
            if evento.price < 0:
                return False
        return True
        
    _constraints = [(_check_price, 'El precio no puede ser negativo.', ['price']),
                    (_check_date_start, 'Error: La fecha de inicio no puede ser anterior a la actual.', ['fecha']), ] 
    
    
     
    
