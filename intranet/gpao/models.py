from django.db import models

# Create your models here.
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
    designation = models.CharField(max_length=100, verbose_name=u"Désignation:")
    categorie = models.CharField(max_length=2,choices=CATEGORIE_NM,default=ASSY_SYSTEM,verbose_name=u"Catégorie de NM:")
    liens = models.ManyToManyField('self', through='LienNM', symmetrical=False, related_name='related_to')
    
    def __unicode__(self):
        return u"%s - %s" % (self.reference,self.designation)
        
#class Piece(models.Model):
#    LETTER = 'LT'
#    A4 = 'A4'
#    OTHER = 'OT'
#    PAPER_FORMATS = (
#        (LETTER, 'Letter'),
#        (A4, 'A4'),
#        (OTHER, 'Autre'),
#    )
#    reference = models.CharField(max_length=30, unique=True, verbose_name=u"# Référence:")
#    designation = models.CharField(max_length=100, verbose_name=u"Désignation:")
#    date = models.DateField(default=datetime.date.today, verbose_name=u"Date:")
#    format_papier = models.CharField(max_length=2,choices=PAPER_FORMATS,default=LETTER,verbose_name=u"Format papier:")
#    ref_commercial = models.CharField(max_length=30, verbose_name=u"Référence commercial:")
#    ref_mecanique = models.CharField(max_length=30, verbose_name=u"Référence mécanique:")
#    brute = models.CharField(max_length=30, verbose_name=u"Brute:")
        
class LienNM(models.Model):
    from_nm = models.ForeignKey(Nm, related_name='from_nm')
    to_nm = models.ForeignKey(Nm, related_name='to_nm',verbose_name=u"Lié à NM:")
    numero_pe = models.IntegerField(max_length=6,verbose_name=u"# sur le PE:")
    quantite = models.IntegerField(max_length=6,verbose_name=u"Quantité:")
    
    def __unicode__(self):
        return u"%s linkto %s" % (self.from_nm,self.to_nm)