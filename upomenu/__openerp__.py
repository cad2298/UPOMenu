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
{
    "name": "UPOMenu",
    "version": "1.0",
    "depends": ["base"],
    "author": "Grupo02",
    "category": "Catering",
    "description": """Module to manage a catering service
    """,
    "init_xml": [],
    'update_xml': [],
    'demo_xml': [],
    'data': ['menu_view.xml','evento_view.xml','bebida_view.xml', 'plato_view.xml', 'ingrediente_view.xml', 'platosmenu_view.xml',
             'bebidasmenu_view.xml','comedor_view.xml','personal_view.xml','empleado_view.xml','encargado_view.xml','cocinero_view.xml','finca_view.xml','cliente_view.xml','calendario_de_menus_view.xml',
            'workflow/evento_workflow.xml', 'workflow/menu_workflow.xml',
            ],
    'demo':['demo/demo_bebida.xml',
            'demo/demo_bebidasmenu.xml',
            'demo/demo_finca.xml',
            'demo/demo_ingrediente.xml',
            'demo/demo_cliente.xml',
            'demo/demo_encargado.xml',
            'demo/demo_empleado.xml',
            'demo/demo_cocinero.xml',
            'demo/demo_plato.xml',
            'demo/demo_platosmenu.xml',
            'demo/demo_menu.xml',
            'demo/demo_calendario_de_menus.xml',
            'demo/demo_comedor.xml',
            'demo/demo_evento.xml',],
    'installable': True,
    'active': False,
#    'certificate': 'certificate',
}