from zope import schema
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from collective.z3cform.colorpicker.colorpicker.ColorpickerWidget
from medialog.hyperlapse.widgets.widget import FootballWidget

_ = MessageFactory('medialog.hyperlapse')


class IStreetview(form.Schema):
    """ A field for geodata (to and from)"""
	
    fromlocation = schema.TextLine(
        title = _("label_fromlocation", default=u"Starting point"),
        description = _("help_fromlocation",
                      default="Choose Startingpoint"),
    )

    tolocation = schema.TextLine(
        title = _("label_tolocation", default=u"Finishing point"),
        description = _("help_tolocation",
            default="Choose Where to finish"),
    )

    form.widget(
                fromlocation=ColorpickerWidget

                )

alsoProvides(IStreetview, IFormFieldProvider)

