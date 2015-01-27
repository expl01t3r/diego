print('''
                                                                     
 _|_|_|          _|_|_|        _|_|        _|      _|        _|_|_|  
 _|    _|      _|            _|    _|      _|_|    _|      _|        
 _|_|_|          _|_|        _|_|_|_|      _|  _|  _|        _|_|    
 _|    _|            _|      _|    _|      _|    _|_|            _|  
 _|_|_|    _|  _|_|_|    _|  _|    _|  _|  _|      _|  _|  _|_|_|    

         Break Security - Automated Network Scanner
''')
import nmap
import argparse


nscan = nmap.PortScanner()
op = argparse.ArgumentParser()
op.add_argument('--alvo', action = 'store', dest = 'alvo', required = False, help = 'Digite o IP do alvo')
op.add_argument('--porta', action = 'store', dest = 'porta', required = False, help = 'Digite a(s) porta(s) que serão escaneadas')
ps = op.parse_args()

print('Inicando escaneamento\n')
result = nscan.scan(ps.alvo, ps.porta)


#test
print(result['scan'][ps.alvo]['tcp'])
print(list(result['scan'][ps.alvo]['tcp'].keys()))
print('-'*50)
print(list(result['scan'][ps.alvo]['tcp'].values()))
