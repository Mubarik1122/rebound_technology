# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request

class ReboundTech(http.Controller):

    @http.route('/', auth='public', website=True)
    def rebound_technology_home(self, **kw):
        return http.request.render('rebound_technology.Home')

    @http.route('/technology', auth='public', website=True)
    def technology_func(self, **kw):
        return http.request.render('rebound_technology.Technology')

    @http.route('/sustainability', auth='public', website=True)
    def sustainability_func(self, **kw):
        return http.request.render('rebound_technology.Sustainability')

    @http.route('/team', auth='public', website=True)
    def team_func(self, **kw):
        return http.request.render('rebound_technology.Team')

    @http.route('/news', auth='public', website=True)
    def news_func(self, **kw):
        news_data = []
        recs = request.env['rebound_technology.news'].sudo().search([])
        sorted_recs = sorted(recs, key=lambda rec: rec.sequence)
        for rec in sorted_recs:
            news_data.append({
                'id': rec.id,
                'title': rec.name,
                'date': [rec.date.strftime('%d'), rec.date.strftime('%b').upper()],
                'link': rec.link or False,
                'description': rec.description or False,
            })
        data = {
            'all_news': news_data
        }
        return http.request.render('rebound_technology.News', data)

    @http.route('/news/<string:news_post_title>', auth='public', website=True)
    def sub_news_func(self, news_post_title, **kw):
        news = request.env['rebound_technology.news'].sudo().search([("name", '=', news_post_title), ('news_type', '=', 'content')])
        data = {
            'news_content': news.description,
            'title': news.name,
            'creator': news.create_uid.name,
            'date': news.date.strftime('%B %d, %Y')
        }
        return http.request.render('rebound_technology.sub_news', data)

    @http.route('/contact_us', auth='public', website=True)
    def contact_us_func(self, **kw):
        return http.request.render('rebound_technology.Contact-Us')

    @http.route('/contact/form', auth='public', type='http', website=True, csrf=False)
    def email_contact_form(self, **kw):
        form_data = kw
        print('abc')
        crm_rec = request.env['crm.lead'].sudo().create({
            'name': form_data['name'],
            'email_from': form_data['email'],
            'phone': form_data['phone'],
            'description': form_data['massage'],
            'type': 'opportunity'
        })
