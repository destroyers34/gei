# admin.py
from django.contrib import admin
from gpao.models import Nm, LienNM, LienPiece, Piece, Pe, Famille


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
    list_display = ('reference', 'pe', 'designation', 'categorie',)
    list_filter = ('categorie',)


class PieceAdmin(admin.ModelAdmin):
    list_display = ('reference', 'plan', 'designation', 'date', 'format_papier', 'ref_commercial', 'ref_mecanique',
                    'brute',
                    'soudure', 'finition', 'commentaires')


class PeAdmin(admin.ModelAdmin):
    list_display = ('reference', 'plan')


class FamilleAdmin(admin.ModelAdmin):
    list_display = ('reference', 'designation')


admin.site.register(Nm, NmAdmin)
admin.site.register(Piece, PieceAdmin)
admin.site.register(Pe, PeAdmin)
admin.site.register(Famille, FamilleAdmin)