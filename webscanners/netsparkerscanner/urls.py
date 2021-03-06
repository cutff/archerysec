# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from django.urls import include, path
from webscanners.netsparkerscanner import views

app_name = 'netsparkerscanner'

urlpatterns = [
    # All netsparker URL's
    path('netsparker_list_vuln/',
        views.netsparker_list_vuln,
        name='netsparker_list_vuln'),
    path('netsparker_scan_list/',
        views.netsparker_scan_list,
        name='netsparker_scan_list'),
    path('netsparker_vuln_data/',
        views.netsparker_vuln_data,
        name='netsparker_vuln_data'),
    path('netsparker_vuln_out/',
        views.netsparker_vuln_out,
        name='netsparker_vuln_out'),
    path('del_netsparker_scan/',
        views.del_netsparker_scan,
        name='del_netsparker_scan'),
    path('netsparker_del_vuln/',
        views.netsparker_del_vuln,
        name='netsparker_del_vuln'),
    path('export/',
        views.export,
        name='export'),

]
