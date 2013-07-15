#-*- coding: utf-8 -*-
from django.db import models
import datetime
from django.utils.translation.trans_real import blankout


class Piece(models.Model):
    LETTER = 'LT'
    LEDGER = 'LD'
    A4 = 'A4'
    OTHER = 'OT'
    PAPER_FORMATS = (
        (LETTER, 'Letter'),
        (LEDGER, 'Ledger'),
        (A4, 'A4'),
        (OTHER, 'Autre'),
    )
    NONE = 'XX'
    ZINC = 'ZP'
    ANODISATION = 'AN'
    PEINT = 'PE'
    PLACAGE = 'PL'
    OXIDE_NOIR = 'OB'
    BROSSE = 'BR'
    AUTRE = 'OT'
    FINITIONS = (
        (NONE, 'Aucune'),
        (ZINC, 'Zinc Plated'),
        (ANODISATION, 'Anodisation'),
        (PEINT, 'Peint'),
        (PLACAGE, 'Placage'),
        (OXIDE_NOIR, 'Oxide Noir'),
        (BROSSE, 'Brossé'),
        (AUTRE, 'Autre'),
    )
    reference = models.CharField(max_length=30, unique=True, verbose_name=u"# Référence:")
    plan = models.FileField(upload_to="PLANS DE DEFINITION (X__-XXXX)", null=True, blank=True)
    designation = models.CharField(max_length=100, verbose_name=u"Désignation:")
    date = models.DateField(default=datetime.date.today, verbose_name=u"Date:")
    format_papier = models.CharField(max_length=2, choices=PAPER_FORMATS, default=LETTER,
                                     verbose_name=u"Format papier:")
    ref_commercial = models.CharField(max_length=30, verbose_name=u"Référence commercial:", default='XXX')
    ref_mecanique = models.CharField(max_length=30, verbose_name=u"Référence mécanique:", default='XXX')
    brute = models.CharField(max_length=30, verbose_name=u"Brute:", default='XXX')
    soudure = models.BooleanField(verbose_name=u"Soudure:")
    finition = models.CharField(max_length=2, choices=FINITIONS, default=NONE, verbose_name=u"Finition:")
    commentaires = models.CharField(max_length=200, verbose_name=u"Commentaires:", null=True, blank=True)
    
    def __unicode__(self):
        return u"%s - %s" % (self.reference, self.designation)

    class Meta:
        verbose_name = "Pièce"
        verbose_name_plural = "Pièces"


class Pe(models.Model):
    reference = models.CharField(max_length=30, unique=True, verbose_name=u"# Référence:")
    plan = models.FileField(upload_to="PLANS D'ENSEMBLE (PE-XXXX)")

    def __unicode__(self):
        return u"%s" % self.reference

    class Meta:
        verbose_name = "Plan d'ensemble"
        verbose_name_plural = "Plan d'ensembles"


class Nm(models.Model):
    ASSY_SYSTEM = 'AS'
    WIRING_PNEUMATIC = 'WP'
    WIRING_ELECTRIC = 'WE'
    MACHINE = 'MA'
    SOFTWARE = 'SO'
    RETROFIT = 'RF'
    MODERNISATION = 'MO'
    REPARATION = 'RE'
    SETUP_CLAMP = 'SC'
    CATEGORIE_NM = (
        (ASSY_SYSTEM, 'Assy System'),
        (WIRING_PNEUMATIC, 'Wiring Pneumatic'),
        (WIRING_ELECTRIC, 'Wiring Electric'),
        (MACHINE, 'Machine'),
        (SOFTWARE, 'Software'),
        (RETROFIT, 'Rétrofit'),
        (MODERNISATION, 'Modernisation'),
        (REPARATION, 'Réparation'),
        (SETUP_CLAMP, 'Setup Clamp'),
    )
    reference = models.CharField(max_length=30, unique=True, verbose_name=u"# Référence:")
    pe = models.ForeignKey(Pe, null=True, blank=True)
    designation = models.CharField(max_length=100, verbose_name=u"Désignation:")
    categorie = models.CharField(max_length=2, choices=CATEGORIE_NM, default=ASSY_SYSTEM,
                                 verbose_name=u"Catégorie de NM:")
    liens = models.ManyToManyField('self', through='LienNM', symmetrical=False, related_name='related_to')
    liens_piece = models.ManyToManyField(Piece, through='LienPiece', symmetrical=False, related_name='related_piece')
    
    def __unicode__(self):
        return u"%s - %s" % (self.reference,self.designation)
        
    def get_liensnm(self):
        return LienNM.objects.filter(from_nm=self)
        
    def get_lienspiece(self):
        return LienPiece.objects.filter(from_nm=self)

    class Meta:
        verbose_name = "Nomenclature"
        verbose_name_plural = "Nomenclatures"


class LienNM(models.Model):
    from_nm = models.ForeignKey(Nm, related_name='from_nm')
    to_nm = models.ForeignKey(Nm, related_name='to_nm', verbose_name=u"Lié à NM:")
    numero_pe = models.IntegerField(max_length=6, verbose_name=u"# sur le PE:")
    quantite = models.IntegerField(max_length=6, verbose_name=u"Quantité:")
    
    def __unicode__(self):
        return u"%s linkto %s" % (self.from_nm,self.to_nm)


class LienPiece(models.Model):
    from_nm = models.ForeignKey(Nm, related_name='from_nm_p')
    to_piece = models.ForeignKey(Piece, related_name='to_piece', verbose_name=u"Lié à Pièce:")
    numero_pe = models.IntegerField(max_length=6, verbose_name=u"# sur le PE:")
    quantite = models.IntegerField(max_length=6, verbose_name=u"Quantité:")
    
    def __unicode__(self):
        return u"%s linkto %s" % (self.from_nm,self.to_piece)