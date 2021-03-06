# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428450710.940088
_enable_loop = True
_template_filename = '/Users/Nate/chf_dmp/homepage/templates/person.html'
_template_uri = 'person.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        people = context.get('people', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        people = context.get('people', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n<div class="text-left">\n    <h1 class="page-header">People</h1>\n</div>\n\n<div class="text-left" style="margin-bottom: 20px;">\n    <a href="/homepage/person.create/" class="btn btn-warning">Add New Person</a>\n</div>\n\n<table id="person_table" class="table table-striped">\n    <tr>\n        <th>Actions</th>\n        <th>ID</th>\n        <th>First Name</th>\n        <th>Last Name</th>\n        <th>Birth Date</th>\n        <th>Address</th>\n        <th>City</th>\n        <th>State</th>\n        <th>ZIP</th>\n        <th>Country</th>\n        <th>Phone Number</th>\n        <th>Type</th>\n        <th>Email</th>\n    </tr>\n')
        for person in people:
            __M_writer('    <tr>\n        <td>\n            <a href="/homepage/person.edit/')
            __M_writer(str( person.id ))
            __M_writer('/">Edit</a>\n            |\n            <a href="/homepage/person.delete/')
            __M_writer(str( person.id ))
            __M_writer('/">Delete</a>\n        </td>\n        <td>')
            __M_writer(str( person.id ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.given_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.last_name ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.birth_date.strftime('%b %d, %Y') ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.address.address1 ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.address.city ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.address.state ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.address.zip_code ))
            __M_writer('</td>\n        <td>')
            __M_writer(str( person.address.country ))
            __M_writer('</td>\n\n')
            if person.org_phones.count() != 0:
                for phone in person.org_phones.all():
                    __M_writer('                <td>\n                    ')
                    __M_writer(str( phone.number ))
                    __M_writer('<br/>\n                </td>\n                <td>\n                    ')
                    __M_writer(str( phone.type ))
                    __M_writer('<br/>\n                </td>\n')
            else:
                __M_writer('            <td>None</td>\n            <td>None</td>\n')
            __M_writer('\n        <td>')
            __M_writer(str( person.email ))
            __M_writer('</td>\n    </tr>\n')
        __M_writer('</table>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "/Users/Nate/chf_dmp/homepage/templates/person.html", "line_map": {"64": 38, "65": 39, "66": 39, "67": 40, "68": 40, "69": 41, "70": 41, "71": 42, "72": 42, "73": 43, "74": 43, "75": 44, "76": 44, "77": 46, "78": 47, "79": 48, "80": 49, "81": 49, "82": 52, "83": 52, "84": 55, "85": 56, "86": 59, "87": 60, "88": 60, "89": 63, "27": 0, "95": 89, "35": 1, "45": 3, "52": 3, "53": 29, "54": 30, "55": 32, "56": 32, "57": 34, "58": 34, "59": 36, "60": 36, "61": 37, "62": 37, "63": 38}, "uri": "person.html"}
__M_END_METADATA
"""
