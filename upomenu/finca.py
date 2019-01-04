
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

class finca(osv.Model):

    _name = 'finca'
    _description = 'Fincas.'
 
    _columns = {
            'name':fields.char('Nombre', size=64, required=True),
            'ubicacion':fields.char('Ubicación', size=256, required=True),
            'aforo':fields.integer('Aforo'),
            'precio':fields.integer('Precio'),
            'conciertos':fields.boolean('Admite conciertos'),
            'exterior':fields.boolean('Exterior'),
            'evento_ids':fields.one2many('evento','finca_id','Eventos'),
                        
        }
    def _check_price(self, cr, uid, ids): 
        
        for finca in self.browse(cr, uid, ids):
            if finca.precio <=0:
                return False
        return True
    
    _constraints = [(_check_price, 'Error: precio erroneo', ['precio']), ] 