import os

from kalliope.core.NeuronModule import NeuronModule, InvalidParameterException

class Nordvpn (NeuronModule):
    def __init__(self, **kwargs):
        # we don't need the TTS cache for this neuron
        cache = kwargs.get('cache', None)
        if cache is None:
            cache = False
            kwargs["cache"] = cache
        super(Nordvpn, self).__init__(**kwargs)

        # get parameters form the neuron
        self.configuration = {
            "param": kwargs.get('param', None),            
        }

        # check parameters
        if self._is_parameters_ok():
            if kwargs['param'] == 'd':
            	os.system("nordvpn d")
            if kwargs['param'] == 'c':
            	#ici vous paramétrez votre connection, c'est la ligne de commande pour se connecter voir man nordvpn
            	os.system("nordvpn connect --group The_Americas")
            if kwargs['param'] == 'status':
            	stat = os.popen("nordvpn status", "r").read()
            	self.say(stat)

    def _is_parameters_ok(self):
        """
        Check if received parameters are ok to perform operations in the neuron
        :return: true if parameters are ok, raise an exception otherwise
        .. raises:: InvalidParameterException
        """
        
        if self.configuration['param'] is None:
            raise InvalidParameterException("NordVpn a besoin d'un paramètre c=connect, d=deconnect ou status") 

        return True
