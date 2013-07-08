# admin.py
from django.contrib import admin
from gpao.models import Nm, LienNM, LienPiece, Piece

class LienNMInline(admin.TabularInline):
    model = LienNM
    fk_name = 'from_nm'
    extra = 0

class LienPieceInline(admin.TabularInline):
    model = LienPiece
    fk_name = 'from_nm'
    extra = 0

class NmAdmin(admin.ModelAdmin):
    inlines = [LienNMInline, LienPieceInline]
    list_display = ('reference','designation','categorie',)
    list_filter    = ('categorie',)

class PieceAdmin(admin.ModelAdmin):
    list_display = ('reference','designation','date','format_papier','ref_commercial','ref_mecanique','brute','soudure','finition','commentaires')
    
admin.site.register(Nm, NmAdmin)
admin.site.register(Piece, PieceAdmin)