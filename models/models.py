# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ReboundTechnologyNews(models.Model):
    _name = 'rebound_technology.news'
    _description = 'Rebound Technology News'

    name = fields.Char(required=True)
    sequence = fields.Integer(default=10)
    date = fields.Date(required=True)
    news_type = fields.Selection([
        ('content', 'Content'),
        ('link', 'Link')
    ], required=True, string="News Type", default='link')
    link = fields.Text()
    description = fields.Text()

    @api.onchange('news_type')
    def _onchange_news_type(self):
        if self.news_type == 'link':
            self.description = False
        elif self.news_type == 'content':
            self.link = False

