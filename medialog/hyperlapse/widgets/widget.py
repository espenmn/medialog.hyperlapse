import zope.component
import zope.interface
import zope.schema.interfaces

from z3c.form import interfaces
from z3c.form import widget
from z3c.form.browser import text


class IFootballWidget(interfaces.IWidget):
    """Footballfield widget."""


class FootballWidget(text.TextWidget):
    maxlength = 255
    size = 30
    
    zope.interface.implementsOnly(IFootballWidget)
    
    def getJS(self):
        return """jQuery(document).ready(function() {
            
            // for ie9 doesn't support debug console >>>
                         
            }(jQuery));
            """

def FootballFieldWidget(field, request):
    """IFieldWidget factory for FootballWidget."""
    return widget.FieldWidget(field, FootballWidget(request))
