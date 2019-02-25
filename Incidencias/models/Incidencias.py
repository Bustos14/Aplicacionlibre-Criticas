#-*- coding: utf-8 -*-
from openerp import models, fields, api

class Aplicacionejemplo01Task(models.Model):
    _name = 'aplicacionejemplo01.task'
    name = fields.Char('Nombre del restaurante', required=True)
    name2 = fields.Text('Observaciones')
    name3 = fields.Date('Fecha', required=True)
    comboBo = fields.Selection([('Muy buena','Muy buena'),('Normal','Normal'),('Mala','Mala')],string='Experiencia',required=True)
    prioridad = fields.Selection([('0', 'Horrible'),('1', 'Muy Bajo'),('2','Bajo'),('3','Normal'),('4','Alto'), ('5','Excelente')],string='Nota')
    

    @api.one  
    def do_toggle_done(self):
        self.is_done = not self.is_done
        return True

    @api.multi
    def do_clear_done(self):
        done_recs = self.search([('is_done', '=', True)])
        done_recs.write({'active': False})
        return True
