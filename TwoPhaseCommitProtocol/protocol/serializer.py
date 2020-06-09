

def site_to_dict(site):
    site = {
        "name" : site.name,
        "port" : site.port,
        "amount": site.amount,
        "status": site.status.status
    }
    return site

def sites_to_dict(site):
    sites = []
    sites.append({
        "name" : site.name,
        "port" : site.port,
        "amount": site.amount,
        "status": site.status.status
    })
    return sites