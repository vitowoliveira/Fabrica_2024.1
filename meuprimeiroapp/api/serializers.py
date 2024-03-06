from rest_framework.serializers import ModeSerializer
from ..models import PessoaBancoDeDados
class PessoaSerializer(ModeSerializer):
    class Meta: 
    model = PessoaBancoDeDados  
    fieds = ['id', ]