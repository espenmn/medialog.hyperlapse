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
    
    import pdb; pdb.set_trace()
    print field
    
    def javascript(self):
        return """jQuery(document).ready(function() {
            
            var options = {
          map: ".map_canvas",
          formatted_address: "geocomplete",
          details: "form ",
          markerOptions: {
            draggable: true
          }
        };
        
        $(".football").geocomplete(options)
          .bind("geocode:result", function(event, result){
            $.log("Result: " + result.formatted_address);
          })
          .bind("geocode:error", function(event, status){
            $.log("ERROR: " + status);
          })
          .bind("geocode:multiple", function(event, results){
            $.log("Multiple: " + results.length + " results found");
          });
        
        $(".footballfield").bind("geocode:dragged", function(event, latLng){
          $("input[name=lat]").val(latLng.lat());
          $("input[name=lng]").val(latLng.lng());
          $("#reset").show();
        });
        
        $("#find").click(function(){
          $(".footballfield").trigger("geocode");
        });
        
        $("#examples a").click(function(){
          $(".footballfield").val($(this).text()).trigger("geocode");
          return false;
        });
        
      });
    """

def FootballFieldWidget(field, request):
    """IFieldWidget factory for FootballWidget."""
    return widget.FieldWidget(field, FootballWidget(request))
