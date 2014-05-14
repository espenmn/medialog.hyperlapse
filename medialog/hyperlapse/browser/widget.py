from zope.component import adapter
from zope.interface import implementer
from zope.interface import implementsOnly
from zope.schema.interfaces import IField

import z3c.form.interfaces
from z3c.form.interfaces import IFormLayer
from z3c.form.interfaces import IFieldWidget
from z3c.form.interfaces import ITextAreaWidget

from z3c.form.browser.textarea import TextAreaWidget
from z3c.form.widget import FieldWidget

from z3c.form.interfaces import DISPLAY_MODE


class PlaceFieldWidget(TextAreaWidget):
    js = None
    
    @property
    def mapid(self):
        return "%s-map" % self.view.name.replace('.', '-')
    
    def coords(self):
        return self.view.value




class IPlaceFieldWidget(ITextAreaWidget):
    """Interface for z3c.form place widget"""
    pass




@adapter(IField, IFormLayer)
@implementer(IFieldWidget)
def PlaceFieldWidget(field, request):
    """IFieldWidget factory for FormPlaceWidget."""
    return FieldWidget(field, PlaceFiledWidget(request))
