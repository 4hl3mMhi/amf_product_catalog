# -*- coding: utf-8 -*-
#############################################################################
#
#    Author: Ahlem Mehri
#
#    You can modify it under the terms of the GNU AFFERO
#    GENERAL PUBLIC LICENSE (AGPL v3), Version 3.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU AFFERO GENERAL PUBLIC LICENSE (AGPL v3) for more details.
#
#    You should have received a copy of the GNU AFFERO GENERAL PUBLIC LICENSE
#    (AGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
#############################################################################

{
    'name': "Product Catalog",
    'version': '16.0.1',
    'summary': """Enables the printing option for the catalog
     of single/multi products using the pre-configured 
     document layout in the settings menu.""",
    'description': """Enables the printing option for the catalog
     of single/multi products using the pre-configured 
     document layout in the settings menu.
==================================================================
Features:
    * Printing Capability: Enable the printing option for product catalog.
    * Product Versatility: Create catalogs for both single and multi-products.
    * Customized Layouts: Utilize pre-configured document layout available in the settings menu for tailored catalog designs.
     
     """,
    'category': 'Sales/Sales',
    'author': 'Ahlem Mehri',
    'maintainer': 'Ahlem Mehri',
    'sequence': 5,
    'depends': ['base', 'sale_management'],
    'data': [
        'report/product_catalog_template.xml',
        'report/product_catalog_report.xml',
    ],
    'images': ['static/description/banner.png'],
    'assets': {
        'web.report_assets_common': [
            '/amf_product_catalog/static/src/css/catalog_style.css',
        ],
        'web.report_assets_pdf': [
            '/amf_product_catalog/static/src/css/catalog_style_pdf.css',
        ],
    },
    'license': "AGPL-3",
    'installable': True,
}
