from runner import navigator
from config.config import Config

URL_API = 'https://dns.projectdiscovery.io/dns/{0}/subdomains'
DOMAINS_LIST = []


def returnDomains(domain, silent=False):
    req = navigator.Navigator()
    keys = Config().read('chaos')
    if keys:
        for key in keys:
            json = req.downloadResponse(URL_API.format(domain), 'JSON', 'GET', header={'Authorization': key})
            try:
                for _ in json['subdomains']:
                    DOMAINS_LIST.append('{0}.{1}'.format(_, domain))
                if not silent:
                    req.ModuleLoaded('project discovery chaos ', DOMAINS_LIST)
                return DOMAINS_LIST
            except:
                return []
    else:
        return []
