from zope.interface import implements, Interface

from Products.Five import BrowserView
from Products.CMFCore.utils import getToolByName

#from medialog.hyperlapse import hyperlapseMessageFactory as _


class IHyperlapseView(Interface):
    """
    Hyperlapse view interface
    """

    def test():
        """ test method"""


class HyperlapseView(BrowserView):
    """
    Hyperlapse browser view
    """
    implements(IHyperlapseView)

    def __init__(self, context, request):
        self.context = context
        self.request = request

    @property
    def javascript(self):
        return u"""
        <script type="text/javascript">
            
            function init() {
        
            var hyperlapse = new Hyperlapse(document.getElementById('pano'), {
                                        zoom: 1,
                                        width: 800,
                                        height: 400,
                                        use_lookat: false,
                                        elevation: 50,
                                        distance_between_points: 1,
                                        max_points: 100,
                                        millis: %(millis)s,
                                        });
                                        
                                        hyperlapse.onError = function(e) {
                                            console.log(e);
                                        };
                                        
                                        hyperlapse.onRouteComplete = function(e) {
                                            hyperlapse.load();
                                        };
                                        
                                        hyperlapse.onLoadComplete = function(e) {
                                            hyperlapse.play();
                                        };
                                        
                                        // Google Maps API stuff here...
                                        var directions_service = new google.maps.DirectionsService();
                                        
                                        var route = {
                                            request:{
                                                origin: new google.maps.LatLng(%(from)s),
                                                destination: new google.maps.LatLng(%(to)s),
                                                travelMode: google.maps.DirectionsTravelMode.DRIVING
                                        }
                                        };
                                        
                                        directions_service.route(route.request, function(response, status) {
                                                                 if (status == google.maps.DirectionsStatus.OK) {
                                                                 hyperlapse.generate( {route:response} );
                                                                 } else {
                                                                 console.log(status);
                                                                 }
                                                                 });
    
    }
    
            window.onload = init;
</script>"""  {
              'millis' : self.context.millis,
              'from'   : self.context.fromlocation,
              'to'     : self.context.tolocation,
              }

    @property
    def portal_catalog(self):
        return getToolByName(self.context, 'portal_catalog')

    @property
    def portal(self):
        return getToolByName(self.context, 'portal_url').getPortalObject()

    def test(self):
        """
        test method
        """
        dummy = _(u'a dummy string')

        return {'dummy': dummy}
