from zope import schema
#from plone.directives import dexterity
from plone.directives import form
from plone.autoform.interfaces import IFormFieldProvider
from zope.interface import alsoProvides
from zope.i18nmessageid import MessageFactory

from collective.z3cform.mapwidget.widget import MapFieldWidget
from .browser.widget import FormPlaceWidget

_ = MessageFactory('medialog.hyperlapse')


class IStreetview(form.Schema):
    """ A field for geodata (to and from)"""
	
    fromlocation = schema.Text(
        title = _("label_fromlocation", default=u"Starting point"),
        description = _("help_fromlocation",
                      default="Choose Startingpoint"),
    )

    tolocation = schema.Text(
        title = _("label_tolocation", default=u"Finishing point"),
        description = _("help_tolocation",
            default="Choose Where to finish"),
    )

    form.widget(
            fromlocation=MapFieldWidget,
            tolocation=MapFieldWidget,
    )

alsoProvides(IStreetview, IFormFieldProvider)

