import json, requests, sys, inspect
from common import *

url_list = {
    'proto': ['https://', 'http://'],
    'version': ['/v1/', '/v2/'],
    'list_tags': ['repositories/', '/tags'],
    'search': ['search?q=', '&n=', '&page=']
}

def formulate_url(action):
    retreive_variable = registry_connect()
    if action == 'list_tags':
        url = url_list['proto'][0] +  retreive_variable.node + url_list['version'][0] + url_list['list_tags'][0] + retreive_variable.repository_namespace + url_list['list_tags'][1]
    elif action == 'search':
        url = url_list['proto'][0] +  retreive_variable.node + url_list['version'][0] + url_list['search'][0] + retreive_variable.search_name + url_list['search'][1] + str(retreive_variable.num_results) + url_list['search'][2]
    return url
    
def get_json(url):
    r = requests.get(url)
    if r.encoding is None:
        r.encoding = 'utf-8'
    
    try:
        data = r.json()
    except ValueError:
        print 'ValueError: No JSON object could be decoded.'
        return
    
    return data

class registry_connect(object):
    
    def __init__(self, node=None):
        self.node = node
        if self.node is None:
            self.node = 'registry.hub.docker.com'
    
    def list_tags(self, repository_namespace=None):
        registry_connect.repository_namespace = self.repository_namespace = repository_namespace
        
        if self.repository_namespace is None:
            exception_handlers(errorTypes='TypeError', msg='Namespace Argument not provided.')
            return

        url = formulate_url(inspect.stack()[0][3])
        data = get_json(url)
        
        docker_tags = []
        for item in data:
            docker_tags.append(item['name'])
        
        return docker_tags
 
    def search(self, **kwargs):
        registry_connect.search_name = self.search_name = kwargs.get('search_name', 'empty')
        registry_connect.num_results = self.num_results = kwargs.get('num_results', 100)
        registry_connect.is_automated = self.is_automated = kwargs.get('is_automated', False)
        registry_connect.is_trusted = self.is_trusted = kwargs.get('is_trusted', False)
        registry_connect.is_official = self.is_official = kwargs.get('is_official', False)
        
        if self.search_name == 'empty':
            exception_handlers(errorTypes='TypeError', msg='Namespace Argument not provided.')
            return
        
        url = str(formulate_url(inspect.stack()[0][3])) + str(1)
        data = get_json(url)
        
        docker_search_results = []
        
        for i in range(1,data['num_pages']+1):
            url_pg_number = str(formulate_url(inspect.stack()[0][3])) + str(i)
            search_result = get_json(url_pg_number)

            for item in search_result['results']:
                if self.is_official:
                    if not item['is_official']:
                        continue
                if self.is_trusted:
                    if not item['is_trusted']:
                        continue
                if self.is_automated:
                    if not item['is_automated']:
                        continue
                del item['is_automated']
                del item['is_trusted']
                del item['is_official']
                docker_search_results.append(item)
        
        return docker_search_results
        

        